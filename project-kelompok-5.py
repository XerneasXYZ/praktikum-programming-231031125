#PROJECT

import datetime
import os
import string
import random

mahasiswa_template = {
    'nama' : 'nama',
    'nim'  : '102030',
    'skslulus' : 20,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True :
    os.system("cls")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print('-'*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa :")
    mahasiswa['skslulus'] = int(input("SKS LULUS:"))
    TAHUN_LAHIR = int(input("Tahun Lahir (yyyy:) "))
    BULAN_LAHIR = int(input("Bulan Lahir (1-12:) "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31:) "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY =''.join((random.choice(string.ascii_uppercase) for i in  range(5)))
    data_mahasiswa.update({KEY:mahasiswa})
    
    
    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<10} {'SKS':<10} {'Lahir':<10}")
    print("-"*60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        
        NAMA = data_mahasiswa[KEY]['nama']
        NIM  = data_mahasiswa[KEY]['nim']
        SKS  = data_mahasiswa[KEY]['skslulus']
        LAHIR= data_mahasiswa[KEY]['lahir'].strftime('%x')
        print(f"{KEY:<6} {NAMA:<15} {NIM:<8} {SKS:^10} {LAHIR:^10}")
        
    print("\n")
    is_done = input("Isi Lagi? (Y/N)")
    if is_done == "n":
        break

print("\nTerima Kasih Telah Mengisi Data")


