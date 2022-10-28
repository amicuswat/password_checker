

def has_digits(password):
    return any(letter.isdigit() for letter in password)


def has_letters(password):
    return any(letter.isalpha() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_symbols(password):
    symbols = ".,:;!_*-+()/#%&"
    for letter in password:
        if letter in symbols:
            return True


def is_very_long(password):
    return len(password) > 12


def main():
    password = input('Введите пароль: ')

    checks = [
        has_digits,
        is_very_long,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]

    score = 0

    for func in checks:
        if func(password):
            score += 2

    print(f'Рейтин пароля: {score}')


if __name__ == "__main__":
    main()
