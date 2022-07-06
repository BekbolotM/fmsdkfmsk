# Задание №1
# a = [x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]
# print(sum(a))

# Задание №2:
# a = 333
# b = 555
# a, b = b, a
# print('A = ', a , 'B = ', b)

# Задание №3:
# a = '4729461084'
# b = int(a)
# suma = 0
#
# while b > 0:
#     digit = b % 10
#     suma = suma + digit
#     b = b // 10
#
# print("Сумма:", suma)

# Задание №4:
# a = input ('введите дату в формате "2020-10-24 18:30" :')
# date = {}
#
# date['year = '] = a[0:4:]
# date['month ='] = a[5:7]
# date['day = '] = a[8:10]
# date["o'clock"] = a[-5::]
# print(date)

# Задание №5:
# a = 'Hello'
# b = a + a + a + a + a
# c = len(b)
# conv1 = c / 5
# print('Получаем число: ', conv1)
# a = 'Python3'
# b = a * 7
# c = len(b)
# conv = c / 7
# print('Получаем число: ', conv)

# Задание №6:
# mkdir /dream_team/tut

#Задание №7
# Вариант 1
# 1. Открыть терминал
# 2. ls
# 3. cd /home
# 4. ls
# 5. cd /developer
# 6. ls
# 7. cd /Desktop
# Вариант 2
# 1. cd /home/developer/Desktop

#Задача 1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b =[x for x in a if x>5]
# print(b)
#Задача 2
# digits = (113, 118, -5, 1, 135, 137, 0, 142, 144, 17, 154, 0, 155, 2, 159, 172)
# for i in digits:
#     f = i / 9
#     print(f)
#     print(round(f, 2))
# Задача 3
# main_list=[]
# spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
# # main_list = list(set(spisok_2)-set(spisok_1))
# for i in spisok_2:
#     if i not in spisok_1:
#         main_list.append(i)
# for i in spisok_1:
#     if i not in spisok_2:
#         main_list.append(i)
#
# print(main_list)



# Задание 3
# a = [2, 4, 7, 1, 8.4, -3.3, 7.1, -2, 4, -1, 7, -43, 8, -3, 6, 9]
# even = -1
# odd = 1
#
# for i in a:
#     if int(i) % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#
# print("Even: %d, odd: %d" % (even, odd))

#Задание 4
# a = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
# b = []
# for i in a:
#     if i > 0:
#         b.append(1)
#     elif i < 0:
#         b.append(-1)
#     else:
#         b.append(0)
#
# print(a)
# print(b)

#Задание 5
# a = [2,4,6,8,10,1,3,5,7,9,11,13,17]
# chet = []
# for i in range(len(a)):
#     a[i] = int(a[i])
#     if a[i] % 2 == 0:
#         chet.append(str(a[i]))
# print(' '.join(chet))

#Задание 6
# a = [1,0,-2,4,3,6,6,3,5,8,4,2]
# c= []
# for i in range(len(a) - 1):
#     n = a[i]
#     i += 1
#     m = a[i]
#     if m > n:
#         c.append(m)
# print(f'numbers{a}', f'результат {c}')

