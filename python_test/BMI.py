#1
#BMI.py
h=float(input('height:'))
w=int(input('weight:'))
bmi = w/(h*h)
print('bmi:',bmi)
if bmi>0 and bmi <18.5:
    print('too light')
elif bmi >=18.5 and bmi <=24:
    print('normal')
elif bmi >=24:
    print('abnormal')
else:
    print('bmi error')