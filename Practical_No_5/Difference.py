#write a python program to compute the diff between 2 list.
A=list(map(int,input("Enter Elements for Set A---> ").split()))
B=list(map(int,input("Enter Elements for Set B---> ").split()))
print("Difference Between two lists---> ",list(set(A)-set(B)))
