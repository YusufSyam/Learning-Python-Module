'''
Berikut adalah operator yang digunakan yang membantu menghasilkan ekspresi
untuk mewakili karakter yang diperlukan dalam string atau file

. 	        Matches with any single character except newline ‘\n’.
? 	        match 0 or 1 occurrence of the pattern to its left
+ 	        1 or more occurrences of the pattern to its left
* 	        0 or more occurrences of the pattern to its left
\w 	        Matches with a alphanumeric character whereas \W (upper case W) matches non alphanumeric character.
\d 	        Matches with digits [0-9] and /D (upper case D) matches with non-digits.
\s 	        Matches with a single white space character (space, newline, return, tab, form) and \S (upper case S) matches any non-white space character.
\b 	        boundary between word and non-word and /B is opposite of /b
[..] 	    Matches any single character in a square bracket and [^..] matches any single character not in square bracket
\ 	        It is used for special meaning characters like \. to match a period or \+ for plus sign.
^ and $ 	^ and $ match the start or end of the string respectively
{n,m} 	    Matches at least n and at most m occurrences of preceding expression if we write it as {,m} then it will return at least any minimum occurrence to max m preceding expression.
a| b 	    Matches either a or b
( ) 	    Groups regular expressions and returns matched text
\t, \n, \r 	Matches tab, newline, return


For more details on  meta characters “(“, “)”,”|” and others details ,
you can refer this link (https://docs.python.org/2/library/re.html).

'''

import re

string1= 'jett revive me jett'
string2= 'watch them run when lit by my sonar, thats, when we strike'

# Contoh soal

# ------------- Soal 0: Dapatkan 1 huruf setelah huruf 'w' -------------
soal0_1= re.findall(f'w\w',string2)
print(soal0_1)

# ------------- Soal 1: Dapatkan kata pertama dari string -------------

# Langkah 1, menggunakan '.'
# Sebaiknya menempatkan r sebelum pattern untuk menyatakan bahwa string pattern merupakan raw string
sol1_1= re.findall(r'.', string1)
print(sol1_1)

# Langkah 2, menggunakan '\w' yang tidak akan mengambil spasi
sol1_2= re.findall(r'\w', string1)
print(sol1_2)

# Langkah 3, menambahkan '*' untuk hanya mengambil kata
sol1_3= re.findall(r'\w*', string1)
print(sol1_3)

# Langkah 4, mengganti '*' dengan '+' untuk tidak mengambil spasi
sol1_4= re.findall(r'\w+', string1)
print(sol1_4)

# Langkah 5, menambahkan '^' untuk hanya mengambil string pertama
sol1_5= re.findall(r'^\w+', string1)
print(sol1_5)

# Jika ingin mengambil string terakhir, gunakan '\w+$' instead

# ------------- Soal 2: dapatkan 2 karakter pertama dari setiap kata dari string -------------

# Langkah 1, ekstrak dua dua huruf dari setiap kata
sol2_1= re.findall(r'\w\w', string2)
print(sol2_1)

# Langkah 2, menambahkan '\b' di kiri '\w' yang artinya
# Hanya mengambil huruf pertama yang bersebelahan dengan spasi
sol2_2= re.findall(r'\b\w\w', string2)
print(sol2_2)

# Solusi lain
sol2_3= re.findall(r'\b\w.', string2)
print(sol2_3)

# ------------- Soal 3: dapatkan kata yang mengandung angka yang diapit 1 atau lebih huruf -------------
string3= 'p1l lolp2qt qwerty3'
sol3_1= re.findall('\w+\d\w+', string3)
print(sol3_1)

# ------------- Soal 4: dapatkan kata 2 karakter (selain new line) sesudah karakter '#' -------------
string4= '#q2ab aksd#vasova #  o'
sol4_1= re.findall('#..(\w+)', string4)
print(sol4_1)

# ------------- Soal 5: dapatkan domain dari sebuah email, misal (com, in) -------------
string5= 'sova@kalolo.biz, abc.test@gmail.com, xyz@test.in'
sol5_1= re.findall(r'@\w+.(\w+)', string5)
print(sol5_1)

# ------------- Soal 6: dapatkan kata yang mengandung lan, lau, atau lap -------------
string6= 'balapan di jalanan walaupun hujan'
sol_6= re.findall(r'\w+la[nup]\w+', string6)
print(sol_6)

# ------------- Soal 7: ekstrak tanggal -------------
string7= 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
sol_7= re.findall(r'\d{2}-\d{2}-\d{4}', string7)
print(sol_7)


