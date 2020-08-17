import sys
sys.stdin = open("input.txt", "r")
from collections import Counter



T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    numbers=list(map(int,input().split()))

    c=Counter(numbers)
    mode=c.most_common(1)
    result=mode[0][0]
    print(f'#{test_case} {result}')



