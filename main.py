

def main():
    password = input('Введите пароль:')

    if len(password) > 12:
        print('Длинный')
    else:
        print('Короткий')

    for letter in password:
        if letter.isdigit():
            print(f'{letter} - Цифра')
        else:
            print(f'{letter} - Буква')


if __name__ == "__main__":
    main()
