import sys
sys.stdin = open("input.txt", "r")

'''
n이 1295이면?
각각 읽어주면서 빈 set에 한자리씩 넣어준다.
{1,2,9,5}
그리고 set에 추가한후, n에 n을 더해준 값으로 n을 초기화한다. 그리고 len(set)가 10이 되면 멈춘다!
'''
#문제는 N에 N을 더해버리면 1,2,3,4, 가 아니라 1,2,4,8 이런식으로 된다.
#
T=int(input())
for test_case in range(1,T+1):
    digit = set()
    N = int(input())
    A = N

    while len(digit) < 10:
         for i in str(A):
            digit.add(i)

            if len(digit)==10:
                print(f'#{test_case} {A}')
                break

         A += N