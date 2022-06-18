#To check if the list contains 3 consecutive common numbers
L=list(map(int,input("Enter Elements---> ").split()))
c=[]
size=len(L)
for i in range(size-2):
    if L[i]==L[i+1] and L[i+1]==L[i+2]:
        c.append(L[i])
print("3 Consecutive Comman Numbers---> ",str(c))
