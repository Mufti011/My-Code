#OPERASI KOMPARASI
#setiap hasil dari komparasi adalah boolean
#<,>,<=,>=,==,!=, is not
print("======OPERASI KOMPARASI======")
a = 2
b = 4
#lebih besar dari
print("===Lebih dari===")

hasil = a > 3
print(a,'>',3,'adalah',hasil)
hasil = a > 1
print(a,'>',1,'adalah',hasil)
hasil = b > 3
print(b,'>',3,'adalah',hasil)
hasil = b > 6
print(b,'>',6,'adalah',hasil)

#kurang dari
print("===Kurang dari===")
hasil = a < 3
print(a,'<',3,'adalah',hasil)
hasil = a < 1
print(a,'<',1,'adalah',hasil)
hasil = b < 3
print(b,'<',3,'adalah',hasil)
hasil = b < 6
print(b,'<',6,'adalah',hasil)

#sama dengan
print("===Sama dengan===")
hasil = a == 2
print(a,'==',2,'adalah',hasil)
hasil = a == 1
print(a,'==',1,'adalah',hasil)
hasil = b == 3
print(b,'==',3,'adalah',hasil)
hasil = b == 6
print(b,'==',6,'adalah',hasil)

#!=
print("===!===")
hasil = a != 3
print(a,'!=',3,'adalah',hasil)
hasil = a != 1
print(a,'!=',1,'adalah',hasil)
hasil = b != 3
print(b,'!=',3,'adalah',hasil)
hasil = b != 6
print(b,'!=',4,'adalah',hasil)


print("===Object Identity "is"===")
# "is" sebagai komparsi object identity
x = 5 #ini adalah assigment membuat project
y = 5
print('nilai x =',x,'id =',hex(id(x)))
print('nilai y =',y,'id =',hex(id(y)))
print("id yang sama disimpan dalam memari yang sama")
hasil = x is y
print('x is y =', hasil)

print("===Object Identity "is not"===")
# "is" sebagai komparsi object identity
x = 5 #ini adalah assigment membuat project
y = 5
print('nilai x =',x,'id =',hex(id(x)))
print('nilai y =',y,'id =',hex(id(y)))
print("id yang sama disimpan dalam memari yang sama")
hasil = x is not y
print('x is not y =', hasil)