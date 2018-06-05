#test_if2.py
a=input("grade:")
a=int(a)
if a>=0 and a<=100:
    if a>90:
        print('excute')
    elif a>80:
        print('good')
    elif a>59:
        print('pass')
    else:
        print('fail')
else:
    print('grade unexpected')