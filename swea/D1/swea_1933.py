
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
#10이 주어지면 약수를 뽑는 예제
#1,2,5,10
#약수는 1부터 10까지 모든 자연수를 나눴을때 나머지가 0인 숫자
#range(T+1) 해서 자연수를 FOR문으로 읽어옴
#그리고 나머지가 0인 i를
#만들어놓은 문자열에 저장한다.
result=''
for i in range(1,T+1):
    if T%i==0:
        print(i,end=' ')
    
        