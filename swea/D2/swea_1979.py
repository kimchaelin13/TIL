'''
어디에 단어가 들어갈 수 있을까

N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.

주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.
'''
import sys
sys.stdin = open("input.txt", "r")
#파리퇴치와 비슷하게 풀고싶다
#가로를 먼저 읽고, 구간이 K만큼이 합이 3이 되는지, 3이 되는 개수를 세고

for test_case in range(1, int(input())+1):
    N,K=map(int,input().split())
    puzzle=[list(map(int,input().split())) for _ in range(N)]

    result=0
    for i in range(N):
        sum=0
        for j in range(N):
            if puzzle[i][j] == 1: #1이 K번 연속으로 와야하므로 값이 1인지 확인
                sum+=1 #1이면 sum에 1을 더함
                if sum == K:
                    result+=1
            else: #행렬 값이 0인 경우
                sum=0 #아무것도 더하지 않는다

            if sum>K: #딱 K개만 들어갈 자리가 있어야 하므로, 넘으면
                result -=1 #위의 if문으로 추가된 result에서 -1을 하고
                sum=0 #그 다음 블럭에서 만들어질 수 있으니까 sum=0으로 초기화한다.

    for i in range(N):
        sum=0
        for j in range(N):
            if puzzle[j][i] == 1:
                sum+=1
                if sum == K:
                    result+=1
            else:
                sum = 0

            if sum > K:
                result -= 1
                sum=0
    print(f'#{test_case} {result}')






