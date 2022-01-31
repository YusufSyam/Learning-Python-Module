# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?

import re

# s= 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
# s= 'abaabaabaabaae'
s= input()

# Sintaks (?=) adalah lookahead, simpelnya untuk mencari pattern yang ovverlap
find= re.finditer(r'(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]([AIUEOaiueo][AIUEOaiueo]+)[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', s)
result= '\n'.join([i.group(1) for i in find])

print(result if len(result)!=0 else -1)