file_name = "lab2.txt"
count_symbols = 0
vowel_letters = "aoeiuауоыиэяюёе"
count_vow = 0
consonant_letters = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ"
count_cons = 0
# digits = "1234567890"
count_dig = 0
with open(file_name, 'rt', encoding="utf-8") as file:
    text = file.readlines()

    [print(el, end="") for el in text]

    for line in text:
        count_symbols += len(line)
        for i in line:
            if i.lower() in vowel_letters:
                count_vow += 1
            if i.lower() in consonant_letters:
                count_cons += 1
            if i.isdigit():
                count_dig += 1
            # if i in digits:
            #     count_dig += 1
    print(f"\n\nКоличество символов: {count_symbols}")
    print(f"Количество строк: {len(text)}")
    print(f"Количество гласных: {count_vow}")
    print(f"Количество согласных: {count_cons}")
    print(f"Количество цифр: {count_dig}")
