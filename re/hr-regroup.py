# https://www.hackerrank.com/challenges/re-group-groups/problem
import re

# s= '..123456789AA'
s= input()

match= re.search(r'([<>0-9a-zA-Z])\1+', s)

print(match.group(0)[0] if bool(match) else -1)

