import sys
sys.stdin = open("input.txt", "r")

for i in range(1,int(input())+1):
    N=int(input())
    velocity = 0
    distance = 0
    for _ in range(N):
        arr=list(map(int,input().split()))
        if arr[0] == 1:
            velocity += arr[1]
        elif arr[0] ==2 :
            if velocity > arr[1]:
                velocity -= arr[1]
            else:
                velocity=0
        distance += velocity
    print(f'#{i} {distance}')

