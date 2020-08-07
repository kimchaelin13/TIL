
import sys
sys.stdin = open("input.txt", "r")
#중복되는 것없이 앞에서부터 범위를 늘려가면서 읽음
#[0][1] 같은지?
#[0,1] [2,3] 같은지?
#[0,1,2][3,4,5]같은지? 이런식으로 늘려감
for test_case in range(1,int(input())+1):
    s = input()
    #최대마디길이가 10이기 때문에 range(1,11)
    for n in range(1,11):
        if s[:n]==s[n:2*n]:
            break
    print(f'#{test_case} {n}')