print("=====OPERASI LOGIKA / BOOLEAN (not, or, and, xor)=====")
#not, or, and, xcor
#not
print("===NOT===")
a = True
c = not a
print('data a =',a)
print('------ NOT')
print('data c =', c)

#or
print("===OR===")
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)

a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

a = False
b = True
c = a or b
print(a,'OR',b,'=',c)

#and
print("===AND===")
a = True
b = False
c = a and b
print(a,'AND',b,'=',c)

a = True
b = True
c = a and b
print(a,'AND',b,'=',c)

a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

a = False
b = True
c = a and b
print(a,'AND',b,'=',c)

#XOR
print("===XOR===")
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)