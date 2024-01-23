def polidrom(num):
    num = abs(num)
    a = str(num)
    arr = list(a)
    if len(arr) % 2 != 0:
        arr.pop(int(len(arr) / 2))
    for i in range(int(len(arr) / 2)):
        if arr[i] != arr[len(arr) - (i + 1)]:
            return False
    return True


print(f"Переданное число палиндром? {polidrom(124421)}")
