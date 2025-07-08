# Tipe data numerik
# Integer (int) untuk bilangan bulat
number_1 = 1000024
# Float (float) untuk bilangan desimal atau floating point
number_2 = 3.14
# Complex (complex) untuk nilai berisi kombinasi bilangan real dan imaginer
number_3 = 120+3j

print(number_1)
print(number_2)
print(number_3)

# Tipe data String / str
# Ditandai dengan tanda awalan dan akhiran "" atau ''
# Contoh petik dua ""
# Sebaris
string_1 = "halo pyhton"

# Multi-baris
string_2 = """Selamat
Belajar
Python"""

print(string_1)
print(string_2)

# Contoh petik '
# Sebaris
string_3 = 'for the lord!'

# Multi-baris
string_4 = '''
Sesok
preiii
'''

print(string_3)
print(string_4)

# JJika ada baris baru (atau newline) di bagian awal penulisan ''' atau """ 
# maka baris baru tersebut merupakan bagian dari string. 
# Jika ingin meng-exclude-nya bisa menggunakan """\ atau '''\
string_5 = '''\
sesok
preii
'''

# Tipe data bool (boolean)
# Literal untuk tipe data ini adalah True = benar, dan False = salah.
bool_1 = True
bool_2 = False

print(bool_1)
print(bool_2)

# Tipe data None untuk merepresentasikan nilai kosong (null atau nil)
# Pengecekan nilai kosong digunakan
data = "hello"
print(data)

data = None
print(data)

data = "python"
print(data)

# Tipe data list
# Digunakan untuk menampung nilai kolektif yang disimpan secara urut yang isinya
# bisa berupa banyak varian tipe data (tidak sejenis)
# Ditulis dalam kurung siku [] dan dipisahkan oleh tanda koma ,

# List int
list_1 = [2, 4, 8]

# List string
list_2 = ["John", "Alice", "Bob"]

# List mix
list_3 = [24, False, "Sesok Preii"]

print(list_1)
print(list_2)
print(list_3)

# Mengakses element list dengan notasi list[index_number]
# index_number dimulai dari 0
print(list_1[2])

# Tipe data tuple
# Tipe data kolektif mirip list, namun tidak dapat diubah nilainya (immutable)
# Tuple ditulis dalam tanda kurung biasa ()

# Tuple int
tuple_1 = (1, 2, 3)

# Tuple str
tuple_2 = ("Doe", "Toor")

# Tuple mix
tuple_3 = (9, True, "Sesok Preii")

print(tuple_1)
print(tuple_2)
print(tuple_3)

# Mengakses element tuple dengan notasi tuple[index_number]
print(tuple_1[2])

# Tipe data dictionary (dict)
# Untuk menyimpan data kolektif terstruktur berbentuk key value
profile_1 = {
    "name": "John",
    "is_male":True,
    "age": 45,
    "hobbies": ["eating", "learning"]
}

print(profile_1)

# Pengaksesan property dict menggunakan notasi dict[property_name]
print("name: %s" % (profile_1["name"]))
print("hobbies: %s" % (profile_1["hobbies"]))

# Tipe data set
# Cara lain menyimpan data kolektif
# Kelemahan: tidak bisa menyimpan informasi urutan data, elemen data yang sudah
# dideklarasikan tidak bisa diubah nilainya (tapi bisa dihapus), tidak bisa diakses
# menggunakan index (tapi bisa menggunakan perulangan)
set_1 = {"pineapple", "spaghetti"}
print(set_1)