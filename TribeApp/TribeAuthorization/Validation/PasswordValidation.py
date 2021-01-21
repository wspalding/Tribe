import re


def validate_password(password):
    # chek length
    if len(password) < 16:
        return False
    # check if has number
    if not bool(re.search(r'\d', password)):
        return False
    if not bool(re.search(r'[@_!#$%^&*()<>?/|}{~:]', password)):
        return False
    # passed validation
    return True