'''
거스름돈
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    value = int(input())  # 거스름돈
    result = 0  # 동전의 개수
    changes=[50000,10000,5000,1000,500,100,50,10]

    fin=[]
    for i in changes:
        result = value//i
        fin.append(result)
        value %= i

    print(f'#{test_case}')
    print(f'{" ".join(map(str, fin))}')  #이거 맨날 [1,2,30]같은걸 1,2,30으로 뽑을때 헷갈렸는데 유용하게 쓸 수 있음
