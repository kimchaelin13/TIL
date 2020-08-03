# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys
#몫과 나머지를 출력
#케이스가 3개가 들어오고,첫번째 케이스는 9 2
#9//2=4 , 9%2는 1
#list(map(int,input().split()))으로 [9,2]로 잡는다
#리스트 접근으로 9//2, 9%2 뽑아와서 미리 만들어놓은 문자열에 저장
#마지막 for문 벗어나서 프린트

sys.stdin = open("input.txt", "r")

T = int(input())
result=''
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    number=list(map(int,input().split())) 
    #print(number) [9,2] [15,6] [369,15]
    sh = number[0]//number[1]
    #print(sh)
    re = number[0] % number[1]
    #print(re)
    print(f'#{test_case} {sh} {re}')

