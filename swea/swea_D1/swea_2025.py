import sys
sys.stdin = open("input.txt", "r")

T = int(input())
#10을 받고 1+2+3+,,=55로 출력해야함
#for문으로 range(T+1)만큼 돌게 함
#하나씩 뽑아서 미리 만들어놓은 변수sum에 저장한다.
sum=0
for i in range(T+1):
    sum+=i
print(sum)

