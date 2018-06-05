#zifu.py
a=input()

# if len(a)%2:
#     t=int(len(a)/2)
#     print(a[t])
# else:
#     print('|')

re = a[int(len(a)/2)] if len(a)%2 else '|'
print(re)

a=input()
if a:
    print(ord(a[0]))

a=int(input())
print(chr(a))