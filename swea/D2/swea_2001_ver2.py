import sys
sys.stdin = open("input.txt", "r")
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = []
    for i in range(N):
        flies.append(list(map(int, input().split())))

    killed = []
    for v in range(N-M+1):
        for h in range(N-M+1):
            s = 0
            for m in range(M):
                s += sum(flies[v+m][h:h+M])
            killed.append(s)

    print(f'#{tc} {max(killed)}')