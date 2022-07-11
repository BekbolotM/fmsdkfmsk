at = 10
it = 15
wo = 20
try:
    for e in range(-at, at):
        print(wo / e)
        if at > 5:
            print("at" > 5)
except SyntaxError:
    print('Salam')
except TypeError:
    print('Ошибка типов данных')
