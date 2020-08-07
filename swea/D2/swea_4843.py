#swea 4843
'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.


10 1 9 2 8 3 7 4 6 5


주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
'''

import sys
sys.stdin = open("input.txt", "r")
#리스트를 오름차순, 내림차순 2개씩 만들어주는데 반만 받아줌(전체길이의 반)
#special sort 빈 리스트를 만들어주고,
#그 리스트의 홀수인덱스에는 오름차순 리스트에 있는 값을 차례로 넣어주고
#그 리스트의 짝수인덱스에는 내림차순 리스트에 있는 값을 차례로 넣어줌

T = int(input())
for test_case in range(1, T + 1):
    L=int(input())
    nums= list(map(int,input().split()))
    incre=sorted(nums)
    decre=sorted(nums,reverse=True)
    specialSort=[0]*L

    #special=i[0]d[0]i[1]d[1]i[2]d[2],
    for i in range(10): #0,1,2,3,4,5,6,7,8,9
        if i%2==0:
            specialSort[i]=decre[i//2]
        else:
            specialSort[i]=incre[(i-1)//2]

    result=specialSort[:10]
    RESULT=''
    for i in result:
        RESULT +=" " + str(i)

    print(f"#{test_case}{RESULT}")








    # result=''
    # for i in range(10):
    #     result += str(specialSort[i])
    # print(" ".join(result))




