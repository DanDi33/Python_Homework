def pig_latin(str):
    arr = str.split()
    for i in range(len(arr)):
        if arr[i][-1] in [".", ",", "!", "?"]:
            word, mark = arr[i][:-1], arr[i][-1]
        else:
            word = arr[i]
            mark = ""
        if word.isalpha():
            if word[0].lower() in ["a", "e", "i", "o", "u"]:
                word += "way"
            else:
                word_arr = list(word)
                check_upper = False
                if word_arr[0].isupper():
                    check_upper = True
                word_arr[0] = word_arr[0].lower()
                while word_arr[0] not in ["a", "e", "i", "o", "u"]:
                    temp = word_arr.pop(0)
                    word_arr.append(temp)
                    word = "".join(word_arr) + "ay"
                if check_upper:
                    word = word.title()
        arr[i] = word + mark
    return " ".join(arr)


if __name__ == '__main__':
    # text = input("Введите текст: ")
    text = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the "
            "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and "
            "scrambled it to make a type specimen book.")
    print(f"Ваш текст: \"{text}\"")
    print(f"Поросячья латынь: \"{pig_latin(text)}\"")
