'''
flatten문제
아래 코드 오답이 2케이스가 있음. 다시 해야함
'''
import sys
sys.stdin = open("input.txt", "r")



for test_case in range(1,11):
    T=int(input())
    number=list(map(int,input().split()))

    for i in range(T):
        MAX=max(number)
        MIN=min(number)
        max_index=number.index(MAX)
        min_index=number.index(MIN)
        number[max_index] -=1
        number[min_index] +=1 
    MAX=max(number)
    MIN=min(number)
    print(f'#{test_case} {MAX-MIN}')


