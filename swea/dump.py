
import sys
sys.stdin = open("input.txt", "r")

#list를 먼저 정렬한다
#만약 max(list)가 여러개면? 가장 왼쪽에 있는 값을 선택한다.이걸 어떻게 하지
#[1,2,2,3,4,5,5,6,8,9,9]
# len(A)=11, 9의 개수는 2개. list[len(A)-count(max(A))]

#만약 min(list)가 여러개면? 가장 오른쪽에 있는 값을 선택한다.
#list(count(min(list)-1))

#물론 max(list)와 min(list)가 한개밖에 없으면 그 값을 선택하면 된다.
#max와 min값을 선택해서 max-1해주고 min+1해준다.
#언제까지? 리스트의 모든 값이 같아질때까지

T = int(input())

for test_case in range(1, 11):
    number=list(map(int,input().split()))

    for i in range(T):
        MAX, MIN = max(number), min(number)
        max_index = number.index(MAX)
        min_index = number.index(MIN)
        number[max_index] -=1
        number[min_index] += 1
    
    print(f'#{test_case} {max(number)-min(number)}')

