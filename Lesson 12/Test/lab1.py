from os import strerror

try:
    cont = lcnt = 0
    for line in open('text.txt', 'rt', encoding='utf-8'):
        lcnt += 1
        for ch in line:
            print(ch, end="")
            cont += 1
    print('\n\nCharacters in file:', cont)
    print('Lines in file:    ', lcnt)
except  IOError as e:
    print('I/O error occurred: ', strerror(e.errno))
