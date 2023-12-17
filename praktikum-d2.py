print('pertemuan-2\n')

a = True
b = False
print('===========ini and===========')
hasil = a and a
print ('nilai',a,'and',a,'adalah',hasil)
hasil = a and b
print ('nilai',a,'and',b,'adalah',hasil)
hasil = b and a
print ('nilai',b,'and',a,'adalah',hasil)

print('\n===========ini or===========')
hasil = a or a
print ('nilai',a,'or',a,'adalah',hasil)
hasil = a or b
print ('nilai',a,'or',b,'adalah',hasil)
hasil = b or a
print ('nilai',b,'or',a,'adalah',hasil)

print('\n===========ini not===========')
hasil = not a
print('hasil not',a,'adalah',hasil)
hasil = not b
print('hasil not',b,'adalah',hasil)

print('\n===========ini xor===========')
hasil = a ^ a
print ('nilai',a,'xor',a,'adalah',hasil)
hasil = a ^ b
print ('nilai',a,'xor',b,'adalah',hasil)
hasil = b ^ a
print ('nilai',b,'xor',a,'adalah',hasil)
hasil = b ^ b
print ('nilai',b,'xor',b,'adalah',hasil)

print('\n===========ini nand===========')
hasil = not (a and a)
print ('nilai',a,'nand',a,'adalah',hasil)
hasil = not (a and b)
print ('nilai',a,'nand',b,'adalah',hasil)
hasil =not (b and a)
print ('nilai',b,'nand',a,'adalah',hasil)
hasil =not (b and b)
print ('nilai',b,'nand',b,'adalah',hasil)

print('\n===========ini nor===========')
hasil = not (a or a)
print ('nilai',a,'nor',a,'adalah',hasil)
hasil = not (a or b)
print ('nilai',a,'nor',b,'adalah',hasil)
hasil = not (b or a)
print ('nilai',b,'nor',a,'adalah',hasil)
hasil = not (b or b)
print ('nilai',b,'nor',b,'adalah',hasil)

print('\n===========ini nxor===========')   #atau bisa menambahkan not sebelum hasil
hasil = a ^ a
print ('nilai',a,'nxor',a,'adalah',not hasil)
hasil = a ^ b
print ('nilai',a,'nxor',b,'adalah',not hasil)
hasil = b ^ a
print ('nilai',b,'nxor',a,'adalah',not hasil)
hasil = b ^ b
print ('nilai',b,'nxor',b,'adalah',not hasil)

print('\n===========IS===========')
a = 5
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)

a = 6
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)

print('\n===========is not===========')
a = 5
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)

a = 6
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)

print('\n===========in===========')
nama = 'Bacharuddin Jusuf Habibie'

test = 'rud'
cek = test in nama
print(test,'terdapat di',nama,'adalah'+str(cek))

test = 'bach'
cek = test in nama
print(test,'terdapat di',nama,'adalah'+str(cek))

test = 'ib'
cek = test in nama
print(test,'terdapat di',nama,'adalah'+str(cek))

test = 'a'
cek = test in nama
print(test,'terdapat di',nama,'adalah'+str(cek))

test = 'i'
cek = test in nama
print(test,'terdapat di',nama,'adalah'+str(cek))

test = 'u'
cek = test in nama
print(test,'terdapat di',nama,'adalah'+str(cek))

test = 'e'
cek = test in nama
print(test,'terdapat di',nama,'adalah'+str(cek))

test = 'o'
cek = test in nama

print('\n ============= in')
data = ['Institut',
        'Teknologi',
        'Bacharuddin',
        'Jusuf',
        'Habibie'
        ]
print('data adalah',data)
test1 = 'Habibie'
test2 = 'Parepare'
test3 = 'Kampus'
test4 = 'Institut'

cek = test1 in data
print(test1,'terdapat di data adalah'+str(cek))
cek = test2 in data
print(test2,'terdapat di data adalah'+str(cek))
cek = test3 in data
print(test3,'terdapat di data adalah'+str(cek))
cek = test4 in data
print(test4,'terdapat di data adalah'+str(cek))

#INI OPERATOR BITWISE
a = 13  #isi dengan tanggal lahir
b = 10  #isi dengan bulan lahir
b += 80
print('\n===========AND===========')
print('Nilai',a,'dalam biner           =',format(a,'08b'))
print('Nilai',b,'dalam biner           =',format(b,'08b'))
print('-----------------------------------------AND')
c = a & b
print('Nilai',a,'&',b,'dalam biner adalah',format(c,'08b'))

