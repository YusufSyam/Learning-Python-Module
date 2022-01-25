import re

# text= '''
# 11
# #BED
# {
#     color: #FfFdF8; background-color:#aef;
#     font-size: 123px;
#     background: -webkit-linear-gradient(top, #f9f9f9, #fff);
# }
# #Cab
# {
#     background-color: #ABC;
#     border: 2px dashed #fff;
# }
# '''

line= int(input())

is_css= False

text= []
for i in range(line):
    text.append(input())

for i in text:
    if '{' in i:
        is_css= True
    elif '}' in i:
        is_css= False
    elif is_css:
        for j in re.findall(r'#[A-Fa-f0-9]{3,6}', i):
            print(j)
