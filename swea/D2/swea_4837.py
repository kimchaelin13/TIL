#swea 4837
'''
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
 

예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
 

테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''


import sys
sys.stdin = open("input.txt", "r")

T=int(input())
numbers=[ i for i in range(1,13)]
N=len(numbers)
full_lst=[]

#[1,2,3,,,12]의 부분집합을 찾아서 모두 full_lst에 담아둠
for i in range(1<<N):
    sub_lst=[]
    for j in range(N):
        if i & (1<<j):
            sub_lst.append(numbers[j])
    full_lst.append(sub_lst)


for test_case in range(1,T+1):
    N,K=map(int,input().split())

    #부분집합 중 개수가 N인것을 찾기
    n_lst=[]
    for sub in full_lst:
        if len(sub) == N :
            n_lst.append(sub)


    #그 중에 합이 k인 것을 찾기
    cnt=0
    for i in n_lst:
        if sum(i) == K: #n_lst안에는 리스트가 있으므로 i는 리스트임
            cnt+=1

    print(f'#{test_case} {cnt}')



    









