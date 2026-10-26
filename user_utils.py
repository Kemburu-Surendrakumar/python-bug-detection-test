
def normalize_username(username):
    return username.strip().lower()


def is_valid_email(email):
    if not isinstance(email, str):
        return False

    if "@" not in email:
        return False

    local, separator, domain = email.partition("@")

    return bool(separator and local and "." in domain and not domain.startswith("."))
