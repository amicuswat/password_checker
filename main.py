

def main():
    password = input('Введите пароль:')

    if len(password) > 12:
        print('Длинный')
    else:
        print('Короткий')


if __name__ == "__main__":
    main()
