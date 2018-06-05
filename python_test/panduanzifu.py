#panduanzifu.py
a=input()
print('is int:',a.isdigit())
try:
    b=float(a)
except:
    print('is float: false')
else:
    print('is float:',isinstance(b,float))
print(a.count(' ',0,len(a)))
