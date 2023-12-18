
from datetime import datetime, timedelta

def waktu_operasi():
    waktu1 = input("Masukkan waktu pertama (format HH:MM:SS): ")
    waktu2 = input("Masukkan waktu kedua (format HH:MM:SS): ")
    operasi = input("Masukkan operasi (penjumlahan atau selisih): ")

    format_waktu = "%H:%M:%S"
    waktu1 = datetime.strptime(waktu1, format_waktu)
    waktu2 = datetime.strptime(waktu2, format_waktu)

    if operasi == 'penjumlahan':
        hasil = (waktu1 + timedelta(hours=waktu2.hour, minutes=waktu2.minute, seconds=waktu2.second)).time()
    else:
        return "Operasi tidak valid. Gunakan 'penjumlahan' atau 'selisih'."

    return hasil

print(waktu_operasi())
from datetime import datetime, timedelta

def waktu_operasi():
    waktu1 = input("Masukkan waktu pertama (format HH:MM:SS): ")
    waktu2 = input("Masukkan waktu kedua (format HH:MM:SS): ")
    operasi = input("Masukkan operasi (penjumlahan atau selisih): ")

    format_waktu = "%H:%M:%S"
    waktu1 = datetime.strptime(waktu1, format_waktu)
    waktu2 = datetime.strptime(waktu2, format_waktu)


    if operasi == 'selisih':
        hasil = (waktu1 - timedelta(hours=waktu2.hour, minutes=waktu2.minute, seconds=waktu2.second)).time()
    else:
        return "Operasi tidak valid. Gunakan 'penjumlahan' atau 'selisih'."

    return hasil

print(waktu_operasi())