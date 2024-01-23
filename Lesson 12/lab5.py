founded_word = input("Введите слово для поиска в файле: ")
count = 0
try:
    with open('lab5_lorem.txt', 'rt', encoding='utf-8') as file:
        lines = file.readlines()
        print('\nТекст файла:')
        [print(lines[i][:-1]) if i < len(lines) - 1 else print(lines[i]) for i in range(len(lines))]
        for i, line in enumerate(lines):
            lines[i] = line[:-1]
            words = lines[i].split()
            for j, word in enumerate(words):
                if word[-1] in ".,!?:;'\"" and word[:-1].lower() == founded_word.lower() or words[j].lower() == founded_word.lower():
                    count += 1
        print(f'\nСлово \"{founded_word}\" встречает в текстовом файле: {count} раз(а)')
except Exception as exc:
    print("Cannot open the file:", exc)
