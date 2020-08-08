'''
시각 덧셈
시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.
(시각은 12시간제로 표시한다. 즉, 시가 가질 수 있는 값은 1시부터 12시이다.)

'''

import sys
sys.stdin = open("input.txt", "r")

#분 부터 더하자
#H1,M1,H2,M2 으로 각각 변수 저장
#M1이랑 M2를 더하고, (M1+M2)%60
#((H1+H2) + (M1/M2)//60)%12

for test_case in range(1, int(input())+1):
    H1,M1,H2,M2=map(int,input().split())
    sumM=(M1+M2)%60
    sumH=((H1+H2) + (M1+M2)//60)%12
    #만약에 시간이 0이 나오면 12로 바꿈
    if sumH==0:
        sumH=12
    print(f'#{test_case} {sumH} {sumM}')

