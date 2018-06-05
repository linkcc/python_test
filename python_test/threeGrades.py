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

#2
#threeGrades.py
import math;
a=float(input('第一个学生成绩：'))
b=float(input('第二个学生成绩：'))
c=float(input('第三个学生成绩：'))
print('最大成绩：',max(a,b,c))
print('最小成绩：',min(a,b,c))
print('平均成绩：',round((a+b+c)/3),1)
