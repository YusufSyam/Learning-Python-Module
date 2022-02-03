# https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re

credit_cards= [input() for i in range(int(input()))]
# credit_cards= '''4123456789123456
# 5123-4567-8912-3456
# 61234-567-8912-3456
# 4123356789123456
# 5133-3367-8912-3456
# 5123 - 3567 - 8912 - 3456'''.split('\n')

for i in credit_cards:
    is_valid= re.match(r'^[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$', i)
    is_consecutive= re.search(r'(\d)\1\1\1', i.replace('-', ''))

    print('Valid' if is_valid and not is_consecutive else 'Invalid')
    # print('Valid' if is_valid else 'Invalid')