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

for name, obj in globals().items():
    if name.startswith("_"):
        continue
    try:
        meths = list_methods(obj)
    except Exception:
        continue
    if meths:
        print(name, "=>", ", ".join(sorted(meths)))