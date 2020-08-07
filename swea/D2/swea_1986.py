'''
1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.
'''
import sys
sys.stdin = open("input.txt", "r")


#for문으로 range()를 이용해서 숫자를 읽고
#만약 홀수면 그냥 어떤 빈 리스트에 담고
#짝수면 -(짝수) 를 담아두고
#마지막에 그 리스트를 모두 더함!

for test_case in range(1,int(input())+1):
    lst=[]
    sum=0
    for i in range(1,int(input())+1):
        if i % 2: #홀수
            lst.append(i)
        else:
            lst.append(-i)
    for i in lst:
        sum+=i
    print(f'#{test_case} {sum}')







