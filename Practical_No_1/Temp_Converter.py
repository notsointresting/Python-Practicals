#Program to convert celsius to fahrenheit and vica versa

print("<--------------------Temperature Converter-------------------->")
print("Press 1 to convert Celsius to Farenheit")
print("Press 2 to convert Farenheit to Celsius\n")
c=int(input("Enter Your Choice---> "))
while c!=0:
    if c==1:
        print("\n<----------Celsius to Farenheit---------->")
        celsius = float(input("Enter Temperature in Celsius---> "))
        F = (celsius * 1.8) + 32
        print("{0} C ---> {1} F".format(celsius,F))
        print("Press 0 to exit\n")
        c=int(input("Enter Your Choice---> "))
        
    elif c==2:
        print("<----------Farenheit to Celsius---------->")
        F = float(input("Enter Temperature in Farenheit---> "))
        C = (F - 32) * 5/9
        print("{0} F ---> {1} C".format(F,C))
        print("Press 0 to exit\n")
        c=int(input("Enter Your Choice---> "))
        
