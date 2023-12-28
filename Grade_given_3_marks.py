a=0
b=0
c=0
a=int(input("enter first subject marks out of 100"))
b=int(input("enter second subject marks out of 100"))
c=int(input("enter third subject marks out of 100"))
while a>100 or b>100 or c>100:
    if a>100 or b>100 or c>100:
        print("enter values less than 100")
    a=int(input("enter first subject marks out of 100"))
    b=int(input("enter second subject marks out of 100"))
    c=int(input("enter third subject marks out of 100"))
T=a+b+c
P=T//3
if P>=90:
    print("Your grade is A+")
elif P>=60:
    print("Your grade is A")
elif P>=50:
    print("Your grade is B+")
elif P>=40:
    print("Your grade is B")
else: print("Your grade is C")


