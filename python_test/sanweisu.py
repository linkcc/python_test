#sanweisu.py
i=0
L = [m+n+q for m in '1234' for n in '1234' for q in '1234']
for x in L:
    a=int(int(x)%10)
    b=int(int(x)/10%10)
    c=int(int(x)/100%10)
    if a!=b and a!=c and b!=c:
        i += 1
        if i%4:
            print(a,b,c,end = '|')
        else:
            print(a,b,c)