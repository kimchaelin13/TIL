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


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1): 

    #int()안에 리스트는 못들어간대
    #split()은 문자열을 어떤 기준으로 쪼개서 리스트로 변환하는 함수
    #그래서 numbers를 리스트로 바꿀려면
    #numbers=map(int,input().split())
    #map함수안에는 iterable한 인자가 모두 들어갈 수 있대! 
    #그런데 이게 map으로만 감싸면 또 타입에러가 나는데, 이건 그때 선생님이 말씀해주신건데
    #map이 무슨 객체,,어쩌고 ㅎ ㅎ 라서 list로 형변환을 해줘야 numbers가 최종적으로 리스트로 변환된거래!!

    numbers=list(map(int,input().split()))

    n_sum = 0
    for n in numbers :
        #그리고 여기는 t가 아니라 n!! numbers안의 n을 하나씩 더하는거니까!
        n_sum = n_sum + n 
        #그리고 답이 정수형태로 나와야해서 round()로 감싸줍니당,,
        avg = round(n_sum / len(numbers))

    print(f'#{test_case} {avg}') #그리고 여기 {test_case}라고 써야하고, acg도 변수니까 {}안에 써야하는것같압,,,
