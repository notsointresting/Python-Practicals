def Happy(num):
    rem=s=0
    while num > 0:
        rem = num%10
        s = s + (rem*rem)
        num = num//10
    return s
num = int(input())
result = num
while(result!=1 and result!=4):
    result = Happy(num)
if result==1:
    print("HAPPY NUMBER")
elif result==4:
    print("NOT HAPPY NUMBER")
