

def main():
    password = input('Введите пароль:')

    if len(password) > 12:
        print('Длинный')
    else:
        print('Короткий')

    if password.isdigit():
        print('Цифра')
    else:
        print('Буква')


if __name__ == "__main__":
    main()
