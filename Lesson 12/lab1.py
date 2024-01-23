from os import strerror

try:
    t1 = open('new_text1.txt', 'rt', encoding='utf-8')
    t2 = open('new_text2.txt', 'rt', encoding='utf-8')
    text1 = t1.readlines()
    text2 = t2.readlines()
    if len(text1) < len(text2):
        text1, text2 = text2, text1
    for i in range(len(text1)):
        if i < len(text2)-1 and text1[i] != text2[i]:
            print(f'Строки {i + 1} не равны:')
            print(f'\"{text1[i][:-1]}\" не равен \"{text2[i][:-1]}\"\n')
        if i >= len(text2)-1:
            print(f'В одном файле меньше строк чем в другом: \n \"{text1[i][:-1]}\"\n')
    t1.close()
    t2.close()
except IOError as e:
    print('I/O error occurred: ', strerror(e.errno))
