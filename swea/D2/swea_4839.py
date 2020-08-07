#swea4839

'''
짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.

예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.

찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.

A는 300, B는 50 쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.

책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.
'''


import sys
sys.stdin = open("input.txt", "r")

TEST=int(input())

for test_case in range(1,TEST+1):
    F, A, B = map(int, input().split())
    full = [i for i in range(1, F + 1)]
    start_a=0
    end_a=len(full)-1
    start_b=0
    end_b=len(full)-1

    cnt_a=0
    while start_a <= end_a:
        middle_a=(start_a+end_a)//2
        
        if full[middle_a] == A: #검색성공
            cnt_a+=1
            break
            
        elif full[middle_a] < A:
            start_a=middle_a
            cnt_a+=1

        elif full[middle_a] > A:
            end_a=middle_a
            cnt_a+=1



    cnt_b=0
    while start_b<= end_b:
        middle_b=(start_b+end_b)//2
        
        if full[middle_b] == B: #검색성공
            cnt_b+=1
            break

        elif full[middle_b] < B:
            start_b=middle_b
            cnt_b+=1

        elif full[middle_b] > B:
            end_b=middle_b
            cnt_b+=1


    if cnt_a > cnt_b :
        result='B'
    elif cnt_a < cnt_b:
        result='A'
    else:
        result=0

    print(f'#{test_case} {result}')









