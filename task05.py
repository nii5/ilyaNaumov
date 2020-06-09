def det_number(str):
    while True:
        num = input(str)
        if num.isdigit():
            num = int(num)
            break
        else:
            print('Вы ввели не числое значение')
    return num

revenue =det_number('Введите выручку фирмы: ')
costs = det_number('Введите  издержки фирмы: ')
profit = revenue - costs
if profit>0:
    profitability = float(profit/revenue)
    strength = det_number('Введите  численность сотрудников фирмы: ')
    print(f'Прибыль фирмы составила {profit} и рентабельностью {profitability}.'
          f'Прибыль на одного сотрудника составила {strength}')
else:
    print(f'Фирма сработала в убыток {profit}')
