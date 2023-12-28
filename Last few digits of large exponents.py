a=0
b=0
c=0
x=0
y=0
z=0
while a>=0:
    a=int(input("How many digits do you want? "))
    b=int(input("Enter the base "))
    c=int(input("Enter the exponent "))
    z=int(b**c)
    y=int(10**a)
    x=int(z%y)
    print(x)
p=0
p=input("Hit enter to close")
