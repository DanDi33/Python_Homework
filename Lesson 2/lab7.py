buyer1 = int(input("Введите продажи 1го менеджера: "))
buyer2 = int(input("Введите продажи 2го менеджера: "))
buyer3 = int(input("Введите продажи 3го менеджера: "))
print("*"*30)
if buyer1 > 0 or buyer2 > 0 or buyer3 > 0:
    if buyer1 < 500:
        buyer1 = 200 + buyer1 * 0.03
    elif 500 <= buyer1 < 1000:
        buyer1 = 200 + 500 * 0.03 + (buyer1 - 500) * 0.05
    else:
        buyer1 = 200 + 500 * 0.03 + 500 * 0.05 + (buyer1 - 1000) * 0.08
    print(f"Зарплата 1го продавца: {buyer1}")
    if buyer2 < 500:
        buyer2 = 200 + buyer2 * 0.03
    elif 500 <= buyer2 < 1000:
        buyer2 = 200 + 500 * 0.03 + (buyer2 - 500) * 0.05
    else:
        buyer2 = 200 + 500 * 0.03 + 500 * 0.05 + (buyer2 - 1000) * 0.08
    print(f"Зарплата 2го продавца: {buyer2}")
    if buyer3 < 500:
        buyer3 = 200 + buyer3 * 0.03
    elif 500 <= buyer3 < 1000:
        buyer3 = 200 + 500 * 0.03 + (buyer3 - 500) * 0.05
    else:
        buyer3 = 200 + 500 * 0.03 + 500 * 0.05 + (buyer3 - 1000) * 0.08
    print(f"Зарплата 3го продавца: {buyer3}")
    print("*" * 30)
    if buyer1 > buyer2 and buyer1 > buyer3:
        print(f"1ый продавец - лучший!!! Он заработал с учетом премии 200$: {buyer1 + 200}$")
    elif buyer2 > buyer1 and buyer2 > buyer3:
        print(f"2ый продавец - лучший!!! Он заработал с учетом премии 200$: {buyer2 + 200}$")
    else:
        print(f"3ый продавец - лучший!!! Он заработал с учетом премии 200$: {buyer3 + 200}$")
else:
    print("Некорректное значение продаж")
