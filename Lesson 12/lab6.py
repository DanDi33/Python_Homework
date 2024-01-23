from os import strerror

founded_word = input("Введите слово которое хотите заменить в файле: ")
changed_word = input("Введите слово для замены: ")

try:
    with (open('lab6_lorem.txt', 'rt', encoding='utf-8') as file):
        lines = file.readlines()
        print('\nТекст файла:')
        [print(lines[i][:-1]) if i < len(lines) - 1 else print(lines[i]) for i in range(len(lines))]
        for i, line in enumerate(lines):
            lines[i] = line[:-1]
            words = lines[i].split()
            for j, word in enumerate(words):
                if word[-1] in ".,!?:;'\"" and word[:-1].lower() == founded_word.lower():
                    words[j] = changed_word + words[j][-1]
                if words[j].lower() == founded_word.lower():
                    words[j] = changed_word
            lines[i] = " ".join(words) + '\n'
        print(f'\nСлово \"{founded_word}\" заменено в текстовом файле на слово \"{changed_word}\"')

except Exception as exc:
    print("Cannot open the file:", exc)


try:
    with open('lab6_lorem.txt', 'wt', encoding='utf-8') as file:
        file.writelines(lines)
        print('\nТекст файла после замены:')
        [print(lines[i][:-1]) if i < len(lines) - 1 else print(lines[i]) for i in range(len(lines))]

except IOError as e:
    print('I/O error occurred: ', strerror(e.errno))
