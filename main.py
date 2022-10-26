

def has_digits(password):
    for letter in password:
        if letter.isdigit():
            return True


def has_letters(password):
    for letter in password:
        if letter.isalpha():
            return True


def has_upper_letters(password):
    for letter in password:
        if letter.isupper():
            return True


def has_lower_letters(password):
    for letter in password:
        if letter.islower():
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
        has_lower_letters
    ]

    score = 0

    for func in checks:
        if func(password):
            score += 2

    print(f'Рейтин пароля: {score}')


if __name__ == "__main__":
    main()
