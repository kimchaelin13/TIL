'''
압축 풀기
[압축된 문서의 내용]

A 10
B 7
C 5

[압축을 풀었을 때 원본 문서의 내용]

AAAAAAAAAA
BBBBBBBCCC
CC


'''


import sys
sys.stdin = open("input.txt", "r")


# 2차원 배열로 단어와 수를 str로 받기

for tc in range(1, int(input()) + 1):
    N = int(input())
    chars = [input().split() for _ in range(N)]
    cnt = 0
    print(f'#{tc}')
    # 10개씩 cnt를 세고 10개가 되면 print()를 해서 한칸 띄워주기
    for i in range(N):  # chars에 들어있는 원소 수만큼 돌아가야됨
        for j in range(int(chars[i][1])):  # 수가 str로 돼있기 때문에 int를 해줌
            cnt += 1
            print(chars[i][0], end='')
            if cnt == 10:  # cnt가 10이 되면 print()로 한줄 띄우고cnt리셋
                print()
                cnt = 0
    print()  # tc끼리는 구분돼야되기 때문

