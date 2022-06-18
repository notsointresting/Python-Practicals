# Find Perfect Number
N=int(input("Enter a number---> "))
C=0
for i in range(1,N):
    if N%i==0:
        C+=i
if C==N:
    print(N,"is a perfect number!")
else:
    print(N,"is not a perfect number!")
