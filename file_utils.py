def get_extension(filename):
    # Intentional bug: "README" incorrectly returns "README"
    return filename.split(".")[-1]
