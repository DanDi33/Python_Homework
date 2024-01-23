try:
    with open('lab4_text.txt', 'rt', encoding='utf-8') as file:
        lines = file.readlines()
        print('Текст файла:')
        [print(lines[i][:-1]) if i < len(lines) - 1 else print(lines[i]) for i in range(len(lines))]
        max_index = 0
        for i, line in enumerate(lines):
            if len(line) > len(lines[max_index]):
                max_index = i
        print(f'\nСамой длинной является {max_index + 1} строка. \nТекст строки: \"{lines[max_index][:-1]}\"')
except:
    print("Error")
