print("INSTRUCTIONS")
print("The Array is a b c d")
print("Enter 0 to append a letter.")
print("Enter 1 to remove a letter.")
print("Enter 2 to get the index of a letter.")
print("Enter 3 to see the array at any point.")
print("Enter any other number to exit")
Array=['a','b','c','d']
x=0
while x<4:
    x=int(input("Enter number: "))
    if x==0:
        y=input("type the letter you want to append ")
        Array.append(y)
    elif x==1:
        y=input("type the letter you want to remove ")
        for z in Array:
            if z==y:
                Array.remove(y)
        print("Remember to only enter a letter already in the Array")
    elif x==2:
        
        y=input("type the letter you want the index of ")
        for z in Array:
            if z==y:
                print(Array.index(z))
        print("Remember to only enter a letter already in the Array")
    elif x==3:
        print(*Array)

p=0
p=input("Hit enter to close")
