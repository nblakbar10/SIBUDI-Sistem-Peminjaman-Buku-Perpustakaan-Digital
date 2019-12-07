import time
import sys
import os
import playsound

arynama,arynim,aryjudul,arytglpinjam,arytglkembali = [],[],[],[],[]

class perpus:
    def menu(self):
        print('''
        *********************  \033[34mSIBUDI\033[0m  **********************
        **** Sistem Peminjaman Buku Perpustakaan Digital ****
        Pilih Menu :\033[0m
        \033[34m1. Pinjam Buku
        2. Kembalikan Buku
        3. Cetak Struk Bukti Pinjam
        4. Cek Daftar Buku Lengkap
        5. Lihat History Peminjam Buku
        6. Lihat Peraturan Perpustakaan
        0. Matikan Aplikasi\033[0m
        *****************************************************
        ''')
        playsound.playsound("selamatdatang.mp3")
        while True:
            try:
                pil = int(input('\nMasukkan Pilihan Anda : '))
                if(pil==1):
                    pilih.pinjambuku()
                    pilih.ulang()
                elif(pil==2):
                    pilih.kembalikanbuku()
                    pilih.ulang()
                elif(pil==3):
                    pilih.cetakstruk()
                    pilih.ulang()
                elif(pil==4):
                    pilih.daftarbuku()
                    pilih.ulang()
                elif(pil==5):
                    pilih.daftarpinjam()
                    pilih.ulang()
                elif(pil==6):
                    pilih.peraturan()
                    pilih.ulang()
                elif(pil==0):
                    time.sleep(0.5)
                    #os.startfile("")
                    print("\033[34mTerima Kasih, Sampai jumpa kembali.")
                    quit()
                else:
                    print('\033[31mPilihan tidak tersedia\033[0m')
                    pilih.ulang()
            except ValueError:
                print("Inputan anda salah ! Silahkan ulangi kembali...")

    def ulang(self):
        time.sleep(1)
        ulang = input('Apakah anda ingin mencoba lagi ? [Ya/Tidak] ')
        print('=============================================================\n')
        if (ulang=='Ya' or ulang=='ya' or ulang=='Y' or ulang=='y'):
            pilih.menu()
        elif (ulang=='Tidak' or ulang=='tidak' or ulang=='t' or ulang=='T'):
            time.sleep(0.5)
            print('Terima kasih, sampai jumpa kembali!')
            quit()
        else:
            print('\033[31mInputan anda salah ! Pilih (Ya) atau (Tidak) !\033[0m')
            pilih.ulang()

    def pinjambuku(self):
        #os.startfile("")
        print("Silahkan masukkan data diri Anda\n")
        nama = str(input("\033[34mNama Peminjam Buku : "))
        while True:
            try:
                nim = int(input("NIM : "))
                break
            except ValueError:
                print("Inputan anda salah ! Silahkan ulangi kembali...")
        judul = str(input("Judul Buku : "))
        tglpinjam = str(input("Tanggal Pinjam : "))
        tglkembali = str(input("Tanggal Kembali : "))
        while True:
            try:
                 banyak = int(input("Banyaknya buku yang dipinjam : "))
                 break
            except ValueError:
                print("Inputan anda salah ! Silahkan ulangi kembali...")
        konfirm = str(input("Apakah data diri anda sudah benar?  (Ya/Tidak)\033[0m"))
        for i in range(1):
            arynama.append(nama)
            arynim.append(nim)
            aryjudul.append(judul)
            arytglpinjam.append(tglpinjam)
            arytglkembali.append(tglkembali)
            if (konfirm == 'Ya' or konfirm == 'ya' or konfirm == 'Y' or konfirm == 'y'):
                print('Terimakasih telah meminjam buku ditempat kami, kami berharap agar anda dapat mengembalikan buku dengan tepat waktu\n')
                print('\033[31m*******Silahkan Ambil Struk Anda*******\033[0m')
                print('_____________________________________________________')
                #kode untuk cetak struknya
                #struk = "struk.txt"
                sys.stdout = open("struk.txt", "w")
                print('''
                        *********************  SIBUDI  **********************
                        **** Sistem Peminjaman Buku Perpustakaan Digital ****
                        **************** Struk Bukti Pinjam *****************
                    ''')
                print('\t\t\tTanggal : ',tglpinjam,"2019")
                print("\t\t\tNama Peminjam Buku : ",nama)
                print("\t\t\tNIM : ",nim)
                print("\t\t\tJudul Buku : ",judul)
                print("\t\t\tTanggal Peminjaman : ",tglpinjam)
                print("\t\t\tTanggal Kembali : ",tglkembali)
                print("\t\t\tJumlah Buku yang Dipinjam : ",banyak)
                print('''
                        ***Terima Kasih Telah Meminjam Buku Ditempat Kami***
                        ***Struk Harap Dibawa pada saat pengembalian Buku***
                        ''')
                sys.stdout.close()
                sys.stdout = sys.__stdout__         #ini supaya pas file .txt nya diclose programnya ga muncul error, dan berulang ke kondisi "Apakah anda ingin mencoba lagi?
                time.sleep(1)
                os.system("struk.txt")
            else:
                print('Silahkan ulangi input data diri anda!')
                pilih.pinjambuku()

    def kembalikanbuku(self):
        #os.startfile("")
        #nanti disini buat denda, jika ngembaliin bukunya lewat dari tanggal yang ditentukan, maka akan kena denda dan akan ditampilkan kalkulasi total dendanya
        nama = str(input("\033[34mNama Peminjam Buku : "))
        while True:
            try:
                nim = int(input("NIM : "))
                break
            except ValueError:
                print("Inputan anda salah ! Silahkan ulangi kembali...")
        judul = str(input("Judul Buku : "))
        tglpinjam = str(input("Tanggal Pinjam : "))
        tglkembali = str(input("Tanggal Kembali : "))
        tglsekarang = str(input("Tanggal hari ini : "))
        while True:
            try:
                 banyak = int(input("Banyaknya buku yang dipinjam : "))
                 break
            except ValueError:
                print("Inputan anda salah ! Silahkan ulangi kembali...")
        konfirm = str(input("Apakah data diri anda sudah benar?  (Ya/Tidak)\033[0m"))
        if (konfirm == 'Ya' or konfirm == 'ya' or konfirm == 'Y' or konfirm == 'y'):
            if(tglkembali==tglsekarang):
                print('Terimakasih telah mengembalikan buku dengan tepat waktu')
                print('=============================================================\n')
            else:
                print("\033[31mANDA TERLAMBAT MENGEMBALIKAN BUKU, ANDA AKAN DIKENAKAN DENDA 50.000 rupiah PER HARINYA\033[0m")
                totalterlambat = int(input("Berapa hari anda terlambat mengembalikan buku? : "))
                denda = 50000 * totalterlambat
                print("Jadi total denda yang harus anda bayar adalah = ", denda)
        else:
            print('Silahkan ulangi input data diri anda!')
            pilih.kembalikanbuku()

    def cetakstruk(self):
        #nanti disini bakalan langsung redirect ke file .txt yang isinya berupa struk
        #os.startfile("")
        print('\033[31m*******Silahkan Ambil Struk Anda*******\033[0m')
        time.sleep(1)
        os.system("struk.txt")

    def daftarbuku(self):
        #nanti disini dimasukkan file .txt yang isinya daftar buku di perpustakaan, nanti pas tampilannya mungkin bisa pop-up.
        #os.startfile("")
        print('\033[31mDaftar Buku Lengkap sedang diproses, mohon tunggu...\033[0m')
        time.sleep(2)
        os.system("daftarbuku.txt")

    def daftarpinjam(self):
        print("Daftar History : \n")
        print("Nama : %s\tNIM : %s\tJudul Buku : %s\tTanggal Pinjam : %s\tTanggal Kembali : %s"% (arynama,arynim,aryjudul,arytglpinjam,arytglkembali))

    def peraturan(self):
        print('''Peraturan Peminjaman Buku :
    1. Peminjaman maksimal 2 (dua) buku.
    2. Lama peminjaman 1 (satu) minggu dari tanggal peminjaman.
    3. Setiap peminjam harus mengembalikan pinjaman buku, majalah, surat kabar dan lain-lain sesuai 
       dengan waktu yang sudah ditentukan oleh perpustakaan.
    4. Peminjam wajib mendapatkan & memiliki Struk Bukti Pinjam saat akan hendak meminjam buku.
    5. Saat mengembalikan buku, peminjam wajib membawa dan Struk Kertas Bukti Pinjam kepada
       pengawas perpus.
    6. Perpanjangan masa peminjaman buku hanya boleh dilakukan satu kali.
    7. Apabila buku-buku,majalah,surat kabar yang dipinjam rusak atau hilang harap segera melapor 
       kepada pengelola atau petugas perpustakaan.''')

        print('''Sanksi :
    1. Keterlambatan pengembalian buku dikenakan sanksi denda sesuai dengan peraturan dan tata 
       tertib yang telah ditentukan, yaitu Rp. 10.000,- untuk 1 (satu) buku per hari.
    2. Apabila buku yang dipinjam rusak atau hilang, maka peminjam wajib mengganti dengan buku 
       yang sama, atau membayar 3 (tiga) kali lipat dari harga buku tersebut (ditambah biaya sanksi 
       denda keterlambatan pengembalian buku bila ada).
    3. Bagi pemustaka yang tidak mematuhi peraturan dan tata tertib Perpustakaan, maka di hari 
       selanjutnya tidak akan dilayani.''')
        time.sleep(1)

pilih = perpus()
pilih.menu()
pilih.pinjambuku()
pilih.cetakstruk()
pilih.daftarbuku()
pilih.kembalikanbuku()
pilih.daftarpinjam()
pilih.peraturan()
