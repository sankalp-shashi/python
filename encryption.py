A=[0]*20
B=[0]*20
C=[0]*20
D=[0]*20
a=10
print("Program closes after entering password 10 times")
#while a>=0:
A=input("enter password: ")
for i in range(0,len(A)):
    B[i] = ord(A[i])
for j in range(0,len(A)):
    if int(B[j])%2==0:
         C[j] = int(B[j]/2)
         print("ord(C[j])=",B[j]," even",C[j])
    else:
        C[j] = int((B[j]+1)/2)
        print("ord(C[j])=",B[j]," odd",C[j])
for k in range(0,len(A)):
    D[k] = chr(C[k])
print("the encrypted password is: ",*D)
 #   a-=1

    
