import data from lab7



print("PROGRAM MENAMPILKAN DAFATR NILAI MAHASISWA")
while True:
    print("")
    c =input("(L)lihat, (T)ambah, (U)bah, (H)apus, (K)eluar : ")
    if c.lower() == 't':
        lab7.tambah()

    elif c.lower() == 'u':
        lab7.ubah()

    elif c.lower() == 'l':
        lab7.lihat()

    elif c.lower() == 'h':
        lab7.hapus()

    elif c.lower() == 'k':
        print("Keluar")
        break
