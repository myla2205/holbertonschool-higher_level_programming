#!/usr/bin/python3
def uppercase(str):
    for a in str:
        tmp = ord(a)
        if tmp >= 97 and tmp <= 122:
            pr = chr(tmp - 32)
        else:
            pr = a
        print('{}'.format(pr), end='')
    print()
