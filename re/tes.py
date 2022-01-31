a= 'abcdefgh'
# a[2]= 'w'
index= 3
a= a[:index] + 'w' + a[index+1:]

print(a)