a = int(input('Chislo: '))
if a != 0:
  print('Ne pusto')
  if a > 0:
    print('Chislo bolshe 0')
    if a % 2 == 0:
      print('Chetnoe chislo')
      if a % 2 == 1:
        print('Chislo nechetnoe')
else:
  print('Ok')
