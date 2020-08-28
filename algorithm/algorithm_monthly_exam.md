### 1. SWEA_2001_파리퇴치

왜 이건 돌아가고 아래껀 안돌아갈까

```python
def flapper(r,c):
    sum = 0
    for i in range(r,r+M):
        for j in range(c,c+M):
            sum += flies[i][j]
    return sum



for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    flies=[list(map(int,input().split())) for _ in range(N)]

    ans = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp=flapper(i,j)
            if ans<tmp:
                ans=tmp

    print("#{} {}".format(tc,ans))
```



```python
def flapper(r,c): #
    sum=0
    for r in range(r,r+M): #
        for c in range(c,c+M): #
            sum+=flies[r][c]
    return sum


for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    flies=[list(map(int,input().split())) for _ in range(N)]

    ans=0
    for r in range(N-M+1): 
        for c in range(N-M+1): 
            tmp=flapper(r,c) ***********
            if ans<tmp:
                ans=tmp
    print('#{} {}'.format(tc,ans))

```



**things confused**

- `*` 변수 지정, ㄹㅇ 모르겠다. 

  tmp=flapper(r,c) 가 위의 flapper함수에서 어떻게 호출되는거지?

  def flapper(r,c) 안에 있는 r,c는 기준을 갖고 쓰는건ㄱㅏ?

- 왜 안돌아가지? 



**ver2**

```python
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
                s += sum(flies[v+m][h:h+M]) #1
            killed.append(s)

    print(f'#{tc} {max(killed)}')
```



#1 모르겠다/ 일단 뭔지 모르겠고, 어떻게 저렇게 접근할수있는지! 뭔가아마 의수오빠코드일거같당,,







### 2. SWEA_1979_어디에 단어가 들어갈까



```python
for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    result=0 #1
    
    
    #가로
    for i in range(N):
        sum = 0 #2
        for j in range(N):
            if arr[i][j] == 1:
                sum+=1
                if sum==K:
                    result+=1
            else:
                sum=0

            if sum>K:
                result-=1
                sum=0
	#세로
    for i in range(N):
        sum = 0
        for j in range(N):
            if arr[j][i]==1:
                sum+=1
                if sum==K:
                    result+=1
            else:
                sum=0

            if sum>K:
                result-=1
                sum=0
    print('#{} {}'.format(tc,result))
```

> 변수 초기화 위치 설정이 늘 헷갈렸는데, 여기서도 헷갈렸음
>
> 그냥 코드를 바로 작성했던게 문제였다. 문제를 보고 줄글로 조건을 자세히 만들고, 어떻게 적용해야할지 먼저!!제발!! 생각하자

#1 : result는 가로, 세로 모두 확인하고 마지막에 값을 뽑아냄. 

#2 : sum이 for밖에 있는지 아래있는지 이중for문 아래인지 헷갈렸는데, 그건 문제마다 모두!!! 달라야 함. 이유를 이 문제를 뜯어보다가 드디어 알았다 ㅎ 여기 sum이 있어야 하는 이유는 이 문제에서 나는 행을 하나씩 점검하면서 sum에 값을 넣고, 조건에 맞춰서 result를 추가하거나 삭제한다. 그리고 다음 행으로 넘어갈때는 당연히 (중간정산용이었던) sum을 초기화해줘야한다. 따라서 row가 바뀌고, 그 아래에서 sum을 초기화해주고 다시 누적해야하는것!!!! 