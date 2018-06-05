#print_test.py
import re

L = re.split(',| |，|  ', input('请输入，用逗号或空格隔开：'))
l=L.copy()

for i in range(len(L)):
    L[i] = len(L[i])
L.sort()

#print(L[-1])

for i in range(len(l)):
    print(l[i].rjust(L[-1]))

for i in range(len(l)):
    print(l[i].center(L[-1]))