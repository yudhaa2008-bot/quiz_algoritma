import sys

print("======================================")
print(" PROGRAM KELULUSAN UJIAN MATEMATIKA ")
print("======================================")

# Input nama mahasiswa
nama = input("Masukkan nama mahasiswa: ")

# Menentukan target nilai
if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    print("Nama mahasiswa tidak terdaftar!")
    sys.exit()

print("\nNama mahasiswa :", nama)
print("Target nilai   :", target)

# Inisialisasi
percobaan = 1
lulus = False

# Perulangan maksimal 3 kali
while percobaan <= 3:
    nilai = int(input(f"Masukkan nilai ujian ke-{percobaan}: "))

    # Pengecekan nilai
    if nilai >= target:
        lulus = True
        break
    else:
        print("Nilai belum mencapai target.")

        if percobaan < 3:
            print("Silakan mengikuti remedial.\n")

    percobaan += 1

# Menampilkan hasil akhir
print("\n======================================")
print("             HASIL UJIAN             ")
print("======================================")

if lulus:
    print(f"{nama} berhasil lulus setelah {percobaan} kali percobaan!")
else:
    print(f"{nama} tidak lulus setelah 3 kali percobaan!")

print("======================================")