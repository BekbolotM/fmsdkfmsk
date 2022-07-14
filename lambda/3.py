eat = input('Что вы бы хотели покушать? ')
drink = input('А пить что будите? ')
with open(f'/home/converge/Рабочий стол/menu.txt', 'w') as f:
    f.write('Блюдо: ' f'{eat}\n')
    f.write('Напиток: ' f'{drink}')

