from os import strerror
try:
    fo = open('newtext.txt','wt')
    for i in range(10):
        a = 'line #'+str(i+1)+'\n'
        # for ch in a:
        #     fo.write(ch)
        fo.write(a)
    fo.close()
except IOError as e:
    print('I/O error occurred: ', strerror(e.errno))
