for i in range(5):
  name = input('Введите Ваше имя: ')
  prof = input('Ваша профессия: ')
  names = {}
  names[name] = prof
  print(f'Здравствуйте ', {name}, 'Прекрасная профессия ', {prof})
