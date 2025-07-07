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
# Contoh naming convention variable
pesan = 'Halo, Selamat Pagi'
nilai_ujian = 99.0

print(pesan)
print(nilai_ujian)

# Deklarasi variabel beserta tipe data
nama1: str = "Himawan"
hobi1: str = "jajan"
usia: int = 18
laki1: bool = True
nilai_ujian1: float = 100.0

print("Nama: %s" % (nama1))
print("Hobi: %s" % (hobi1))
print("Usia: %d" % (usia))
print("Laki: %r" % (laki1))
print("Nilai Ujian: %f" % (nilai_ujian1))
# Karakter %f untuk data bertipe numerik float

# Deklarasi banyak variabel sebaris
nilai1, nilai2, nilai3, nilai4 = 24, 25, 26, 27
nilai_rata_rata = (nilai1 + nilai2 + nilai3 + nilai4) / 4

print("Rata-rata nilai: %f" % (nilai_rata_rata))