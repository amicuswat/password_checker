

def has_digits(password):
    for letter in password:
        if letter.isdigit():
            return True

    return False


def is_very_long(password):
    return len(password) > 12


def main():
    password = input('Введите пароль:')

    print(has_digits(password))
    print(is_very_long(password))


if __name__ == "__main__":
    main()
