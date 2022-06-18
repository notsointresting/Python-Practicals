#Program to convert Kilometers to Miles and vica versa

print("<--------------------Distance Converter-------------------->")
print("Press 1 to convert Kilometers to Miles")
print("Press 2 to convert Miles to Kilometers\n")
c=int(input("Enter Your Choice---> "))
while c!=0:
    if c==1:
        print("\n<----------Kilometers to Miles---------->")
        K = float(input("Enter Distance in Kilometers---> "))
        M = K * 0.621371
        print("{0} Km ---> {1} Miles".format(K,M))
        print("Press 0 to exit\n")
        c=int(input("Enter Your Choice---> "))
        
    elif c==2:
        print("<----------Miles to Kilometers---------->")
        M = float(input("Enter Distance in Miles---> "))
        K = M/0.621371
        print("{0} Miles ---> {1} Km".format(M,K))
        print("Press 0 to exit\n")
        c=int(input("Enter Your Choice---> "))
        
