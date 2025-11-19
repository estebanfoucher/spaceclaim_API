def walk_obj(name, obj, depth=0, seen=None):
    if seen is None:
        seen = set()
    if id(obj) in seen or depth > 3:
        return
    seen.add(id(obj))

    print("  " * depth + f"{name}: {type(obj)}")

    try:
        for attr in dir(obj):
            if attr.startswith("_"):
                continue
            try:
                value = getattr(obj, attr)
            except Exception:
                continue
            walk_obj(f"{name}.{attr}", value, depth + 1, seen)
    except Exception:
        pass

for name, obj in globals().items():
    if not name.startswith("_"):
        walk_obj(name, obj)