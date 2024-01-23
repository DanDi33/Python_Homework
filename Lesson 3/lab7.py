startRange = 100
endRange = 9999
count = 0
for el in range(startRange, endRange + 1):
    el = str(el)
    if len(el) < 4:
        el += "a"
    if (el[0] != el[1]
            and el[0] != el[2]
            and el[0] != el[3]
            and el[1] != el[2]
            and el[1] != el[3]
            and el[2] != el[3]):
        count += 1
        print(el)
print(f"Количество целых чисел, у которых все цифры неравны, равно: {count}")
