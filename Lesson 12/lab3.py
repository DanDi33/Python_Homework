try:
    with open('lab3.txt', 'rt') as file:
        text = file.readlines()
        print('Текст в файле до удаления:')
        [print(text[i][:-1]) if i < len(text) - 1 else print(text[i]) for i in range(len(text))]
        text.pop()
    with open('lab3_res.txt', 'w') as file:
        print('\nПосле удаления последней строки:')
        for line in text:
            file.write(line)
            print(line[:-1])
except:
    print("Error")
