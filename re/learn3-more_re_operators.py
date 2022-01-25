import re

# Menggunakan finditer instead of findall

string1= '''
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

string2= '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras ac bibendum tellus, id ullamcorper arcu. Nam fringilla diam auctor dui consectetur porttitor. Mauris sollicitudin ac est ac auctor. Quisque tempor aliquam metus. Aenean felis dolor, egestas ut porttitor ut, mattis ut est. Ut congue enim sit amet eros egestas, ut fermentum felis scelerisque. Pellentesque sollicitudin ligula ac est ultrices pharetra.

Nulla efficitur risus odio, sed accumsan erat maximus ac. Sed semper neque id eros ultricies imperdiet. Phasellus aliquet porttitor vehicula. Mauris gravida bibendum ligula, id dictum ante laoreet bibendum. Cras aliquet tempor lectus sit amet feugiat. Phasellus in elit justo. Sed elementum dui quis arcu efficitur, et auctor ante sollicitudin. Maecenas sit amet ullamcorper leo. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed ut felis laoreet, vulputate ligula consectetur, gravida mi. Cras a purus quis nunc imperdiet fringilla. Fusce tempor, nulla sit amet accumsan sollicitudin, ante ante pretium lorem, quis luctus metus justo in erat. Fusce posuere ac mi ac faucibus. 
'''

# ------------- Soal 1: cari nama yang mengandung mr, ms, atau mrs, bisa ada atau tidak titik setelah nya -------------
sol1= re.finditer(r'M(r|s|rs)\.?\s\w*', string1)

for match in sol1:
    print(match)

# ------------- Soal 2: cari email dari string1 -------------
sol2= re.finditer(r'[A-Za-z0-9.-]+@[a-z-]+\.\w+', string1)

for match in sol2:
    print(match)

# ------------- Soal 3: cari pattern website dari string1 -------------
sol3= re.finditer(r'https?://w?w?w?\.?\w+\.\w+', string1)
sol3_2= re.finditer(r'https?://(www.)?\w+\.\w+', string1)
for match in sol3:
    print(match)

# Misal kita ingin mengambil nama domain (seperti google) dan top level domain (seperti .com)
# Kita bisa membungkus dalam grup terlebih dahulu
sol3_3= re.finditer(r'https?://(www.)?(\w+)(\.\w+)', string1)

for match in sol3_3:
    print(match.group(2), match.group(3))

# Atau simplenya kita bisa menggunakan method .sub()
result_sub= re.sub('https?://(www.)?(\w+)(\.\w+)', r'\2\3', string1)
# r\2\3 artinya kita hanya mengambil group 2 dan 3
print(result_sub)

# ------------- Soal 4: Return all words of a string those starts with vowel -------------
sol4= re.finditer(r'\b[aiueoAIUEO]\w+', string2)

for match in sol4:
    print(match)