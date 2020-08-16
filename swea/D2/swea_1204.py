'''
어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.

이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.

다음과 같은 수 분포가 있으면,

10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3

최빈수는 8이 된다.

최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라)
'''

#일단 테스트 케이스 10개를 돌면서!
#케이스 숫자를 리스트에 담자
#그리고, {10:1, 8:4,,}이런식으로,
#그리고 value값이 가장 큰 것을 뽑고, 그것의 키값을 반환

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    nums=list(map(int,input().split())) #숫자를 리스트에 담고,
    newdict={}
    for i in nums:
        newdict[i]=nums.count(i) #newdict에 각각 카운트한 것을 담았다.
    MAX=max(list(newdict.values())) #newdict의 value 중 가장 큰 값을 MAX에 저장
    max_count = 0
    for key, value in newdict.items():
        if max_count < value:  # 4
            max_count = value
            mode = key
        elif max_count == value:  # 5
            if mode < key:
                mode = key
    print(f'#{test_case} {mode}')













