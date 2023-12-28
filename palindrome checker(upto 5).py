A=[0]*16
B=[0]*16
k=4
print("You can check upto 5 words to see if they are palindromes or not.")
while k>=0:    
    A=input("enter word: ")
    B=A[::-1]
    if A==B:
        print("The word is a palindrome")
    else:
        print("The word is not a palindrome")
    k-=1


