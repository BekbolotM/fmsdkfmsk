values = ("turusbekova 109/1", 10, 1005, ["tables", "chairs"], 23.00)


def check(val):
    try:
        set(val)
    except:
        return False
    else:
        return True


n_list = list(map(check, values))

if all(n_list):
    print('Мы можем конвертировать')
else:
    print('Net')
