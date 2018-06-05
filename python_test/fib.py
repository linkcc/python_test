#fib.py
def fib(max):
    a,b,c = 0,0,1
    while a < max:
        yield c
        b,c = c,b+c
        a = a+1

a=int(input())
for n in fib(a):
    print n
