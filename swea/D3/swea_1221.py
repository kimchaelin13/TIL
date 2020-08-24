'''

'''

import sys
sys.stdin = open("input.txt", "r")


numbers={'ZRO':0,'ONE': 1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
for test_case in range(1, int(input())+1):
    N, M = input().split()
    print(N)
    chars = list(map(str,input().split()))
    chars_list= []
    for char in chars:
        chars_list.append(numbers[char])
    chars_list = sorted(chars_list)
    #print(chars_list)
    result = []
    for key, value in numbers.items():
        for i in chars_list:
            if i == value:
                result.append(key)
    result = ' '.join(result)
    print(result)
















