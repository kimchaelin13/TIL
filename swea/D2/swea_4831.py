#전기버스
import sys
sys.stdin = open("input.txt", "r")

T=int(input())

for test_case in range(1,T+1):
    K,N,M = list(map(int,input().split()))
    stops=list(map(int,input().split()))
    stops.extend([0,N])
    stops = sorted(stops)
    loca = 0
    cnt=0
    while True:
        if loca+K >= N:
            break

        else:
            if loca+K in stops:
                cnt+=1
                loca = loca + K

            else:
                bin = []
                for i in range(loca+1,loca+K):
                    if i in stops:
                        bin.append(i)
                if bin == []:
                    cnt=0
                    break
                loca = max(bin)
                cnt += 1



    print(f'#{test_case} {cnt}')





