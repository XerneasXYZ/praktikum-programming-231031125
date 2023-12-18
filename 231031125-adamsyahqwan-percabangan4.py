pendapatan = int(input('pendapatan : '))

if pendapatan <= 1000:
        persentase = 0
elif pendapatan <= 2000:
        persentase = 7.9
elif pendapatan <= 3000:
        persentase = 14.9
elif pendapatan <= 4000:
        persentase = 21.9
elif pendapatan <=5000:
        persentase = 28.9
else:
        persentase = 34.9
        
bonus = pendapatan * (persentase / 100)
total = pendapatan + bonus

print('pendapatan:',pendapatan)
print('persentase:',persentase,'%')
print('bonus:',bonus)
print('Jumlah total:',total)