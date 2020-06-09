a = 2.00
b = 3
c = 10 # процент
n=1
print(f'1-й день: {a}')
while a<=b:
    n += 1
    a = a+(a*c/100)
    print(f'{n}-й день: {"%.2f" % a}')


