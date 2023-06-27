#Setting Variabel identitas
nim = input("masukkan NIM  =")
nama =input("masukkan Nama Lengkap =")
kelas =input("masukkan Kelas=")
prodi= input("Masukkan Nama Prodi=")

#Setting Variabel nilai
Bhs_indo =int(input("nilai bahasa indonesia:"))
Bhs_ing  =int(input("nilai bahasa inggris:"))
Pd       =int(input("nilai pemrograman dasar:"))
Mtk      =int(input("nilai matematika:"))
Kal1     =int(input("nilai kalkulius 1:"))
So       =int(input("nilai sistem operasi:"))

#Perhitungan

rata =(Bhs_indo+Bhs_ing+Pd+Mtk+Kal1+So)/6

if(rata>0 and rata <=60):
    grade_rata = ("C") 
elif(rata> 60 and rata <=75) :
    grade_rata = ("B") 
elif(rata> 75 and rata <=85) :
    grade_rata =("AB") 
elif(rata>85 and rata <=100) :
    grade_rata =("A") 
else:
    grade_rata =("Grade Anda Tidak  Ditemukan")

    
if(Bhs_indo >0 and Bhs_indo <=60):
    grade_indo = ("C") 
elif(Bhs_indo> 60 and Bhs_indo <=75) :
    grade_indo = ("B") 
elif(Bhs_indo> 75 and Bhs_indo  <=85) :
    grade_indo =("AB") 
elif(Bhs_indo>85 and Bhs_indo <=100) :
    grade_indo=("A") 
else:
    grade_rata =("Grade Anda Tidak  Ditemukan")
        
if(Bhs_ing>0 and Bhs_ing <=60):
    grade_ing = ("C") 
elif(Bhs_ing> 60 and Bhs_ing <=75) :
    grade_ing = ("B") 
elif(Bhs_ing> 75 and Bhs_ing  <=85) :
    grade_ing =("AB") 
elif(Bhs_ing>85 and Bhs_ing <=100) :
    grade_ing=("A") 
else:
    grade_ing =("Grade Anda Tidak  Ditemukan")
    
if(Pd>0 and Pd<=60):
    grade_Pd = ("C") 
elif(Pd> 60 and Pd <=75) :
    grade_Pd = ("B") 
elif(Pd> 75 and Pd  <=85) :
    grade_Pd =("AB") 
elif(Pd>85 and Pd <=100) :
    grade_Pd=("A") 
else:
    grade_Pd =("Grade Anda Tidak  Ditemukan")
    
if(Mtk>0 and Mtk<=60):
    grade_Mtk = ("C") 
elif(Mtk> 60 and Mtk <=75) :
    grade_Mtk = ("B") 
elif(Mtk> 75 and Mtk  <=85) :
    grade_Mtk =("AB") 
elif(Mtk>85 and Mtk<=100) :
    grade_Mtk=("A") 
else:
    grade_Mtk =("Grade Anda Tidak  Ditemukan")
    
if(Kal1>0 and Kal1<=60):
    grade_Kal1 = ("C") 
elif(Kal1> 60 and Kal1 <=75) :
    grade_Kal1 = ("B") 
elif(Kal1> 75 and Kal1  <=85) :
    grade_Kal1 =("AB") 
elif(Kal1>85 and Kal1<=100) :
    grade_Kal1=("A")
else:
    grade_Kal1 =("Grade Anda Tidak  Ditemukan")
    
if(So>0 and So<=60):
    grade_So = ("C") 
elif(So> 60 and So <=75) :
    grade_So = ("B") 
elif(So> 75 and So  <=85) :
    grade_So =("AB") 
elif(So>85 and So<=100) :
    grade_So=("A") 
else:
    grade_So =("Grade Anda Tidak  Ditemukan") 
    
    
#Cetak Hasil
print("------------------------------------------------") 
print("                    KARTU HASIL STUDI           ") 
print("------------------------------------------------") 

print ("Nim          :",nim)
print ("Nama lengkap  :",nama)
print ("kelas             :",kelas)
print ("Program Studi     :",prodi)
print ("--------------------------")
print ("No   Nama   Makul   Nilai   Grade") 
print ("---------------------------")
print ("1.Bahasa Indonesia  : ",Bhs_indo,"",grade_indo)
print ("2.Bahasa Inggris    : ",Bhs_ing,"",grade_ing)
print ("3.Pemrograman Dasar : ", Pd,"",grade_Pd)
print ("4.Matematika        : ",Mtk,"",grade_Mtk)
print ("5.Kalkulus 1        : ",Kal1,"",grade_Kal1)
print ("6.Sistem Operasi    : ",So,"",grade_So) 
print ("-------------------------")
print ("Rata-rata" ,rata," ",grade_rata)  
print ("-------------------------")
