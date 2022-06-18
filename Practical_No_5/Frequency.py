#Extract elements with frequency greater than K
A=list(map(int,input("ENTER ELEMENTS---> ").split()))
K=3
res=[]
for i in A:
    F = A.count(i)
    if F > K:
        res.append(i)
print("Frequency of Element greater then {0} ---> {1}".format(K,set(res)))
