# DREAM TEAM!!! #
# Задание 1
# import random as rd
#
# print('Добро пожаловать в игру! "Угадайте число"')
#
# x = 0
#
# while True:
#     try:
#         num = int(input('Введите Ваше число (0 - 10): '))
#         x += 1
#         if num > 0 and num != False:
#             random_number = rd.randint(0, 10)
#             print('Выпало число:', random_number)
#             if num == random_number:
#                 print('Вы угадали!!!')
#                 break
#             elif x == 3:
#                 print('Вы проиграли')
#                 break
#     except ValueError:
#         print('Мы принимаем только число!!!')

# Задание 2
# while True:
#     try:
#         symbol = int(input('Введите цифру: '))
#         if symbol == 0:
#             break
#         print(chr(symbol))
#     except ValueError:
#         print('Упс, что-то не так')

# Задание 3
# a = input('Введите Ваше слово: ')
# if len(a) > 10:
#     print("Слишком длинная строка")
# else:
#     for i in range(len(a), 10):
#         a += "*"
#     print(a)

# Задание 4
# arr = []
# try:
#     for i in range(6):
#         arr.append(float(input("Введите вещественные числа -> ")))
#
#     max = arr[0]
#     min = arr[0]
#
#     for i in arr:
#         if max > i:
#             max = i
#         else:
#             min = i
# except ValueError:
#     print('Принимается через "." ')
# print(f"Max значение: {round(max, 2)} | Min значение: {round(min, 2)}")


# Задание 9
# def nums(x, y):
#     return x * y
#     nums2()
#
#
# def nums2(a, b):
#     return a / b
#
#
# print(nums(2, 2) + nums2(10, 2))

# Задания 11
# dict_one = {'a': 1, 'b': 2, 'c': 3}
# dict_two = {'d': 4, 'e': 5, 'f': 6}
# dict_three = {'g': 7, 'h': 8, 'i': 9}
# dict_four = {}
#
# for key, value in dict_one.items():
#     dict_four[key] = value
#     for key, value in dict_two.items():
#         dict_four[key] = value
#         for key, value in dict_three.items():
#             dict_four[key] = value
#
# print(dict_four)

# Задание 13
# a = [-5, 77, -10, 5, 3, 7, -8, -111, 100]
#
# b = [i for i in a if i < 0]
# c = [i for i in a if i >= 0]
#
# print(f'Отрицательные числа:{b}\nПоложительные числа:{c}')
### Вариант 2
# a = []
# b = []
# c = []
# m = []
# for i in range(10):
#     numbers = int(input())
#     if numbers > 0:
#         a.append(i)
#         c.append(numbers)
#     else:
#         b.append(i)
#         m.append(numbers)
# print('положительные число: ', c)
# print('отрицательные число: ', m)

# Задание 14
# b = int(input("Введите номер месяца (1-12): "))
#
#
# def vremia(a):
#     if a == 12 or 1 <= a <= 2:
#         print("Зима")
#     elif 3 <= a <= 5:
#         print("Весна")
#     elif 6 <= a <= 8:
#         print("Лето")
#     elif 9 <= a <= 11:
#         print("Осень")
#     else:
#         print("Неверно введён номер месяца!")
#
#
# vremia(b)

# Задание 15
# def bank():
#     stavka = 10
#     a = int(input("Сумма вклада? "))
#     years = int(input("На сколько лет хотите сделать вклад? "))
#
#     for i in range(years):
#         a = int(a + stavka * a / 100)
#         print("По итогу вы получаете", a, "сомов")
#
#
# bank()

# Задание 16
# a = 0
# days = -1
# summ = 0
#
# while a > -300:
#     summ += a
#     days += 1
#     a = float(input('Введите значения: '))
# print(summ / days)
