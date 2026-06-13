def password_validator(password: str):
    status = "weak"
    if len(password) >= 8 and any(l.isupper() for l in password) and any(l.isdigit() for l in password):
        status = "strong"
    elif len(password) >= 7:
        status = "medium"
    return {"strength": status}