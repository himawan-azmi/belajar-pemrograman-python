# Deklarasi Variabel
nama = "Himawan"
hobi = 'main game'
umur = 25
laki = True

# notasi = (sama dengan) sebagai operator assignment digunakan untuk operasi penugasan
# nilai string dapat dituliskan dengan literal " ataupun '

# Tampilkan nilai variabel ke layar
print("---Biodata---")
print("Nama: %s" % (nama))
print("Hobi: %s, Umur: %d, Laki: %r" %(hobi, umur, laki))
# karakter %s akan di-replace dengan nilai variabel, dan sebagai penanda bahwa data
# yang akan me-replace bertipe string.
# karakter %d untuk data bertipe numerik integer
# karakter %r untuk data bertipe bool (boolean)

# Nama variabel dianjurkan untuk ditulis menggunakan snake_case