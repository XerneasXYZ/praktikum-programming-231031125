#Input Bilangan X
x = int(input('Masukkan Bilangan X: '))

#cek apakah x adalah bilangan ganjil atau tidak
if x % 2 == 1 :
    #jika x ganji, cetak "Bilangan X adalah ganjil"
    print('Bilangan', x, 'adalah ganjil')
else :
    #jika x bukan ganjil, cetak "Bilangan X adalah bukan Ganjil"
    print ('Bilangan', x,'adalah bukan ganjil')

