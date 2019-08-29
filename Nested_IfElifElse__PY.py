nilai = 50

if nilai == 75: #Equal Eksplisit
    print("Nilai Anda : ", nilai)

if nilai is 60: #Equal
    print("Nilai Anda : ", nilai)

if nilai is not 60: #Not Equal
    print("Nilai Anda bukan 60, melainkan hanya : ", nilai)

print(50 * "-")

if 80 <= nilai <= 100:
    print("Nilai Anda adalah : A")
elif 70 <= nilai <= 80:
    print("Nilai Anda adalah : B")
elif 60 <= nilai <= 70:
    print("Nilai Anda adalah : C")
elif 50 <= nilai <= 60:
    print("Nilai Anda adalah : D, Lakukan Perbaikan")
else:
    print("Maaf, Anda tidak Lulus kuliah ini")

print("")
print(50 * "-", "\nOperator Logika Untuk LIST dan STRING\n", 50 * "-")

#Deklarasi Array Variabel
NamaMahasiswa = ["Muhammad", "Jefri", "Amanda", "Rudi", "Akbar", "Rizky", "Meilysa", "Setel Lingkar"]

NamaDipanggil = "Akbar"
if NamaDipanggil in NamaMahasiswa:          #Jika NamaDipanggil: Akbar ada dalam List NamaMahasiswa, maka
    print("Silahkan Maju Ke Depan")
    print('Silahkan', NamaDipanggil, 'Maju Ke Depan')

NamaDipanggil = "Speaker"
if not NamaDipanggil in NamaMahasiswa:      #Jika NamaDipanggil: Speaker tidak ada dalam list NamaMahasiswa, maka
    print('Apakah ada yang bernama:', NamaDipanggil, '?')

Karakter = 'a'
if Karakter in NamaDipanggil:
    print('Huruf "'+Karakter+'" ada kok di dalam Nama Mahasiswa :', NamaDipanggil)
else:
    print("Tidak Ada")

