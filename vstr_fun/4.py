summa = int(input('Введите сумму желаемого кредита: '))
if summa >= 50000:
    x = summa * (3.47 / 100)
    print(summa + x)
else:
    print('Сумма должна быть больше 50 000')
