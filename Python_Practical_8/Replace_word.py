d={}
N=3
for i in range(3):
    name=input("Enter Name: ")
    num=input("Enter Number: ")
    d[name]=num

print(d)
Name=input("Enter Name of that Number to be replace: ")
if Name in d:
    d[Name]=input("Enter New Number---> ")
print(d)    
