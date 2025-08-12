# Deklarasi konstanta dibantu dengan tipe class typing.Final
from typing import Final

PI: Final = 3.14
print("pi: %f" % (PI))

# Module import digunakan untuk meng-import sesuatu
# Keyword from digunakan untuk menentukan dari module mana sesuatu akan di-import

# Tipe Final digunakan untuk menandai suatu variabel sebagai konstanta (nilainya tetap)
# Tipe data konstanta dengan final dapat dituliskan secara eksplisit, atau
# tidak ditentukan dan diidentifikasi oleh interpreter berdasarkan tipe data nilainya

# Tipe data tidak ditentukan secara eksplisit
PI1: Final = 3.14

# Tipe data ditentukan secara eksplisit
TOTAL_MONTH: Final[int] = 12

print("pi: %f" % (PI1))
print("Jumlah Bulan: %d" % (TOTAL_MONTH))

# Naming convention konstanta, nama konstanta harus dituliskan dalam huruf besar (UPPER_CASE)