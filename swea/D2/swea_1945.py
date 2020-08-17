
'''
숫자 N은 아래와 같다.

N=2a x 3b x 5c x 7d x 11e

N이 주어질 때 a, b, c, d, e 를 출력하라.
'''


import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    li = [2, 3, 5, 7, 11]
    new = ''
    for i in li:
        cnt = 0
        if N % i == 0:
            while N % i == 0:
                N = N // i
                cnt += 1
            new += str(cnt)
        else:
            cnt = 0
            new += str(cnt)
    result=' '.join(new)

    print(f'#{test_case} {result}')

