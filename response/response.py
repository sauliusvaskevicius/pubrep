import validators

def validate_email(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"

def main():
    print(validate_email(input("What's your email address? ")))


if __name__ == "__main__":
    main()
