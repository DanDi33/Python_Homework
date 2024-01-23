text = 'This is 1st line\nThis is 2nd line\nThis is 3rd line\n'
text1 = 'This is 4st line\nThis is 5nd line\nThis is 6rd line\n'
with open('foo.txt', 'w') as fp:
    fp.write(text)
    fp.write(text1)
with open('foo.txt', 'r', encoding='utf-8') as fp:
    print(fp.read())
