# MEMBUAT VARIABEL TOKO BAHAN PANGAN
beras = 15000
sayuran = 5000
bumbu = 2000
ikan = 5000
telur = 3000
total_belanja = 0

# CETAK MENU UTAMA TOKO BAHAN PANGAN
print("==================================")
print("         TOKO BAHAN PANGAN")
print("==================================")
print("Berikut tersedia beberapa barang")
print("Gunakan nomor untuk memilih")
print("1. Beras - Rp %d"%(beras))
print("2. Sayuran - Rp %d"%(sayuran))
print("3. Bumbu - Rp %d"%(bumbu))
print("4. Ikan - Rp %d"%(ikan))
print("5. Telur - Rp %d"%(telur))
print("----------------------------------")
nama_pembeli = input("Masukan nama pembeli : ")
uang  = int(input("Masukan jumlah uang: "))
print("----------------------------------")

# PROGRAM TOKO BAHAN PANGAN
while(uang>total_belanja) :
    
    # MEMBUAT VARIABEL PERHITUNGAN
    barang   = ""
    harga_barang  = 0
    
    nomor  = int(input("Beli barang nomor ke : "))
    jumlah_barang = int(input("Tentukan jumlahnya : "))
    
    if(nomor == 1) :
        barang    = "Beras"
        harga_barang = beras*jumlah_barang
        total_belanja += beras*jumlah_barang
    elif(nomor == 2) :
        barang = "Sayuran"
        harga_barang = sayuran*jumlah_barang
        total_belanja += sayuran*jumlah_barang
    elif(nomor == 3) :
        barang = "Bumbu"
        harga_barang = bumbu*jumlah_barang
        total_belanja += bumbu*jumlah_barang
    elif(nomor == 4) :
        barang = "Ikan"
        harga_barang = ikan*jumlah_barang
        total_belanja += ikan*jumlah_barang
    elif(nomor == 5) :
        barang = "Telur"
        harga_barang = telur*jumlah_barang
        total_belanja += telur*jumlah_barang
    else :
        print("Nomor tidak ada: - ")
    
    
    # CEK KONDISI SISA UANG DAN TOAL BELANJA
    if(uang<total_belanja) :
        print("Uang tidak cukup : - ")
        total_belanja = total_belanja - harga_barang
        belanja_lagi = input("Beli lainnya? [Y/N] : ")
        if(belanja_lagi=="Y" or belanja_lagi=="y"):
            continue
        else :
            break
    else :
        # CETAK SISA UANG BELANJA
        print("Membeli barang : %d %s"%(jumlah_barang, barang))
        print("Jumlah harga : Rp %d"%(harga_barang))
        print("Sisa uang : Rp %d"%(uang-total_belanja))
        
        belanja_lagi = input("Beli lainnya? [Y/N]  : ")
        if(belanja_lagi=="Y" or belanja_lagi=="y") :
            continue
        else :
            break

print("----------------------------------")
print("Berikut hasil pembelian belanja")
print("Nama pembeli : %s"%(nama_pembeli))
print("Total belanja: Rp %d"%(total_belanja))
print("Sisa kembalian : Rp %d"%(uang-total_belanja))
