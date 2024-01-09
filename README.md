## PROJECT UAS
| _Variable_ | Isi |
| -------- | --- |
| _Nama_ | Ananda Rahmadani  |
| _NIM_ | 312310461 |
| _Kelas_ | TI.23.A5 |
| _Mata Kuliah | Bahasa Pemrograman |
### Buatlah program kasir di sebuah kantin, dengan kondisi berikut:
* List opsi pilihan makanan/minuman dan aksi, bisa menggunakan format dictionary
* Program harus meminta input pilihan makanan dari pengguna.
* Program harus menghitung total harga makanan yang dipesan.
* Program harus menampilkan struk pembelian.
### Definisi daftar opsi pilihan makanan/minuman dan harga
Bagian ini mendefinisikan daftar opsi pilihan makanan/minuman dan harga masing-masing. Daftar ini disimpan dalam sebuah dictionary Python dengan key sebagai nama menu dan value sebagai harga.

```python
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
```
### Inisialisasi list pesanan di luar loop while
Bagian ini menginisialisasi list pesanan di luar loop while. List ini akan digunakan untuk menyimpan daftar menu yang dipilih oleh pengguna.
```python
pesanan = []
```
### Mulai transaksi
Bagian ini mencetak pesan selamat datang dan memulai transaksi.
```python
print("Selamat datang di Warung Nusantara!")
```
### Permintaan input pilihan makanan dari pengguna
Bagian ini menampilkan daftar menu dan meminta input pilihan makanan dari pengguna. Loop while akan terus berjalan selama pengguna tidak memasukkan pilihan "q".
```python
while True: 
    print("Pilih menu makanan/minuman yang ingin Anda pesan:")
    for key, value in menu.items():
        print(f"{key}: Rp{value}")
```
### Jika pilihan pengguna tidak valid, maka minta input ulang
Bagian ini memeriksa apakah pilihan pengguna ada dalam daftar menu. Jika tidak, maka pengguna akan diminta untuk memasukkan pilihan ulang.
```python
if pilihan == "q":
        break
```
### Menambahkan menu yang dipilih ke dalam list pesanan
Bagian ini menambahkan menu yang dipilih oleh pengguna ke dalam list pesanan.
```python
pesanan.append(pilihan)
```
### Hitung total harga pesanan
Bagian ini menghitung total harga pesanan dengan menggunakan fungsi sum(). Fungsi ini akan menjumlahkan harga dari semua menu yang ada dalam list pesanan.
```python
total_harga = sum(menu[menu_item] for menu_item in pesanan)
```
### Tampilkan struk pembelian
Bagian ini menampilkan struk pembelian dengan menggunakan format tabel. Struk pembelian akan menampilkan nomor menu, nama menu, dan harga masing-masing menu.
```python
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
```
# TERIMA KASIH
