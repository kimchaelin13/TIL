
#1번 min,max
import sys
sys.stdin = open("sample_input.txt", "r")


for test_case in range(1, int(input())+1):
    num=int(input())
    num_list=list(map(int,input().split()))
    #print(num_list)
    for i in num_list:
        MAX=max(num_list)
        MIN=min(num_list)
        result=MAX-MIN
    print(f'#{test_case} {result}')

