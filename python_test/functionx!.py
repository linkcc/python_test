#functionx!.py

def factoral(x):
    sum = 1
    for i in range(2,x+1):
        sum *= i
    return sum

#print(factoral(6))
SUM=0
a=int(input("x:"))
for q in range(1,a+1):
    if q == a:
        print(q,'!',end=' = ')
    else:
        print(q,'!',end=' + ')
    SUM += factoral(q)

print(SUM)