# Есть три кортежа целых чисел необходимо найти
# элементы, которые уникальны для каждого списка.
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = (1, 1, 1, 11, 2, 1, 3, 1)
c = (3, 3, 3, 3, 23, 3, 2, 3)
d = []
print(a, b, c, sep="\n")
for el in a:
    if el not in d and el not in b and el not in c:
        d.append(el)
for el in b:
    if el not in d and el not in a and el not in c:
        d.append(el)
for el in c:
    if el not in d and el not in b and el not in a:
        d.append(el)
print("Уникальными для 3х кортежей являются:", end=" ")
[print(el, end=" ") for el in d]