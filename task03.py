while True:
    n = input('Введите любое число: ')
    if n.isdigit():
        nn = int(n + n)
        nnn = int(n + n +n)
        n = int(n)

        print(n + nn + nnn)
        break
    else:
        print('Вы ввели не число')