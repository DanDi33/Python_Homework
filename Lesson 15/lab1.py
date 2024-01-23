def counter_add():
    k = int(input("Введите число: "))

    def inner():
        return k + 5

    return inner


cnt = counter_add()
print(cnt())
