def upload_path(instance, filename):
    try:
        model = instance.__class__.__name__.lower()
    except:
        model = "unknown"
    return f"{model}/{instance.id}/{filename}"
