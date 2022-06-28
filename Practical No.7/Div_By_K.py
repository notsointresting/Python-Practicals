my_list = [(45, 90, 135), (71, 92, 26), (2, 67, 98)]

print("The list is : ")
print(my_list)

K = 45
print("The value of K has been initialized to ")
print(K)
my_result = [sub for sub in my_list if all(ele % K == 0 for ele in sub)]

print("Elements divisible by K are : " + str(my_result))
