# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re

n= int(input())

emails= [input() for _ in range(n)]
# emails= ['DEXTER <dexter@hotmail.com>', 'VIRUS <virus!@variable.:p>']
# emails= '''shashank <shashank@9mail.com>
# shashank <shashank@gmail.9om>
# shashank <shashank@gma_il.com>
# shashank <shashank@mail.moc>
# shashank <shashank@company-mail.com>
# shashank <shashank@companymail.c_o>'''.split('\n')

valid_emails= []

for i in emails:
    res= re.search(r'\<[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]*\.[a-zA-Z]{1,3}>', i)
    # print(res.group(0) if bool(res) else 'Not an email')
    if(bool(res)):
        valid_emails.append(i)

print('\n'.join([i for i in valid_emails]))
