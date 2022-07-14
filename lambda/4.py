def slovo():
    a = input('Введите слово: ')
    with open(f'{a}.txt', 'w') as f:
        f.write('Ваше слово: ' f'{a}')


slovo()
