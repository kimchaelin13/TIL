#구간합

                    
import sys
sys.stdin = open("input.txt", "r")





for test_case in range(1, int(input())+1):
    A,B = map(int, input().split())
    numbers = list(map(int, input().split()))

    a = []
    for i in range(A-B+1):
        a.append(sum(numbers[i:i+B]))

    print(f'#{test_case} {max(a)-min(a)}')