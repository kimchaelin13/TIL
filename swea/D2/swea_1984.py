
'''
10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.

(소수점 첫째 자리에서 반올림한 정수를 출력한다.)

'''
import sys
sys.stdin = open("input.txt", "r")

#리스트를 만들고, 정렬함
#거기서 맨앞값과 맨뒷값을 빼고, for문을 돌리면서
#평균값을 구하자

for test_case in range(1, int(input())+1):
    numbers=sorted(list(map(int,input().split())))
    l=len(numbers)

    avg=0
    sum=0
    for i in range(1,l-1):
        sum+= numbers[i]
    avg=sum/(l-2)

    print(f'#{test_case} {round(avg)}')







