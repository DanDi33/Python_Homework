import random


def bubble_sort(start_arr):
    arr2 = start_arr.copy()
    check = True
    count = 0
    while check:
        check = False
        for i in range(len(arr2) - 1):
            if arr2[i] > arr2[i + 1]:
                arr2[i], arr2[i + 1] = arr2[i + 1], arr2[i]
                check = True
            count += 1
    return arr2, count


def my_bubble_sort(start_arr):
    arr1 = start_arr.copy()
    count = 0
    i = 1
    while i < (len(arr1)):
        if arr1[i - 1] > arr1[i]:
            arr1[i - 1], arr1[i] = arr1[i], arr1[i - 1]
            i = 0
        count += 1
        i += 1

    return arr1, count


def quick_sort(arr1, reverse=False, counter=1):
    if len(arr1) < 2:
        return arr1, counter
    pivot = arr1[len(arr1) // 2]
    pivot_arr = [el for el in arr1 if el == pivot]
    left_side = [el for el in arr1 if el < pivot]
    right_side = [el for el in arr1 if el > pivot]
    sorted_left, counter_l = quick_sort(left_side, reverse, counter)
    sorted_right, counter_r = quick_sort(right_side, reverse, counter)
    if reverse:
        return sorted_right + pivot_arr + sorted_left, counter + counter_r + counter_l
    else:
        return sorted_left + pivot_arr + sorted_right, counter + counter_r + counter_l


if __name__ == '__main__':
    a = int(input("Введите длину массива: "))
    # a = 10
    arr = []
    [arr.append(random.randint(-a, a)) for i in range(a)]
    print(f"\nИсходный массив: {arr}\n")
    arr_bs, count1 = bubble_sort(arr)
    arr_mbs, count2 = my_bubble_sort(arr)
    arr_qs, count3 = quick_sort(arr)
    print(f"Вариант 1. Сортировка(с проверкой на количество перестановок): {arr_bs}.\nКоличество циклов: {count1}\n")
    print(f"Вариант 2. Сортировка(без проверки на количество перестановок): {arr_mbs}.\nКоличество циклов: {count2}\n")
    print(f"Вариант 3. Сортировка(quick sort, рекурсия): {arr_qs}.\nКоличество рекурсивных переходов: {count3}")

