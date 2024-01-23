startRange = int(input("Введите начало диапазона: "))
endRange = int(input("Введите конец диапазона: "))
if startRange > endRange:
    startRange, endRange = endRange, startRange
for elem in range(startRange, endRange + 1):
    count = 0
    if elem != 0:
        for divider in range(1, abs(elem) + 1):
            if abs(elem) % divider == 0:
                count += 1
            if count == 3:
                break
        if count < 3:
            print(elem)
# Cложность (по-моему): О от n2. Попытался уменьшить с помощью break при count=3
