a = (0)
b = (1)
numbers = []
try:
    while b > a:
        numbers += b
        b += 1
except TypeError:
    print('Упс, сорян ошибочка')
