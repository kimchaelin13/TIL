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
#일단 연도는 0보다만 크면 됨
#월은 01~12만 가능
#일은 1월,3월,5월,7월,8월,10월,12월은 1일~31일 가능
#2월은 28일, 4월/6월/9월/11월은 1일~30일
#여기 안들어가면 모두 -1을 내뱉자
#어떻게 해야하지?
#22220228
#문자열로 바꿔서 [0:4]까지 연도고, [4:6]은 월, 그리고 [6:]은 일이다.
#만약에 월이 1에서 1
#아,,,int로 바꾸면서 앞에 0 다 사라져서 str로 바꿔도 0이 사라짐,,,왓슏아두

for test_case in range(1, T + 1):
    numbers=input()
    year=int(numbers[0:4]) 
    month=int(numbers[4:6])
    date=int(numbers[6:])
    mon_31=[1,3,5,7,8,10,12]
    mon_30=[4,6,9,11]
    mon_28=[2]

    # if len(str(year))<4:
    #     year=print(str(year).zfill(4))
        
    # if len(str(month))< 2:
    #     year=print(str(month).zfill(2))

    # if len(str(date)) < 2:
    #     year=print(str(date).zfill(2))

    if year > 0:

    elif year == 101:
        year == 

        if month in mon_31 and date in range(1,32):
            result=f'{year}/{month}/{date}'

        elif month in mon_30 and date in range(1,31):
            result=f'{year}/{month}/{date}'
        
        elif month == 2 and date in range(1,29):
            result=f'{year}/0{month}/{date}'

        

        else:
            result='-1'

    else:
        result='-1'
    
    print(f'#{test_case} {result}')
