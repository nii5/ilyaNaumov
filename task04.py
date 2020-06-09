'''
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''
while True:
    number = input('Введите число:')
    if number.isdigit():
        str = list(number)
        print(max(str))
        break
    else:
        print('Вы ввели не число')