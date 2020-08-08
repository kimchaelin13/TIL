from pprint import pprint
#swea4836
'''
색칠하기
'''


import sys
sys.stdin = open("input.txt", "r")
#10*10 0으로 초기화함


T =int(input())
V=[[0]*10 for _ in range(10)]

for test_case in range(1, T + 1):
    V = [[0] * 10 for _ in range(10)]
    t = int(input())
    red=[]
    blue=[]
    result = 0
    for i in range(t):
        x1,y1,x2,y2,color =map(int,input().split())


        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                V[x][y] += color
    #pprint(V)



    for i in V:
        result += i.count(3)
    #print(result)


    print(f'#{test_case} {result}')









