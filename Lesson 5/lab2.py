str_comp = input("Введите строку: ")
# str_comp = ("What is Lorem Ipsum? Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem "
#             "Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a "
#             "galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, "
#             "but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in "
#             "the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with "
#             "desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
# print(str_comp)
str_comp = str_comp.split(" ")
arr_words = []
print("Создание массива зарезервированных слов. Для прекращения введите 'y'")
while True:
    word = input("Введите слово: ")
    if word == "y":
        break
    arr_words.append(word)
print(f"Массив зарезервированных слов: \n{arr_words}")
for elem in arr_words:
    if arr_words.count(elem) != 0:
        for i in range(len(str_comp) - 1):
            if str_comp[i].lower() == elem.lower():
                str_comp[i] = str_comp[i].upper()
print(f'Итоговый результат:\n{" ".join(str_comp)}')
