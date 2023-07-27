#variabel tempat penyimpan variabel
a = 10
x = 3
print("Nilai a =",a)

#Tipe data
#1. Tipe data angka/ integer
data_integer = 1
print(type(data_integer))
print("data :", data_integer,", bertipe :", type(data_integer))
#2. Tipe data Float itu angka dengan koma
data_float = 1.5
print(type(data_float))
print("data :", data_float,", bertipe :", type(data_float))
#3.String = kumpulan karakter
data_string = "NASYA"
print(type(data_string))
print("data :", data_string,", bertipe :", type(data_string))
#4.Tipe data : biner True/False (Boolean)
data_bool = "True"
print(type(data_bool))
print("data :", data_bool,", bertipe :", type(data_bool))

#Tipe data khusus
#bilanhan kompleks
data_kompleks = complex(5,6)
print(type(data_kompleks))
print("data :", data_kompleks,", bertipe :", type(data_kompleks))

#Tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print(type(data_c_double))
print("data :", data_c_double,", bertipe :", type(data_c_double))


#CASTING >>> Merubah tipe data
print("====Integer====")
data_int = 9
#ubah data int ke float
data_floatt = float(data_int)
data_floatt = str(data_int)
data_floatt = bool(data_int)
print("data :", data_floatt,", bertipe :", type(data_floatt))
print("====FLOAT====")
data_float = 9.8
#ubah data int ke integer
data_intg = str(data_float)
print("data :", data_intg,", bertipe :", type(data_intg))

#Mengambil data dari user/Konsumer
#ini pasti string tipenya. knp casting penting
data = input("Masukan data : ")
print("data = ",data,",type =",type(data))

angka = float(input("Masukan angka :"))
angka = str(input("Masukan angka :"))
print("data = ",angka,",type =",type(angka))

#ambil data boolean
biner=bool(int(input("Masukan data boolean :")))
print("data = ",biner,",type =",type(biner))


#OPERASI BILANGAN
a = 3
b = 7
print("=====Pertambahan=====")
hasil = a + b
print(a,'+',b,'=',hasil)
print("=====Pembagian=====")
hasil = a / b
print(a,'/',b,'=',hasil)
print("=====Perkurangan=====")
hasil = a - b
print(a,'-',b,'=',hasil)
print("=====Perkalian=====")
hasil = a * b
print(a,'*',b,'=',hasil)
