startRange = 100
endRange = 999
count = 0
for el in range(startRange, endRange+1):
    tmp = str(el)
    if tmp[0] == tmp[1] or tmp[1] == tmp[2] or tmp[2] == tmp[0]:
        count += 1
        print(el)
    # if tmp[0] == tmp[1] and tmp[1] == tmp[2] and tmp[2] == tmp[0]:
    #     count -= 1
    #     print("!"+tmp+"!")
print(f"Количество целых чисел у которых 2 одинаковые цифры равно: {count}")
