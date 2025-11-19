"""
Utilities to generate Python stub classes from the SpaceClaim HTML API docs.

This script walks the ``html/`` folder, discovers documented types and members
based on Microsoft Help metadata, and emits simple ``.py`` stubs into
``spaceclaim_API/_generated`` with class definitions and empty methods.

The goal is not to perfectly model the API, but to provide enough structure
for IDEs and linters to recognize names and call signatures.
"""

from __future__ import annotations

import html
import os
import re
from dataclasses import dataclass, field
import keyword
from pathlib import Path
from typing import Dict, List, Optional

RE_HELP_ID = re.compile(
    r'<meta[^>]+name="Microsoft\.Help\.Id"[^>]+content="([^"]+)"',
    re.IGNORECASE,
)
RE_DESCRIPTION = re.compile(
    r'<meta[^>]+name="Description"[^>]+content="([^"]+)"',
    re.IGNORECASE,
)
RE_SUMMARY_DIV = re.compile(
    r'<div\s+class="summary"\s*>\s*(.*?)\s*</div>',
    re.IGNORECASE | re.DOTALL,
)
RE_PRE_BLOCK = re.compile(
    r"<pre[^>]*>(.*?)</pre>",
    re.IGNORECASE | re.DOTALL,
)


@dataclass
class MethodInfo:
    """Represents a method signature extracted from the docs."""

    name: str
    parameters: List[str] = field(default_factory=list)
    summary: str = ""


@dataclass
class PropertyInfo:
    """Represents a property extracted from the docs."""

    name: str
    summary: str = ""


@dataclass
class FieldInfo:
    """Represents a field extracted from the docs."""

    name: str
    summary: str = ""


@dataclass
class TypeInfo:
    """Represents a documented type (class/struct/etc.)."""

    namespace: str
    name: str
    summary: str = ""
    methods: List[MethodInfo] = field(default_factory=list)
    properties: List[PropertyInfo] = field(default_factory=list)
    fields: List[FieldInfo] = field(default_factory=list)


def _strip_tags(text: str) -> str:
    """Remove rudimentary HTML tags and unescape entities."""
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    return " ".join(text.split())


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _extract_meta_and_summary(html_text: str) -> tuple[Optional[str], str]:
    """Return (help_id, summary/description) for a topic."""
    m_id = RE_HELP_ID.search(html_text)
    help_id = m_id.group(1) if m_id else None

    desc = ""
    m_desc = RE_DESCRIPTION.search(html_text)
    if m_desc:
        desc = _strip_tags(m_desc.group(1))
    else:
        m_summary = RE_SUMMARY_DIV.search(html_text)
        if m_summary:
            desc = _strip_tags(m_summary.group(1))

    return help_id, desc


def _parse_method_signature_from_pre(html_text: str) -> List[str]:
    """
    Heuristically parse parameter names from the first <pre> C# signature.

    This is intentionally conservative; if parsing fails, an empty list is
    returned and the generated method will accept *args, **kwargs.
    """
    m = RE_PRE_BLOCK.search(html_text)
    if not m:
        return []

    pre_html = m.group(1)
    pre_code = _strip_tags(pre_html)

    # Find the opening parenthesis of the parameter list.
    try:
        open_paren = pre_code.index("(")
        close_paren = pre_code.index(")", open_paren)
    except ValueError:
        return []

    param_section = pre_code[open_paren + 1 : close_paren].strip()
    if not param_section:
        return []

    params: List[str] = []
    invalid = False
    for raw_param in param_section.split(","):
        segment = raw_param.strip()
        if not segment:
            continue
        # Remove default value if present.
        if "=" in segment:
            segment = segment.split("=", 1)[0].strip()
        # Take the last token as the parameter name (ignoring modifiers).
        tokens = segment.split()
        if not tokens:
            continue
        name = tokens[-1]
        # Basic C# byref markers we can strip if present.
        name = name.lstrip("*&")
        # Avoid C# params array syntax.
        name = name.replace("[]", "")

        # Only accept names that are valid Python identifiers and not keywords.
        if not name.isidentifier() or keyword.iskeyword(name):
            invalid = True
            break

        params.append(name)

    # If anything looked suspicious, fall back to *args, **kwargs at call-site.
    if invalid:
        return []

    return params


