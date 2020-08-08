'''
스도쿠
'''
import sys
sys.stdin = open("input.txt", "r")

#가로에 9개 담고, 세로에 9개 모두 담고, 길이를 확인하고,
#마지막으로 3*3 배열에 확인함

for test_case in range(1,int(input())+1):
    sdoku=[list(map(int,input().split())) for _ in range(9)]
    result=1

    for i in range(9):
        hor = set()
        ver = set()
        for j in range(9):
            hor.add(sdoku[i][j])
            ver.add(sdoku[j][i])

        if len(hor) != 9:
            result=0
            break

        if len(ver) != 9:
            result=0
            break

    for x in range(0,9,3):
        for y in range(0,9,3):
            rec=set()
            for i in range(3):
                for j in range(3):
                    rec.add(sdoku[x+i][y+j])

        if len(rec) != 9:
            result=0
            break

    print(f'#{test_case} {result}')





