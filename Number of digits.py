n=0

print("This program finds the number of digits of any number.")
print()
n=int(input("Enter number: "))
q=1
z=1
while n//z>0:
    z=10**q
    q=q+1

print()
print(f"The number has {q-1} digits.")
input()
