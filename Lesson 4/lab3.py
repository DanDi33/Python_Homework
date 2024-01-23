startRange = int(input("Введите начало диапазона: "))
endRange = int(input("Введите конец диапазона: "))
if startRange > endRange:
    startRange, endRange = endRange, startRange
for i in range(1, 11):
    for j in range(startRange, endRange + 1):
        print(f"{j}*{i}={i * j}", end="\t" * 2)
    print()