print('\n===========OR===========')
print('Nilai',a,'dalam biner           =',format(a,'08b'))
print('Nilai',b,'dalam biner           =',format(b,'08b'))
print('------------------------------------------OR')
c = a | b
print('Nilai',a,'&',b,'dalam biner adalah',format(c,'08b'))

print('\n===========not in===========')
#Tugas buat nama menjadi nama lengkap masing masing
nama = 'Adam Syahqwan'
test = 'dam'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'ada'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'ahq'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'a'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'u'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'e'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'o'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

print('\n===========not in===========')
#TUGAS dengan cara yang sama buat operator untuk not in
data=['Institut',
      'Teknologi',
      'Bacharuddin',
      'Jusuf',
      'Habibie']
print()
print('Data adalah',data)
test1='Habibie'
test2='Parepare'
test3='Kampus'
test4='Institut'
print()
cek=test1 not in data
print(test1,'Terdapat di data adalah',cek)
cek=test2 not in data
print(test2,'Terdapat di data adalah',cek)
cek=test3 not in data
print(test3,'Terdapat di data adalah',cek)
cek=test4 not in data
print(test4,'Terdapat di data adalah',cek)

# Tugas untuk membuat operator XOR, = a ^ b
print('=========================XOR')
print('Nilai',a,'Dalam biner           =',format(a,'08b'))
print('Nilai',b,'Dalam biner           =',format(b,'08b'))
print('-----------------------------------------------------XOR')
c= a ^ b
print('Nilai',a,'&',b,'Dalam Biner Adalah',format(c,'08b'))

# Tugas untuk membuat operator not, = ~a
print('=========================NOT a')
print('Nilai',a,'Dalam biner         =',format(a,'08b'))
print('-----------------------------------------------------NOT a')
c= ~a
print('Nilai','~','\b',a,'Dalam Biner Adalah',format(c,'08b'))

# Tugas untuk membuat operator not, = ~b
print('=========================NOT a')
print('Nilai',b,'Dalam biner         =',format(b,'08b'))
print('-----------------------------------------------------NOT a')
c= ~b
print('Nilai','~','\b',b,'Dalam Biner Adalah',format(c,'08b'))

# Tugas untuk membuat operator geser kanan, c = a >> 2
print('=========================>>')
print('Nilai',a,'Dalam biner         =',format(a,'08b'))
print('----------------------------------------------------->>')
c= a>>2
print('Nilai',a,'>>','Dalam Biner Adalah',format(c,'08b'))

# Tugas untuk membuat operator geser kiri, c = a << 2
print('=========================<<')
print('Nilai',a,'Dalam biner         =',format(a,'08b'))
print('-----------------------------------------------------<<')
c= a<<2
print('Nilai',a,'>>','Dalam Biner Adalah',format(c,'08b'))

# Tugas untuk operator not and, c = ~ (a & b)
print('=========================not and')
print('Nilai',a,'Dalam biner                 =',format(a,'08b'))
print('Nilai',b,'Dalam biner                 =',format(b,'08b'))
print('-----------------------------------------------------not and')
c=~(a&b)
print('Nilai','~(',a,'&',b,')','Dalam Biner Adalah',format(c,'08b'))

# Tugas untuk operator not or, c = ~ (a | b)
print('=========================not OR')
print('Nilai',a,'Dalam biner                 =',format(a,'08b'))
print('Nilai',b,'Dalam biner                 =',format(b,'08b'))
print('-----------------------------------------------------OR')
c= ~(a|b)
print('Nilai','~(',a,'|',b,')','Dalam Biner Adalah',format(c,'08b'))

# Tugas untuk operator not xor, c = ~ (a ^ b)
print('=========================not XOR')
print('Nilai',a,'Dalam biner                =',format(a,'08b'))
print('Nilai',b,'Dalam biner                =',format(b,'08b'))
print('-----------------------------------------------------not XOR')
c= ~(a ^ b)
print('Nilai ~(',a,'^',b,')Dalam Biner Adalah',format(c,'08b'))

# TUgas untuk operaotr no geser kanan, c = ~(a >> 2) 
print('=========================not Geser kanan')
print('Nilai',a,'Dalam biner                =',format(a,'08b'))
print('-----------------------------------------------------not geser kanan')
c= ~(a >> 2)
print('Nilai ~(',a,'>> 2)','Dalam Biner Adalah',format(c,'08b'))

# TUgas untuk operaotr no geser kiri, c = ~(a << 2) 
print('=========================not Geser kanan')
print('Nilai',a,'Dalam biner                =',format(a,'08b'))
print('-----------------------------------------------------not geser kiri')
c= ~(a << 2)
print('Nilai ~(',a,'<< 2)','Dalam Biner Adalah',format(c,'08b'))







print ('\n'*2)