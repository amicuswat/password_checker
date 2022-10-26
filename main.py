

def has_digits(password):
    found_digits = False
    for letter in password:
        if letter.isdigit():
            found_digits = True
            break

    return found_digits


def is_very_long(password):
    return len(password) > 12


def main():
    password = input('Введите пароль:')

    print(has_digits(password))
    print(is_very_long(password))


if __name__ == "__main__":
    main()
