import os
os.system('cls')


pwd_benar = "ABC123"
a = True
limit = 3
i = 0

while a:
    i+=1
    pwd = input("masukkan password : ")
    if pwd == pwd_benar:
        print("Selamat anda berhasil login!!!")
        a = False
    else:
        os.system('cls')
        print("pasword Salah :<")
        if i == limit:
            print("Kesempatan habis :<")
            a = False
        else:
            print(f"sisa kesempata anda {limit - i}")







