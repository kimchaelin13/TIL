import sys
sys.stdin = open("input.txt", "r")

#리스트를 받고, 뒤에서부터 탐색함
#맨 뒤에 숫자가 max로 설정
#[3,5,9]일때 맨뒤를 초기max로 설정하고 그 앞 숫자부터 1,2면? re+=max-li[j]
#[1,1,3,1,2] #max보다 그 앞일의 가격이 더 크면? 그 앞 요일을 max로 갱신함


for test_case in range(1,int(input())+1):
    N=int(input())
    Li=list(map(int,input().split()))[::-1] #리스트를 뒤에서부터 읽는법
    result=0
    MAX=Li[0]
    for i in range(N-2,-1,-1):
        if MAX > Li[i]:
            result += MAX -Li[i]
        else:
            MAX=Li[i]
    
    print(f'#{test_case} {result}')

