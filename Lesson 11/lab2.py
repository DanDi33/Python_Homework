import random


def rating():
    print("\nПрограмма \"Успеваемость.\"\n\n"
          "1. Вывести список оценок.\n"
          "2. Пересдача.\n"
          "3. Стипендия.\n"
          "4. Вывести отсортированный список по возрастанию.\n"
          "5. Вывести отсортированный список по убыванию."
          )
    match input("\nВведите число: "):
        case "1":
            print("\nОценки: ", end="")
            [print(el, end=" ") for el in arr]
            print()
        case "2":
            print("Какую оценку хотите пересдать?")
            [print(f"{i + 1}: {arr[i]}") for i in range(len(arr))]
            change = int(input("\nВведите порядковый номер оценки, которую хотите заменить: "))
            prev = arr[change - 1]
            arr[change - 1] = int(input("\nВведите новую оценку: "))
            print(f"\nОценка {prev} исправлена на {arr[change - 1]}")
        case "3":
            print(f"\nСтипендия начисляется при среднем бале выше 10,7. Ваш средний бал: {sum(arr) / len(arr)}\n")
            print("Стипендия не начислена.") if sum(arr) / len(arr) < 10.7 else print("Стипендия начислена")
        case "4":
            print(f"\nОценки по возрастанию: ", end="")
            [print(el, end=" ") for el in quick_sort(arr)]
            print()
        case "5":
            print(f"\nОценки по убыванию: ", end="")
            [print(el, end=" ") for el in quick_sort(arr, True)]
            print()
        case _:
            print("\nНекорректный ввод")
    if input("\nПерейти в главное меню(y/n)? ") == "y":
        rating()


def quick_sort(arr1, reverse=False):
    if len(arr1) < 2:
        return arr1
    pivot = arr1[len(arr1) // 2]
    pivot_arr = [el for el in arr1 if el == pivot]
    left_side = [el for el in arr1 if el < pivot]
    right_side = [el for el in arr1 if el > pivot]
    sorted_left = quick_sort(left_side, reverse)
    sorted_right = quick_sort(right_side, reverse)
    if reverse:
        return sorted_right + pivot_arr + sorted_left
    else:
        return sorted_left + pivot_arr + sorted_right


if __name__ == '__main__':
    a = int(input("Введите длину массива: "))
    # a = 10
    arr = []
    [arr.append(random.randint(1, 12)) for i in range(a)]

    rating()
