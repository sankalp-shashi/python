import math
x=0
n=0
m=0
print("This program prints prime numbers in a given range, exluding the limits.")
m=int(input("Enter lower limit: "))
n=int(input("Enter upper limit: "))
print()
x=m+1
if n>m:
    while x<n and x>m:
        y=2
        while y<x and x<n:
            if x%y==0:
                x+=1
                y=2
            else:
                y+=1      
        if x==n:
            break
        else:
            print(x)
            x+=1
else:
    print("Error, upper limit is not greater than lower limit.")
p=0
p=input("Hit enter to close")