def discover_types_and_members(html_root: Path) -> Dict[str, TypeInfo]:
    """
    Walk the HTML directory and build a mapping from full type name to
    TypeInfo, also attaching methods, properties, and fields.
    """
    types: Dict[str, TypeInfo] = {}

    for dirpath, _, filenames in os.walk(html_root):
        for filename in filenames:
            if not filename.lower().endswith(".htm"):
                continue

            path = Path(dirpath, filename)
            text = _read_text(path)
            help_id, summary = _extract_meta_and_summary(text)
            if not help_id:
                continue

            # help_id is like: "T:SpaceClaim.Api.V15.Scripting.Commands.CurveGaps"
            try:
                kind, full_name = help_id.split(":", 1)
            except ValueError:
                continue

            if kind == "T":
                # Type definition.
                if "." not in full_name:
                    continue
                ns, type_name = full_name.rsplit(".", 1)
                key = full_name
                info = types.get(
                    key,
                    TypeInfo(namespace=ns, name=type_name),
                )
                if summary and not info.summary:
                    info.summary = summary
                types[key] = info

            elif kind in {"M", "P", "F"}:
                # Member belonging to a type.
                # Chop off parameters for methods first.
                base = full_name.split("(", 1)[0]
                if "." not in base:
                    continue
                type_full, member_name = base.rsplit(".", 1)
                type_info = types.get(type_full)
                if not type_info:
                    # If the type page was not seen yet, create a shell.
                    if "." not in type_full:
                        continue
                    ns, type_name = type_full.rsplit(".", 1)
                    type_info = TypeInfo(namespace=ns, name=type_name)
                    types[type_full] = type_info

                if kind == "M":
                    # Skip members whose names are not valid Python identifiers
                    # (for example, #ctor constructor markers from the docs).
                    if not member_name.isidentifier():
                        continue
                    params = _parse_method_signature_from_pre(text)
                    type_info.methods.append(
                        MethodInfo(
                            name=member_name,
                            parameters=params,
                            summary=summary,
                        )
                    )
                elif kind == "P":
                    # Skip non-identifier property names (can appear for some
                    # explicit interface implementations).
                    if not member_name.isidentifier():
                        continue
                    type_info.properties.append(
                        PropertyInfo(name=member_name, summary=summary)
                    )
                elif kind == "F":
                    # Skip non-identifier field names.
                    if not member_name.isidentifier():
                        continue
                    type_info.fields.append(
                        FieldInfo(name=member_name, summary=summary)
                    )

    return types


def build_namespace_index(types: Dict[str, TypeInfo]) -> Dict[str, List[TypeInfo]]:
    by_ns: Dict[str, List[TypeInfo]] = {}
    for t in types.values():
        by_ns.setdefault(t.namespace, []).append(t)
    # Sort for stable output.
    for ns_types in by_ns.values():
        ns_types.sort(key=lambda t: t.name)
    return by_ns


def render_type(info: TypeInfo, indent: str = "") -> str:
    """Render a single TypeInfo as a Python class definition string."""
    lines: List[str] = []
    base_indent = indent
    ind = indent + "    "

    doc = info.summary or f"{info.name} stub generated from SpaceClaim docs."
    lines.append(f"{base_indent}class {info.name}:")
    lines.append(f'{ind}"""' + doc + '"""')
    lines.append("")

    # Fields as simple class attributes.
    for field_info in info.fields:
        if field_info.summary:
            lines.append(f"{ind}# {field_info.summary}")
        lines.append(f"{ind}{field_info.name} = None")
    if info.fields:
        lines.append("")

    # Basic __init__ so instances can be created without errors.
    lines.append(f"{ind}def __init__(self, *args, **kwargs):")
    lines.append(f'{ind}    """Initializes {info.name}. Auto-generated stub."""')
    lines.append(f"{ind}    pass")
    lines.append("")

    # Properties.
    for prop in info.properties:
        lines.append(f"{ind}@property")
        lines.append(f"{ind}def {prop.name}(self):")
        if prop.summary:
            lines.append(f'{ind}    """{prop.summary}"""')
        lines.append(f"{ind}    pass")
        lines.append("")

    # Methods.
    for method in info.methods:
        if method.parameters:
            params = ", ".join(["self"] + method.parameters)
        else:
            params = "self, *args, **kwargs"

        lines.append(f"{ind}def {method.name}({params}):")
        if method.summary:
            lines.append(f'{ind}    """{method.summary}"""')
        lines.append(f"{ind}    pass")
        lines.append("")

    return "\n".join(lines)


def generate_stubs(html_root: Path, out_root: Path) -> None:
    """Entry point to generate all stub modules from documentation."""
    print(f"Scanning docs under: {html_root}")
    types = discover_types_and_members(html_root)
    by_ns = build_namespace_index(types)

    # Wipe the output directory to ensure idempotence.
    if out_root.exists():
        for root, dirs, files in os.walk(out_root, topdown=False):
            for f in files:
                Path(root, f).unlink()
            for d in dirs:
                Path(root, d).rmdir()
    out_root.mkdir(parents=True, exist_ok=True)

    for namespace, ns_types in sorted(by_ns.items()):
        rel_parts = namespace.split(".")
        ns_dir = out_root.joinpath(*rel_parts)
        ns_dir.mkdir(parents=True, exist_ok=True)
        init_path = ns_dir / "__init__.py"

        lines: List[str] = []
        lines.append('"""')
        lines.append(
            f"Auto-generated stubs for namespace: {namespace} "
            f"(from SpaceClaim API docs)."
        )
        lines.append('"""')
        lines.append("")
        lines.append("from __future__ import annotations")
        lines.append("")

        for t in ns_types:
            lines.append(render_type(t))
            lines.append("")

        init_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"Generated {init_path}")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    html_root = repo_root / "html"
    out_root = repo_root / "spaceclaim_API" / "_generated"

    if not html_root.exists():
        raise SystemExit(f"HTML docs directory not found: {html_root}")

    generate_stubs(html_root, out_root)


if __name__ == "__main__":
    main()


