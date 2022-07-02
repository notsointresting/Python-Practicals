books ={ 1720 : 'Ghost Of Tsushima' , 7201: 'The Witcher 3: Wild Hunt' , 1027 : 'Death Stranding ' , 1717 : 'Death Note', 3000 : 'Multiverse of Madness' }
Issued_book ={}
#Displaying Books
print("-------------------------------LIBRARY---------------------")
for key, value in books.items():
    print(key, ' : ', value)
print()
print("------------------------------------------------------------")
#Issuing book
key = int(input("Enter book id to issue :"))
if key in books:
    Issue_b = books.pop(key)
    Issued_book[key] = Issue_b
    print("Book which is issued :")
    print(Issued_book)
    print("------------------------------------------------------------------")
    print("After issuing book of id " + str(key) + " dictionary is :")
    for key, value in books.items():
        print(key, ' : ', value)
    print("------------------------------------------------------------------")
    #Returning book
    print("After returning book of id " + str(key) + " dictionary is :")

    books.update(Issued_book)
    for key, value in books.items():
        print(key, ' : ', value)
else:
    print("You Entered Wrong Book ID")
