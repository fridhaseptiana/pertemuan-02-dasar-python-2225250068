# Konstanta
TAHUN_SEKARANG = 2026

# Input data
nama = input("Masukkan nama      : ")
nim = input("Masukkan NIM       : ")
kelas = input("Masukkan kelas     : ")
tahun_lahir = int(input("Masukkan tahun lahir: "))

# Menghitung perkiraan umur
umur = TAHUN_SEKARANG - tahun_lahir

# Menampilkan kartu biodata
print("\n" + "=" * 30)
print("       KARTU BIODATA")
print("=" * 30)
print(f"Nama        : {nama}")
print(f"NIM         : {nim}")
print(f"Kelas       : {kelas}")
print(f"Tahun Lahir : {tahun_lahir}")
print(f"Perkiraan Umur : {umur} tahun")
print("=" * 30)
