
import sys
sys.stdin = open("input.txt", "r")

#A와 B가 가위바위보를 하였다.
# 가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
# A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.
# [입력] 3 2
# [출력] A/A가 이기면 A, B가 이기면 B를 출력한다.
#A가 이길때는? 1/3 2/1 3/2
#B가 이길때는? 3/1 1/2 2/3


T = list(map(int,input().split()))

if T[0]==1 and T[1]==3:
    print('A')
elif T[0]==2 and T[1]==1:
    print('A')
elif T[0]==3 and T[1]==2:
    print('A')

else:
    print('B')
