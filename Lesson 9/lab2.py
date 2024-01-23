print("\n\t\"Проверка на анаграмму\"\n\t")
# word = "выбор"
word = input("\tВведите 1ое слово: ")
# anagram = "обрыв"
anagram = input("\tВведите 2ое слово: ")


def check_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    arr_w = [el for el in word1]
    arr_a = [el for el in word2]
    check = True
    for i in range(len(arr_w)):
        if arr_w[i] in arr_a:
            arr_a.pop(arr_a.index(arr_w[i]))
    if len(arr_a) != 0:
        check = False
    return check


def check_anagram1(word1, word2):
    if len(word1) != len(word2):
        return False
    arr_w = [el for el in word1]
    arr_a = [el for el in word2]
    check = True
    for i in range(len(arr_w)):
        if arr_w[i] in arr_a:
            arr_a.pop(arr_a.index(arr_w[i]))
    if len(arr_a) != 0:
        check = False
    return check


if check_anagram(word, anagram):
    print(f"\n\t\"{anagram}\" - это анаграмма слова \"{word}\"")
else:
    print(f"\n\t\"{anagram}\" - это не является анаграммой слова \"{word}\"")
