def sort_list(func):
    def wrapper(str):
        arr = func(str)
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    return wrapper


@sort_list
def get_list(str):
    return [int(num) for num in str.split()]


lst = get_list("18 3 23 9 6 5 4 78")
print(*lst)
