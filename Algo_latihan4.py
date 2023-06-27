#jumlah barang
megono = int(input("Jumlah megono : "))
telor   = int(input("Jumlah telor   :"))
ayam  = int(input("Jumlah ayam  : "))
minyak  = int(input("Jumlah minyak :"))
cabai = int(input("Jumlah cabai : "))
beras  = int(input("Jumlah beras  : "))

#jumlahe
j_megono= 3000*megono
j_telor = 2000*telor
j_ayam = 4000*ayam
j_minyak= 15000*minyak
j_cabai = 5000*cabai
j_beras = 9000*beras

#belanja
belanja = (j_megono+j_telor+j_ayam+j_minyak+j_cabai+j_beras)

#diskon
if belanja > 200000 :
  diskon = belanja*0.2
else:
  diskon = 0

#total harga
harga= belanja-diskon

#tampilane
print ("------------------------------------------")
print ("          Toko LAFA Berkah          ")
print ("------------------------------------------")
print ("")
print ("No|    NamaProduk    | Harga  | Jumlah ")
print ("")
print ("1. megono       ",megono,"   Rp2.500 ","","Rp",j_megono)
print ("2. telor        ",telor,"   Rp2.000 ","","Rp",j_telor)
print ("3. ayam       ",ayam,"   Rp4.000"," ","Rp",j_ayam)
print ("4. minyak       ",minyak,"   Rp15.000","","Rp",j_minyak)
print ("5. cabai     ",cabai,"   Rp5.000"," ","Rp",j_cabai)
print ("6. Beras        ",beras,"   Rp9.000"," ","Rp",j_beras)
print ("")
print ("------------------------------------------")
print ("Total Belanja : Rp",belanja)
print ("Diskon        : Rp",diskon)
print ("------------------------------------------")
print ("")
print ("Total harga : Rp",harga)
bayar = int(input("Bayar : Rp"))
while bayar < harga:
    print("Bayar e kurang iki lhe'")
    bayar = int(input("Bayar : Rp"))
print (f"Kembalian : Rp{bayar-harga}")
print ("")
print (" Maturnuwun Boloku ")
