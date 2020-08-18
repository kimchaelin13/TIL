
import sys
sys.stdin = open("input.txt", "r")
#a사와 b사 각각의 수도요금을 구한다
#그리고 더 적은 쪽을 반환
T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int,input().split())

    A=P*W #A사의 수도요금

    if W <= R:
        B=Q
    else:
        B=Q+((W-R)*S)

    if A > B : #A가 B보다 비싸면
        result=B #B를 선택한다
    else:
        result=A

    print(f'#{test_case} {result}')


