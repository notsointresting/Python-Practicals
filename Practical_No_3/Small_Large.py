#Print Largest and smallest element in array
print("1st Method")
L=[1,2,33,11,42,422]
print("Largest Element in List---> ",max(L))
print("Smallest Element in List---> ",min(L))
print("2nd Method")
L=sorted(L)
print("Largest Element in List---> ",L[-1])
print("Smallest Element in List---> ",L[0])
