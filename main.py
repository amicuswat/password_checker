

def main():
    password = input('Введите пароль:')

    if len(password) > 12:
        print('Длинный')
    else:
        print('Короткий')

    found_digits = False
    for letter in password:
        if letter.isdigit():
            found_digits = True
            break

    if found_digits:
        print('Есть цифры')
    else:
        print('Нет цифр')


if __name__ == "__main__":
    main()
