def sum_arrays(b=False, *, arr1, arr2):
    arr1_1 = arr1.copy()
    arr2_1 = arr2.copy()
    if not b:
        # Вариант 1
        # arr1_1.extend(arr2_1)
        # return arr1_1

        # Вариант 2
        return arr1_1+arr2_1
    else:
        arr3 = []
        for el in arr1_1:
            if el not in arr3:
                arr3.append(el)
        for el in arr2_1:
            if el not in arr3:
                arr3.append(el)
        return arr3


print(sum_arrays(arr1=[1, 2, 3, 4], arr2=[4, 5, 6]))
print(sum_arrays(True, arr1=[1, 2, 3, 4], arr2=[4, 5, 6]))
