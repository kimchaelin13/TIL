'''
스도쿠
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    #arr에 9개의 리스트를 담으면서 9*9 arr 만들어줌
    arr = [list(map(int, input().split())) for _ in range(9)]
    result=1 #스도쿠이면 1, 아니면 0으로


    for i in range(9): #9번을 돌면서
        hor=set() #가로줄, 123456789가 겹치지 않게 하기 위해 set()타입을 이용
        ver=set() #세로줄
        for j in range(9):
            hor.add(arr[i][j]) #hor에는 가로줄 담고
            ver.add(arr[j][i]) #ver에는 세로줄 담는다

        if len(hor) != 9: #가로길이가 9가 아니면, 다음 검정할 필요가 없음
            result=0
            break
        if len(ver) != 9: #세로도 마찬가지
            result=0
            break

    trg=0 #3*3을 살펴볼차례
    for x in range(0,9,3): #가로줄 첫번째 0,3,6, 이 범위 안에서만 움직이게 설정
        for y in range(0,9,3):
            rec=set()
            for i in range(3):#첫번째 3*3에서 가로줄 먼저
                for j in range(3): #세로줄 읽고
                    rec.add(arr[x+i][y+j]) #rec에 저장

            if len(rec) != 9:
                result=0
                trg=1 #하나라도 trg 1이 되면 빠져나가도록
                break

        if trg: #만약 trg가 1이 아니라면 바로 빠져나가도록
            break

    print(f'#{test_case} {result}')



