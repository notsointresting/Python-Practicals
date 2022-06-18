Number = int(input("Enter the Number to Check Disarium Number = "))
length = len(str(Number))
Temp = Number
Sum = 0
rem = 0
while Temp > 0:
    rem = Temp % 10
    Sum = Sum + int(rem**length)
    Temp = Temp // 10
    length = length - 1
if Sum == Number:
    print(Number,"\nis a Disarium Number.")
else:
    print(Number,"is Not a Disarium Number.")
