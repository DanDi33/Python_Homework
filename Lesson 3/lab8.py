num = input("Введите число: ")
res = ""
for i in range(len(num)):
    if num[i] != "6" and num[i] != "3":
        res += num[i]
print("*"*30)
print(f"Убираем 3 и 6 из числа и получаем: {res}")
