# https://www.hackerrank.com/challenges/re-start-re-end/problem?

import re

# s= 'aaadaa'
# pattern= r'aa'

s= input()
pattern= input()



# print(m)
index_list= []
separator= ('`' if '`' in s else '~')

while(True):
    m = re.search(pattern, s)

    if(bool(m)):
        start= m.start()
        end= m.end()-1
        index_list.append(tuple([start, end]))

        s = s[:start] + separator + s[start + 1:]
    else:
        break

print((-1, -1) if len(index_list)==0 else '\n'.join([str(i) for i in index_list]))
