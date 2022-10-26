

def has_digits(password):
    for letter in password:
        if letter.isdigit():
            return True

    return False


def is_very_long(password):
    return len(password) > 12


def main():
    password = input('Введите пароль: ')

    score = 0

    if has_digits(password):
        score += 2

    if is_very_long(password):
        score += 2

    print(f'Рейтин пароля: {score}')


if __name__ == "__main__":
    main()
