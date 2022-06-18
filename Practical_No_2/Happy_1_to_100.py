def Happy(num):
    rem=s=0
    while num > 0:
        rem = num%10
        s = s + (rem*rem)
        num = num//10
    return s
print("Happy Numbers between 1 to 100 are:-")
for i in range(1,101):
    result = i
    while result !=1 and result !=4:
        result = Happy(result)
        if (result ==1):
            print(i)
