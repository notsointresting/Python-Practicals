print("Disarium Numbers Between 1 to 100 are:-")
for i in range(1,101):
    rem=s=0
    L=len(str(i))
    n=i
    while i>0:
        rem=i%10
        s+=int(rem**L)
        i=i//10
        L-=1
    if s==n:
        print(s)
