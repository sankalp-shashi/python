def P(r,g,b):
    if r==0:
        return 1
    if g==0 or b==0:
        return 0
    return (r*(P(r-1,g,b))+g*(P(r,g-1,b))+b*P(r,g,b-1))/(r+g+b)

r=int(input("Enter r: "))
g=int(input("Enter g: "))
b=int(input("Enter b: "))
print(P(r,g,b))
