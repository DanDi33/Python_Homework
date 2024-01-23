# Есть три кортежа целых чисел необходимо найти эле-
# менты, которые есть в каждом из кортежей и находятся
# в каждом из кортежей на той же позиции.
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = (1, 2, 1, 11, 2, 6, 3, 1)
c = (3, 2, 3, 3, 23, 6, 2)
d = []
len_cort = len(a)
if len_cort > len(b):
    len_cort = len(b)
if len_cort > len(c):
    len_cort = len(c)
print(a, b, c, sep="\n")
for i in range(len_cort):
    if a[i] == b[i] and b[i] == c[i]:
        d.append(a[i])
print("Общими для 3х кортежей являются:", end=" ")
[print(el, end=" ") for el in d]
