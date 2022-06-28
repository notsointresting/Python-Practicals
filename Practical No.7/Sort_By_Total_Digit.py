def count(row):
   return sum([len(str(element)) for element in row])

tup = [(32, 14, 65, 723), (13, 26), (12345,), (137, 234, 314)]

print("The tuple is :")
print(tup)

tup.sort(key = count)

print("The result is :")
print(tup)
