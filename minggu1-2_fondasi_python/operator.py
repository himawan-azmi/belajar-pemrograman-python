# Operator aritmatika
# + -> operasi tambah
num = 2 + 2
print("Hasil penjumlahan 2 + 2 = ", num)

# unary + -> penanda nilai positif
num = +2
print("Hasil unary +2 = ",num)

# - -> operasi pengurangan
num = 3 - 2
print("Hasil pengurangan 3 - 2= ", num)

# unary - -> penanda nilai negatif
num = -2
print("Hasil unary -2 = ", num)

# * -> operasi perkalian
num = 3 * 3
print("Hasil perkalian 3 * 3 = ", num)

# / -> operasi pembagian
num = 8 / 2
print("Hasil pembagian 8 / 2 = ", num)

# // -> operasi bagi dengan hasil dibulatkan ke bawah
num = 10 // 3
print("Hasil pembagian 10 // 3 = ", num, "(dibulatkan ke bawah)")

# & -> operasi modulo (pencarian sisa hasil bagi)
num = 7 % 2
print("Hasil sisa bagi 7 % 2 = ", num)

# ** -> operasi pangkat
num = 3 ** 2
print("Hasil dar 3 pangkat 2 = ", num)

# Operator assignment (=) digunakan untuk penentuan nilai sekaligus deklarasi variabel
# deklarasi variabel
num_1 = 12
num_2 = 1
# deklarasi variabel dengan isi nilai hasil oeprasi aritmatika num_1 + num_2
num_3 = num_1 + num_2
print("Operator assignment, num_1 (12) + num_2 (1) = ", num_3)

# Operator perbandingan dengan tipe data boolean (bool) yang menghasilkan nilai kebenaran
# Dua nilai kebenaran yang ada yaitu True (benar) atau False (salah)
# operator == (apakah kiri sama dengan kanan)
res = 4 == 5
print("Apakah kiri (4) sama dengan kanan (5) 4 == 5? = ", res)
# operator != (apakah kiri tidak sama dengan kanan)
res = 4 != 5
print("Apakah kiri (4) tidak sama dengan kanan (5) -> 4 != 5? = ", res)

# Operator logika memiliki 3 jenis yaitu and, or dan not
# Operator AND
res = (4 == 5) and (2 != 3)
print("Operator AND, (4 == 5) and (2 != 3) = ", res)

# Operator OR
res = (4 == 5) or (2 != 3)
print("Operator OR, (4 == 5) or (2 != 3) ? = ", res)

# Operator Negasi atau NOT
res = not (2 == 3)
print("Operator NOT, not (2 == 3) = ", res)

# Operator bitwise
# bitwise AND, &
# x & y = 0 (0000 0000)

# biwise OR, |
# x | y = 14 (0000 1110)

# biwtise NOT, ~
# ~x = -11 (1111 0000)

# bitwise XOR, ^
# x ^ y = 14 (0000 1110)

# bitwise right shift, >>
# x >> 2 = 2 (0000 0010)

# bitwise left shift, <<
# x << 2 = 40 (0010 1000)

# Operator indetity (is)
# Memiliki kemiripan operator logika ==
# Yang dibandingkan bukan nilai, tetapi identitas atau ID-nya
num_1 = 100001
num_2 = 100001

res = num_1 is num_2
print("num_1 is num_2 =", res)
print("id(num_1): %s, id(num_2): %s" % (id(num_1), id(num_2)))
