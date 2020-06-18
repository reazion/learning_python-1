import random
a,c = input("Выберите тип игры. '6 45', '5 36', '4 20': ").split()
def loter():
    b=[]
    d=[]
    e=0
    for i in range(1,int(c)+1):
        b.append(i)
    while len(d)<int(a):
        e=random.choice(b)
        if e not in d:
            d.append(e)
    print(d)
if a=="4" and c=="20":
    loter()
    loter()
elif a=="5" and c=="36":
    loter()
    a=1
    c=4
    loter()
else:
    loter()
input()
