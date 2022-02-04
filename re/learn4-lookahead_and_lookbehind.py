import re

# ------------------------------- lookbehind -------------------------------

'''
Regex Lookbehind is used as an assertion in Python regular expressions(re) to determine success or failure 
whether the pattern is behind i.e to the right of the parser’s current position. 
They don’t match anything. Hence, Regex Lookbehind and lookahead are termed as a zero-width assertion.
'''

# Terdapat dua jenis, lookbehind positive (mencari string dengan pattern tertentu di belakangnya) dan
# Lookbehind negative (mencari string yang tidak mempunyai pattern tertentu di belakangnya) Nda tau kalo benar

# Lookbehind positive (?<=pattern)
# Misal terdapat sebuah kasus di mana kita ingin mendapat sebuah kata yang terdapat 3 angka sebelumnya
string1= '123Yusuf new york95 '
lb_positive= re.search(r'(?<=\d{3})\w+', string1)

print(lb_positive)

# Lookbehind negative (?<!pattern)
# Misal kasusnya mencari kata 're' yang tidak diawali oleh angka
string2= '123re parepare'
# lb_negative= re.findall(r'(?<!\d{1,})\w+\b', string2) # Kenapa error?
lb_negative= re.search(r'(?<!\d)re\b', string2)

print(lb_negative)

# ------------------------------- lookahead -------------------------------
# Sama seperti lookbehind tapi dia mencari pattern di depan/kanan string

# Lookahead positive (?=pattern)
# Mencari orang yang mandi
string3= 'arya mandi alip mencuci mas mandi'
la_positive= re.findall(r'\b\w+\b(?=\smandi)', string3)
print(la_positive)

# Lookahead negative (?!pattern)
# Mencari orang yang tidak mandi (tanya di stackoverflow)
la_negative= re.findall(r'\b[^m\s]\w+\b(?!\smandi)', string3)
print(la_negative)

# p= 'john died reyna alive max dying pearl died'
# s= re.split(r'(?<=(died|aliv|dyin)\w*)\s', p) # (tanya di stackoverflow)
# print(s)