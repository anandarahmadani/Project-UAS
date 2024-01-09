# Definisikan daftar opsi pilihan makanan/minuman dan hargave
menu = {
    "Nasi Goreng Gila": 200000,
    "Bakmi Jamur": 15000,
    "Soto Ayam": 12000,
    "Kwetiaw Goreng": 14000,
    "Cireng": 7000,
    "Es Teh Manis": 4000,
    "Es Jeruk": 5000,
    "Le Mineral": 3000,
    "Teh Tarik Jelly": 15000,
}

# Inisialisasi list pesanan di luar loop while
pesanan = []

# Mulai transaksi
print("Selamat datang di Warung Nusantara!")

# Permintaan input pilihan makanan dari pengguna
while True: 
print("Pilih menu makanan/minuman yang ingin Anda pesan:")
for key, value in menu.items():
        print(f"{key}: Rp{value}")

    pilihan = input("Masukkan pilihan Anda (tekan q untuk selesai): ")

    # Jika pilihan pengguna adalah q, maka hentikan transaksi
    if pilihan == "q":
        break

    # Jika pilihan pengguna tidak valid, maka minta input ulang
    if pilihan not in menu:
        print("Pilihan Anda tidak valid. Silakan pilih kembali.")
        continue

    # Menambahkan menu yang dipilih ke dalam list pesanan
    pesanan.append(pilihan)

# Hitung total harga pesanan
total_harga = sum(menu[menu_item] for menu_item in pesanan)

# Tampilkan struk pembelian
print("--------------------------------------------------")
print("Struk Pembelian Warung Nusantara")
print("--------------------------------------------------")
print("No. | Menu | Harga")
print("----|------|------")
for i, menu_item in enumerate(pesanan):
    print(f"{i + 1} | {menu_item} | Rp{menu[menu_item]}")
print("--------------------------------------------------")
print(f"Total Harga: Rp{total_harga}")
print("--------------------------------------------------")