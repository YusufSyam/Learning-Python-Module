import re

# t= int(input())

# text= '''
# 4.0O0
# -1.00
# +4.54
# SomeRandomStuff
# '''

text= ['4.0O0', '-1.00', '+4.54', 'SomeRandomStuff', '-+4.5', '12.', '.5']
# text= ['1.414', '+.5486468', '0.5.0', '1+1.0', '0']

line = int(input())

for i in range(line):
    text = input()
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', text)))

# import re
#
# t= int(input())
# text= [input() for i in range(t)]
#
# for i in text:
#     pattern= re.compile('[+.-]\d+\.[0-9]')
#     if pattern.match(i):
#         print(True)
#     else:
#         print(False)

