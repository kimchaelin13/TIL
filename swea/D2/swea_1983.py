'''
조교의 성적 매기기
'''
import sys
sys.stdin = open("input.txt", "r")

#10,2 라고 할때, 숫자를 먼저 담고
#다음으로 학생들의 점수를 리스트에 각각 저장함
#그 각각의 학생들의 리스트의 점수를 구함
#그리고 다 구하면 빈 리스트를 만들어서 그 점수를 다 넣어주고, 내림차순 sort
##10명이면 차례차례 넣어주면 되는데, 20명이면?

# for test_case in range(1,int(input())+1):
#     N,K= map(int,input().split())
#     scores=[list(map(int,input().split())) for _ in range(N)]
#
#     for score in scores:
#         finalScore=round(score[0]*0.35+score[1]*0.45+score[2]*0.20)
#         sorted(finalScore, reversed=True)

for test_case in range(1,int(input())+1):
    N,K= map(int, input().split())
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    score=[0]*3 #스코어가 들어올 3개 빈 리스트를 만들고
    scores=[0]*N #전체 변환될 점수가 들어올 n명만큼의 빈 리스트를 만듦
    for i in range(N):#N번을 돌면서, N명의 최종점수를 socres리스트에 넣는다.
        score[0], score[1], score[2] = map(int,input().split())
        scores[i]=(score[0]*0.35)+(score[1]*0.45)+(score[2]*0.20)

    K_score=scores[K-1] #내림차순으로 정렬하기 전에, k에 해당하는 점수를 먼저 k_score변수에 저장한다.
    scores.sort(reverse=True)
    result=grade[scores.index(K_score)// (N//10)]
    #내림차순으로 정렬되어 있기 때문에 i 는 등수를 의미한다.
    #10명 중 i 등이면 [A+, A0, A- ..] 의 i 번째 성적을 받는다.
    #20명 중 i 등이면 [A+, A0, A- ..] 의 i//2 번째 성적을 받는다. (1등도 A+ 2등도 A+)
    #N명 중 i 등이면 [A+, A0, A- ..] 의 i//(N//10)  번째 성적을 받는다.
    print(f'#{test_case} {result}')






