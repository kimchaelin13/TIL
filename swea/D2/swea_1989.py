'''
초심자의 회문검사
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
lst=[]
for test_case in range(1, T + 1):
    lst=list(map(str,input()))
    length=len(lst)

    #만약에 [0,1,2,3,4]인덱스를 비교해야 하면
    #[0]=[4], [1]=[3]이 같은지 안같은지 확인해야함.
    #둘의 인덱스의 합은 전체 길이 -1
    for index in range(length):
        for inde in range(length):
            if index+inde == length-1:
                if lst[index]==lst[inde]:
                    result=1
                else:
                    result=0
    print(f'#{test_case} {result}')


