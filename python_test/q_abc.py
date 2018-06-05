#ax^2+bx+c=0
import math
def qua(a,b,c):
    s=b*b-4*a*c
    if a==0:
        x=-c/b
        return x
    elif s<0:
        return 'no answer'
    else:
        x=(-b+math.sqrt(s))/(2*a)
        y=(-b-math.sqrt(s))/(2*a)
        return x,y