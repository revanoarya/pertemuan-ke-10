LAB 6

[![00.png](https://i.postimg.cc/nVkzZsH1/00.png)](https://postimg.cc/RqW9LZJ3)

Pada tugas LAB 6, saya diminta untuk membuat sebuah program menambahkan data ke sebuah list dengan sistem library root yang nantinya akan seperti ini.
 Langkah Langkah\
 
 Disini saya membuat file library root nya terlebih dahulu dengan nama folder yaitu data:
 [![Screenshot-2020-12-02-155257-2.png](https://i.postimg.cc/02zq3rrj/Screenshot-2020-12-02-155257-2.png)](https://postimg.cc/GHnNTLFn)
 [![Screenshot-2020-12-02-155336.png](https://i.postimg.cc/y8024RK1/Screenshot-2020-12-02-155336.png)](https://postimg.cc/yDYL0kWt)
 Setelah itu buat lah file python nya dengan nama (lab6.py) tapi itu terserah kalian mau menggunakan nama apa
 [![gbr3.png](https://i.postimg.cc/dVRNSKRD/gbr3.png)](https://postimg.cc/683hygmN)
 Lalu mari kita mengcoding file tersebut dengan syntax seperti di bawah ini
 
 data = []
data = {}

def tambah():
        print("=======Tambah Data=======")
        nama    =input("Nama                :  ")
        nim     =input("Nim                 :  ")
        tugas   =int(input("Masukan Nilai Tugas :  "))
        uts     =int(input("Masukan Nilai UTS   :  "))
        uas     =int(input("Masukan Nilai UAS   :  "))
        akhir   = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
        data[nama] = nim ,tugas, uts, uas, akhir

def lihat():
    if data.items():
        print("=======Daftar Nilai Mahasiswa=======")
        print("================================================================================================")
        print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
        print("================================================================================================")
        i=0
        for x in data.items():
            i+=1
            print(" | {6:2}  |  {0:12s} | {1:9s} | {2:11}  | {3:11} | {4:11}  |  {5:11} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print("============================================================================================")
    else:
        print("=======Daftar Nilai Mahasiswa======")
        print("================================================================================================")
        print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
        print("================================================================================================")
        print("|                                      TIDAK ADA DATA                                         |")
        print("===============================================================================================")

def ubah():
        print('=======Ubah Data Mahasiswa=======')
        nama = input('Nama                :  ')
        if nama in data.keys():
            nim     =input('Nim                 :  ')
            tugas   =int(input("Masukan Nilai Tugas :  "))
            uts     =int(input("Masukan Nilai UTS   :  "))
            uas     =int(input("Masukan Nilai UAS   :  "))
            akhir   =(0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
            data[nama] = nim, tugas, uts, uas, akhir
        else:
            print("Data Nilai Tidak Ada".format(nama))

def hapus():
        print("=======Hapus Data Mahasiswa=======")
        nama=input("Nama :  ")
        if nama in data.keys():
            del data[nama]
        else:
            print("Data Nilai Tidak Ada".format(nama))


Jika sudah memasukan semua syntax diatas jangan di run terlebih dahulu nanti file tersebut akan rusak/tidak dapat dijalankan nanti hasilnya akan error.

Selanjutnya kita bikin file pythonnya tetapi di luar folder data untuk menjalankan file yang barusan di coding oleh kita. File yang kita akan bikin berilah nama (main.py) karna itu akan menjadi file yang akan menjalankan file library root yang telah kita bikin sebelumnya.

[![gbr4.png](https://i.postimg.cc/1RcHQKnY/gbr4.png)](https://postimg.cc/G9tYPGjk)

Jika sudah mari kita coding lagi file ini mari kita skuylah. Seperti biasa mengikuti syntax nya oke.

from data import lab6

print("PROGRAM MENAMPILKAN DAFATR NILAI MAHASISWA")
while True:
    print("")
    c =input("(L)lihat, (T)ambah, (U)bah, (H)apus, (K)eluar : ")
    if c.lower() == 't':
        lab6.tambah()

    elif c.lower() == 'u':
        lab6.ubah()

    elif c.lower() == 'l':
        lab6.lihat()

    elif c.lower() == 'h':
        lab6.hapus()

    elif c.lower() == 'k':
        print("Keluar")
        break

Nah disini di awal terdapat syntax ini:

from data import lab6

Fungsi nya ini untuk menjalankan file library root nya yaitu dari folder bernama (data) untuk membuka file (lab6.py). Itu penjelasan singkatnya, kalau sudah langsung run aja tapi sebelum di run save dulu nanti kalau hilang nangis :v udah langsung skuy ajalah. Nanti akan jadi seperti di bawah ini.

[![Screenshot-2020-12-03-113632.png](https://i.postimg.cc/DfgqDyH9/Screenshot-2020-12-03-113632.png)](https://postimg.cc/vD4gxMQh)

Cukup sekian tugas dari saya jika ada kesalahan saya mohon maaf yang sebesar besar.

TERIMA KASIH
