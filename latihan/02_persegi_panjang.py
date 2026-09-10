# Input panjang dan lebar
panjang = float(input("Masukkan panjang (cm): "))
lebar = float(input("Masukkan lebar (cm): "))

# Menghitung luas dan keliling
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

# Menampilkan hasil
print("\n=== HASIL PERHITUNGAN ===")
print(f"Panjang  : {panjang:.2f} cm")
print(f"Lebar    : {lebar:.2f} cm")
print(f"Luas     : {luas:.2f} cm²")
print(f"Keliling : {keliling:.2f} cm")
