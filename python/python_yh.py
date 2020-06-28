#!/usr/bin/python3


def triangles():
    L1 = [1]
    while True:
        L2 = L1[:]
        yield L2
        for i in range(1, len(L1)):
            L1[i] = L2[i] + L2[i-1]

        L1.append(1)


n = 0
ret = []

for L in triangles():
    ret.append(L)
    n = n+1
    if(n == 10):
        break

print(ret)
