Pass1 ='nabati'
pass2 ='cap'
pass3 ='7007'

# Tugas Buat Password Berlapis 3

# Kesempatan 3x , Password Salah, Anda anda gagal pada halaman 1
# Kesempatan 3x , Password Salah, Anda anda gagal pada halaman 2
# Kesempatan 3x , Password Salah, Anda anda gagal pada halaman 3

# Kesempatan 3x , Password Benar, Selamat Datang DI Halaman 1
# Kesempatan 3x , Password Benar, Selamat Datang DI Halaman 2
# Kesempatan 3x , Password Benar, Selamat Anda Berhasil Login

percobaan_1 = 0
limit = 3
a = True
while a :
    percobaan_1 += 1
    print('')
    print('\tTugas Membuat Password Berlapis') 
    pas_1 = (input('\n\tMasukkan Password Pertama : '))
    if pas_1 == Pass1 :
        print('Password Benar, Selamat datang di Halaman 1')
        percobaan_1 *= 0
        while a :
            percobaan_1 += 1
            print('Anda Berada Di halaman Pertama')
            print('Silahkan Masukkan Password untuk ke halaman selanjutnya:)')
            pas_1 = (input('\n\tMasukkan Password Kedua : '))
            if pas_1 == pass2 :
                print('Password Benar, Selamat datang di Halaman 2') 
                percobaan_1 *= 0
                while  a :
                    percobaan_1 += 1
                    print('Anda Berada Di halaman Kedua')
                    print('Silahkan Masukkan Password untuk ke halaman selanjutnya:)')
                    pas_1 = (input('\n\tMasukkan Password Ketiga : '))
                    if pas_1 == pass3 :
                        print('Password Benar, Selamat Anda berhasil login !!!') 
                        a = False
                        percobaan_1 *= 0
                    else  :
                        print('Password salah !!')
                        if percobaan_1 == limit :
                            print('Anda Telah Mencoba 3x dan anda gagal pada halaman 3')
                            a = False
                        else :
                            print('Sisa Kesempatan anda',limit-percobaan_1) 
            else  :
                print('Password salah !!')
                if percobaan_1 == limit :
                    print('Anda Telah Mencoba 3x dan anda gagal pada halaman 2')
                    a = False
                else :
                    print('Sisa Kesempatan anda',limit-percobaan_1)
    else  :
        print('Password salah !!')
        if percobaan_1 == limit :
            print('Anda Telah Mencoba 3x dan anda gagal pada halaman 1')
            a = False
        else :
            print('Sisa Kesempatan anda',limit-percobaan_1)