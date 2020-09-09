def main():
    email_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirmation = input("Is this your name {}? (Yes/no) ".format(name))
        if confirmation.upper() != "Yes" and confirmation != "":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")

    for email, name in email_name.items():
        print("{} ({})".format(name, email))


def get_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
