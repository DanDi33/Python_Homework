def counter_add(n):
    k = int(input("Введите число: "))

    def inner():
        return k + n

    return inner


cnt = counter_add(2)
print(cnt())
