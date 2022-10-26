

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

    score = 0

    if has_digits(password):
        score += 2

    if is_very_long(password):
        score += 2

    if has_letters(password):
        score += 2

    if has_upper_letters(password):
        score += 2

    if has_lower_letters(password):
        score += 2

    print(f'Рейтин пароля: {score}')


if __name__ == "__main__":
    main()
