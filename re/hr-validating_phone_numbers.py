# https://www.hackerrank.com/challenges/validating-the-phone-number/problem
import re

n= int(input())
arr= [input() for i in range(n)]

for i in range(n):
    if re.match(r'[7-9]\d{9}$', arr[i]):
        print('YES')
    else:
        print('NO')