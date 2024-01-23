def get_cezar_code(str, spred):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dict_rules = {}
    for i in range(len(alphabet)):
        cezar_index = i + int(spred)
        if cezar_index >= len(alphabet) - 1:
            cezar_index -= len(alphabet)
        dict_rules[alphabet[i]] = alphabet[cezar_index]

    coded_arr = []
    for el in str:
        if el.lower() in dict_rules:
            if el.islower():
                coded_arr.append(dict_rules[el.lower()])
            else:
                coded_arr.append(dict_rules[el.lower()].upper())
        else:
            coded_arr.append(el)
    return "".join(coded_arr)


print("\n\t\"Код Цезаря\"")
text = input("\n\tВведите текст: ")
offset = input("\n\tВведите сдвиг: ")
print(f"\n\tВаш код: {get_cezar_code(text, offset)}")
