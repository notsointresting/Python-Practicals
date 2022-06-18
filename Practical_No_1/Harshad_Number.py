num = int(input("Enter To check Harshad's Number or not:- "))   
rem = Sum = 0    
n = num   
while(num > 0):    
    rem = num%10;    
    Sum = Sum + rem;    
    num = num//10;     
if(n%Sum == 0):    
    print(n," is a harshad number") 
else:    
    print(n," is not a harshad number")
