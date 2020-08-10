'''
날짜 계산기
1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31
'''
#[0,31,28,31,30,31,30,31,31,30,31,30,31]
#3 1 3 31

#7 17 12 24
#숫자를 각각 받고, 7.17~8.17, 8,17~9.17, 9.17~10.17,
import sys
sys.stdin = open("input.txt", "r")


for test_case in range(int(input())+1):
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m1,d1,m2,d2=map(int,input().split())
    result=sum(months[m1:m2])+d2-d1+1
    print(f'#{test_case+1} {result}')