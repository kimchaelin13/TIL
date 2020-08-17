# 가랏! RC카 D2 파이썬
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    speed = 0
    move = 0
    for _ in range(N):
        arr = list(map(int, input().split()))
        if arr[0] == 1: #가속이면,
            speed += arr[1] #스피드에 속도값인 arr[1]을 더해준다.

        elif arr[0] == 2: #감속이면
            if speed > arr[1]: #만약에 speend(현속도)가 감속가속도보다 크다면
                speed -= arr[1] #speed에서 arr[1]을 빼준다.
            else: #반대의 경우면
                speed = 0 #제약사항에 따라 speed를 0으로
        move += speed #모든 조건문을 돌고 나서 move에 speed를 더해준다!

    print('#{} {}'.format(t, move))