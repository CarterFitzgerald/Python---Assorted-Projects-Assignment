password = str(input("Enter a string for password: "))


def len_check():
    while len(password) < 8:
        return "invalid"


def symbol_check():
    sym_check = password.isalnum()
    if sym_check:
        return "valid"
    else:
        return "invalid"


def number_check():
    if len([x for x in password if x.isdigit()]) < 2:
        return "invalid"
    else:
        return "valid"


def validity_check():
    if len_check() == "invalid":
        return "invalid password"
    elif symbol_check() == "invalid":
        return "invalid password"
    elif number_check() == "invalid":
        return "invalid password"
    else:
        return "valid password"


def main():
    if validity_check() == "invalid password":
        print("invalid password")
    else:
        print("valid password")


main()
