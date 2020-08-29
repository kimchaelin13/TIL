### 1. SWEA_2001_파리퇴치

> categoty: 2차원 배열 

- 함수를 이용한 VER1

```python
def flapper(r,c): #2
    sum=0
    for i in range(r,r+M):
        for j in range(c,c+M):
            sum+=flies[i][j]
    return sum


for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    flies=[list(map(int,input().split())) for _ in range(N)]

    ans=0
    for r in range(N-M+1):
        for c in range(N-M+1):
            tmp=flapper(r,c) #1
            if ans<tmp:
                ans=tmp
    print('#{} {}'.format(tc,ans))

```



**things confused**

- `*` 변수 지정, ㄹㅇ 모르겠다. 

  > 답! 
>
  > 헷갈렸던것은 함수의 변수 지정이었다. #1과 #2의 파라미터가 같아야 한다고 착각했음. #1의 flapper(r,c)는 그 위 for문의 변수로 r,c를 적어여 하는거고, #2는 flapper(ㅛ,ㅏ)이렇게 아무거나 적어도 상관이 없음. 




**ver2**

```python
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = []
    for i in range(N):
        flies.append(list(map(int, input().split())))

    killed = []
    for r in range(N-M+1):
        for c in range(N-M+1):
            s = 0
            for m in range(M):
                s += sum(flies[r+m][c:c+M]) #1
            killed.append(s)

    print(f'#{tc} {max(killed)}')
```

**things confused**

- #1 모르겠다/ 일단 뭔지 모르겠고, 어떻게 저렇게 접근할수있는지도

  > 답!
  >
  > `s+= flies[r+m][c:c+M]` 
  >
  > `[c:c+M]` : 내가 현재 있는 c(칼럼)의 위치부터 주어진 M까지만 잘라서 더해줘야하니까
  >
  > `[r+m]`: 여기서 sum은 flies의 0번째의 행+M의 (m=0,1) 이런식으로 가게 됨.
  >
  > 
  >
  > 또한 s의 초기화 위치도 늘 헷갈리는 부분,
  >
  > 여기서는 r=0 c=0 로 헤서 M만큼 돌다가 s를 저장하고 -> r=0 c=1 로 바뀔때 또 초기화를 해주고 다시 M만큼 돌다가 s를 저장함.





### 2. SWEA_1979_어디에 단어가 들어갈까

> catarogy: 2차원 배열 

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





### 3.SWEA_1974_스도쿠 검증

> catarogy: 2차원 배열 

```python
for tc in range(1,int(input())+1):
    arr=[list(map(int,input().split())) for _ in range(9)]
    result=1
    #가로
    for r in range(9):
        row_s = set()
        for c in range(9):
            row_s.add(arr[r][c])
        if len(row_s) != 9: #1
            result=0
            break

    #세로
    for r in range(9):
        col_s=set()
        for c in range(9):
            col_s.add(arr[c][r])
        if len(col_s) != 9:
            result=0
            break
    #3*3
    for r in range(0,9,3):
        for c in range(0,9,3):
            cross_s = set()
            for m in range(3):
                cross_s.update(arr[r+m][c:c+3]) #2
            if len(cross_s) != 9:
                result=0
                break
    print('#{} {}'.format(tc,result))
```

**Approach**

> 중복이 없어야  한다. 여기서 set자료구조가 떠오름. 
>
> #가로, 가로행을 하나씩 읽으면서 set에 원소한개씩 추가한다. 그리고 가로행 하나를 다 넣었을때 그때의 set의 길이가 9가 아니라면 result=0하고 break(그래서 처음에 초기값을 result=1로 줬다. 모두통과했는데 걸리는게 없으면 result=1)
>
> #세로도 똑같음
>
> #3*3 같은 경우는 파리퇴치에서 썼던 방식을 써봄.
>
>  가로 세로 모두 0,3,6 에서만 점프해서 읽으면 되서 범위를 저렇게 잡음



**things confused**

- #1 : if 문의 위치, 처음에는 또 row_s를 구하고, 바로 if문을 아래썼다. 그렇게 되면 row_s에 원소하나를 추가하고, if문으로 넘어가게된다. 근데 나는 모든 한행을 다 추가하고, if문을 통해 검사하기를 원했음. 그러면 indent를 한  칸 앞에서 저렇게 해야함
- #2 : 파리퇴치를 다시한번 연습할 수 있었다!! 여기서 오류가 있었는데, 처음에는 add를 썼는데 set에 여러가지 값을 한번에 추가하는건 update임을 기억하자



