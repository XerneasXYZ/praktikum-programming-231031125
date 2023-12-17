import os
os.system('cls')

a = True

while a:
    jawab = input("apakah ingin lanjutkan ? (y/n)")
    if jawab == 'y':
        print("Terima Kasih")
    elif jawab == 'n':
        os.system('cls')
        print("Sampai Jumpa :D")
        a = False
    else:
        print("ngawur luwh kids :<")
        a = True





