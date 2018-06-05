#test_AifBelseC.py
s=input()
s=int(s)
if s>=0:
    s=s*0.8 if s>=500 else s
    print(s)
else:
    print("s unexpected")