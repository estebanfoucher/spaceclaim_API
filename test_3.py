log_path = "spaceclaim_globals.log"  # change to absolute path if you like

def list_methods(obj):
    methods = []
    for attr in dir(obj):
        if attr.startswith("_"):
            continue
        try:
            value = getattr(obj, attr)
        except Exception:
            continue
        if callable(value):
            methods.append(attr)
    return methods

with open(log_path, "w") as f:
    for name, obj in globals().items():
        if name.startswith("_"):
            continue
        try:
            meths = list_methods(obj)
        except Exception:
            continue
        if not meths:
            continue
        f.write(name + ":\n")
        for m in sorted(meths):
            f.write("  - " + m + "\n")
        f.write("\n")

print("Wrote globals/methods to " + log_path)