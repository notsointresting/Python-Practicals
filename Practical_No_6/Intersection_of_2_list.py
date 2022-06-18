L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
c=[]
for i in L1:
    for j in L2:
        if i in L1 and j in L2 and i==j:
            c.append(i)
print(set(c))
