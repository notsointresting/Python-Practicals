#Count unique values inside the list 

A=list(map(int,input("ENTER ELEMENTS:- ").split()))
B=[]
for i in A:
    if A.count(i)==1:
        B.append(i)
if len(B)==0:
    print("No Unique Element Found")
else:
    print("Unique Elements Are---> ",B)
