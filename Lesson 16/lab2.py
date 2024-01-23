from time import time


def how_long(func):
    def wrapper(start_range, end_range):
        t1 = time()
        print(func(start_range, end_range))
        t2 = time()
        print(f"Затраченное время (сек): {t2 - t1}")

    return wrapper


@how_long
def simple_num(start_range, end_range):
    arr = []
    if isinstance(start_range, int) and isinstance(end_range, int):
        if start_range > end_range:
            start_range, end_range = end_range, start_range
        for elem in range(start_range, end_range + 1):
            count = 0
            if elem != 0:
                for divider in range(1, abs(elem) + 1):
                    if abs(elem) % divider == 0:
                        count += 1
                    if count == 3:
                        break
                if count < 3:
                    arr.append(elem)
    return arr


simple_num(1000, 1)
