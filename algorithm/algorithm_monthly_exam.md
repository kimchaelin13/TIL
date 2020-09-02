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



**Things confused**

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

**Things confused**

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



### 1-1 study2_edging

```python
for tc in range(1,int(input())+1):
    N,M,K=map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]

    result=[]
    for r in range(N-K+1):
        for c in range(M-K+1):
            total_s=0 
            minus_s=0
            for k in range(K): #1
                total_s += sum(board[r + k][c:c + K]) 

                if k != 0  and k != K-1: #2
                    minus_s += sum(board[r + k][c+1:c+K-1]) #3

            result.append(total_s-minus_s) #4
    print('#{} {}'.format(tc,max(result)))

```

**Approach**

> 파리퇴치처럼 범위에 있는걸 모두 더하고, 테두리를 제외한 것을 따로 뺸다. 

**things confused**

- #1 : 일단 파리퇴치와 똑같음. 범위안에서 전체를 모두 더할거야. 테두리 생각안함
- #2 : 근데 다 더하는데 `if k != 0  and k != K-1:` 이렇게 쓰는게 어려웠다. 근데 수아가 알려쥼 ㅎㅎㅎㅎ r을 생각할 필요가 없음. 지금 움직이는건 k, k가 돌면서 위치를 지정하는거임. 그래서 일단 행의 처음과 끝이 필요가 없기 때문에 k!=0이고, 또 k!=K-1 조건을 설정함. 그러면 [r+k] 에 조건이 적용됨
- #3 :  그리고 세로열을 또 자를건데(테두리만 필요하니까) c+1로 부터 맨 뒤값 필요없으니까 c+K-1로 sum해줘서 테두리안값을 모두 더해버림.
- #4 : 위치!!! 토탈s를 구하고 마이너스s를 모두 구한다음에! 그때의 값을 result에 더해줘야 함. 그래서 위치가 저기에



### 수아코드

```python
T = int(input())
for tc in range(1,T+1):
    #배열 행의 개수 N 배열 열의 개수M, 테두리 한 변의 크기 K
    N, M, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # print(arr)

    MAX = 0
    for i in range(N-K+1): #행 끝idx에서 K만큼 제외
        for j in range(M-K+1):#열 끝 idx에서 K만큼 제외
            #k만큼 돌거야
            SUM = 0
            for ik in range(K):
                for jk in range(K):
               #크기 K만큼 돌건데 idx가 테두리만 볼거야
                    #ki = 처음과 끝일때 kj만 돈다
                    if ik == 0 or ik == K-1:
                        SUM += arr[i+ik][j+jk]
                    #ki = 중간일때 kj 처음과 끝만
                    else:
                        if jk == 0 or jk == K-1:
                            SUM += arr[i+ik][j+jk]
                        # print(arr[i+ik][j+jk])
            if SUM > MAX:
                MAX = SUM
    print('#{} {}'.format(tc,MAX))
```





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



**Things confused**

- #1 : if 문의 위치, 처음에는 또 row_s를 구하고, 바로 if문을 아래썼다. 그렇게 되면 row_s에 원소하나를 추가하고, if문으로 넘어가게된다. 근데 나는 모든 한행을 다 추가하고, if문을 통해 검사하기를 원했음. 그러면 indent를 한  칸 앞에서 저렇게 해야함
- #2 : 파리퇴치를 다시한번 연습할 수 있었다!! 여기서 오류가 있었는데, 처음에는 add를 썼는데 set에 여러가지 값을 한번에 추가하는건 update임을 기억하자





### 4. SWEA_4836_색칠하기

> catarogy: 2차원 배열 

```python
for tc in range(1,int(input())+1):
    N=int(input())
    board=[[0]*10 for _ in range(10)]
    sum=0
    for i in range(N):
        x1,y1,x2,y2,color = map(int,input().split()) #1

        for r in range(x1,x2+1): #2
            for c in range(y1,y2+1):
                board[r][c]+=color

    for r in range(10): #3
        for c in range(10):
            if board[r][c]==3:
                sum += 1

    print('#{} {}'.format(tc,sum))
```

**Approach**

> 일단 2차원 배열문제 파악/ 범위를 지정해서 color에 맞게 1을 추가하든 2를 추가하든 해야함.
>
> 나한테 포인트는 인덱스의 범위지정과 세번째 for문(3이 몇번인지 체크하는) 의 indent 위치였음



**Things confused**

- #1 :우선 어떻게 x1,y1,x2,color를 받아서 각각 더해줘야하지? 가 어려웠음. 어떤 케이스는 2개가 있고 어떤 케이스는 3개가 있어서 헷갈렸다. 결론은 두번째 input값으로 n값이 들어오게 됨. (칠할 영역의 개수 N) 그래서 N만큼 돌면서 값을 int형으로 뽑아낸다. 

- #2 : 2 2  4 4 1 이 들아오면, row는 2부터 4까지/그리고 col은 2부터 4까지 돌면서 color에 해당하는 값을 추가해준다.

- #3 : board를 완성시켜야함. 보드를 완성시키고 3의 개수를 세야 하기 때문에 저렇게 해야함. 코드를 간결하게 2처럼 바꿔서 쓸 수 있다.

  ```python
  #1
  for r in range(10):
      for c in range(10):
          if board[r][c]==3:
              sum += 1
  #2
  for i in board:
      sum+=i.count(3) 
  ```

  

  
  
  

### 4-1. 색칠 영역 구하기

```python
for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    board=[[0]*N for _ in range(N)]

    for _ in range(M):
        cnt=0
        x1,y1,x2,y2=map(int,input().split())

        for r in range(x1,x2+1):
            for c in range(y1,y2+1):
                if board[r][c] == 0: #1
                    board[r][c] +=1

    for r in range(N):
        for c in range(N):
            if board[r][c]==1:
                cnt+=1
    print('#{} {}'.format(tc,cnt))
```



**Approach**

> 색칠하기문제랑 똑같음
>
> 근데 조건이 다름. 똑같은 영역에 겹치게 색칠이 되도, 2가 되는게 아니라 계속 1임

**things confused**

- #1 : `board[r][c] == 0` 조건을 추가함, 이미 색칠이 되어있다면 다시 색칠을 하면 2가 됨. 근데 나중에 cnt로 뽑을건 1이 색칠되어있는걸 다 카운트해서 뽑을것. 그래서 2가 되면 2가 제외됨. 그래서 `만약에 색칠이 되어 있지 않다면` 그때 1을 더해주는 조건을 추가함(one difference from the above one)



### 5. SWEA_1210_Ladder1

```python
for tc in range(1,11):
    N=int(input())
    ladder=[list(map(int,input().split())) for _ in range(100)]
    dx=ladder[99].index(2) #99번리스트에서(마지막줄) 값이 2인 index를 찾아라!, 리스트는 find 못씀
    dy=99
    move=0

    while dy>0:
        #left
        if (move==3 or move==1) and dx>0 and ladder[dy][dx-1]==1:
            move=1
            dx-=1
        #right
        elif (move==3 or move==2) and dx<99 and ladder[dy][dx+1]==1:
            move=2
            dx+=1
        #up
        else:
            move=3
            dy-=1

    print('#{} {}'.format(tc,dx))
```

**Approach**

> 1이 있는게 길이있음. 길따라 좌,우,내려가다가 마지막 줄에서 goal인 2에 닿으면, 끝남. 그럼 그때 출발한 첫째행의 인덱스를 구하라! 
>
> 0번행의 모든 x를 다 조사하면서 내려갈수도있겠지만, 마지막 줄에서 2를 찾고, 거기서부터 사다리를 타고 올라가서 첫번째 행에 도달했을때, 그때의 x인덱스를 찾는게 더 효율적일것! 

**things confused**

- #1 : `(move==3 or move==1) and dx>0 and ladder[dy][dx-1]==1` 순서가 중요함. 
- #2 : dx, dy는 x와 y가 현재 어디있는지!! 먼저 선언, dy=99는 마지막 열에서부터 시작하니까
- #3 : while문! 어디까지 돌껀데? dy가 0보다 클때까지!! 계속 오,왼,up으로 와서 0번째줄까지 와주세요





### 6. SWEA_1211_Ladder2

```python
for tc in range(1,11):
    N=input()
    ladder=[list(map(int,input().split())) for _ in range(100)]
    start_xs=[i for i in range(100) if ladder[0][i]==1]
    min_cnt=99999
    ans=0

    for start_x in start_xs:
        dx=start_x
        dy=0
        move=0
        cnt=0
        while dy < 99:
            #left
            if (move==3 or move==1) and dx>0 and ladder[dy][dx-1]==1:
                move=1
                dx-=1
            #right
            elif (move==3 or move==2) and dx<99 and ladder[dy][dx+1]==1:
                move=2
                dx+=1
            #down
            else:
                move=3
                dy+=1
            cnt+=1

        if min_cnt>cnt:
            min_cnt=cnt
            ans=start_x
    print('#{} {}'.format(tc,ans))
```

**Approach**

> 가장 먼저 도착하는 시작 x좌표, 그럼 한개씩 다 봐여함. (0번째 행에서 1이 있는 것만 시작좌표가 될 수 있으므로, 따로 뽑아야하고, 움직일때마다 cnt를 하나씩 더한다. 그리고 모두 돌고(=while문이 끝나고) 미리 설정한 min_cnt를 cnt로 갱신한다. 그리고 ans에 뽑은 start_x를 집어넣음. min_cnt는 첫번째 start_x가 마지막 행의 1에 도달했을때까지의 cnt가 되었다. 이제 그 다음 start_x의 cnt가 더 작다면 계속 갱신된다. 



**things confused**

- 위치 위치 위치

- 지금 헷갈리는거 dx=start_x 이거 왜 해야하는지 모르겠다 그냥 start_x로 하면 안되나????

  > 안됨. 내가 필요한건 처음에 시작한 x인덱스의 위치임. 근데 처음에 start_x로 바로 +를 해버리고 -를 해버리면, 나중에 ans=start_x를 했을때, 이동하다가 마지막행 x좌표의 인덱스 값이 나와버림. 그래서 dx=start_x를 설정해주고, dx를 움직이고, 나중에 최종 ans에 처음에 start_x로 갱신해야 함





### 7. SWEA_4869_종이붙이기

> categoty : dp, stack

```python
for tc in range(1,int(input())+1):
    N=int(input())
    lists=[]
    lists.append(1)
    lists.append(3)
    for i in range(2,N//10):
        lists.append(lists[i-1] + (lists[i-2])*2)
    print('#{} {}'.format(tc,lists.pop()))
```

**Approach**

> 전형적 점화식 문제. 문제에서 규칙을 찾고, lists에 1과 3을 append한다. 그리고 찾은 점화식을 통해 lists에 하나씩 append해줘야 하기 때문에, 인덱스 2부터 찾아야하는 N//10까지 돌리면서 lists에 추가해준다.
>
> 그리고 최종결과는 리스트의 마지막값을 pop해주면 된다. 





### 8. SWEA_4866_괄호검사

> cateogory: stack

```python
for tc in range(1,int(input())+1):
    sentence=input()
    stack=[]
    result=1
    for i in sentence:
        if i in '({':
            stack.append(i)

        elif i in ')}':
            if len(stack)==0: #1
                result=0
                break
            else:
                tmp=stack.pop(-1) #2

            if i==')' and tmp=='(':
                continue
            elif i=='}' and tmp=='{':
                continue
    if len(stack)!=0:#3
        result=0 #4
    print('#{} {}'.format(tc,result))
```

**Approach**

> stack의 전형적인 문제. 여는 괄호를 만나면 스택에 넣고, 닫는 괄호를 만나면? 일단 스택의 top에 있는걸 pop해서 tmp라는 변수에 저장하고, 지금 있는 닫는 괄호와 비교한다. 그리고 만약에 두개가 똑같으면 continue(result를 처음에 1로주고, 뭐가 안맞으면 0으로 바꾸는 구조)



**things confused**

- #1 : 일단 닫는 괄호를 만났는데 스택이 비어있으면 그건 뭔가 잘못된거임 result=0으로 해주고, break
- #2 : 만약에 아니면 비교해야하기 때문에 tmp에 stack의 top을 뽑아서 저장한다.
- #3 : 역시 위치.... 이건 모든비교가 끝나고! 모든 sentence의 끝까지 다 돌았을때!! 그때 stack에 뭔가 남아있으면 그건 또 뭔가 잘못된거임. result=0
- #4 : 여긴 break치면 안됨/ 그럼 아예 for문을 빠져나가고 다음 케이스로 가지않고 종료되버림



### 9. SWEA_4873_반복문자 지우기

> category : stack

```python
for tc in range(1,int(input())+1):
    chars=input()
    stack=[]
    for i in range(len(chars)):
        stack.append(chars[i])
        if len(stack)>1:
            if stack[-1]==stack[-2]:
                del stack[-2:]
    print('#{} {}'.format(tc,len(stack)))
```

**Approach**

> 일단 stack에 chars를 하나씩 넣음. 근데 만약에 stack의 길이가 1보다 클때, 그때 만약에 스택의 맨뒤값과 그 앞값이 같다면?? 두개 다 지워버림



### 10. SWEA_4871_그래프 경로(다시 해보자)

> category : dfs

```python
def DFS(s):
    visited[s]=1

    for i in range(1,V+1):
        if arr[s][i]==1 and visited[i]==0:
            DFS(i)




for tc in range(1,int(input())+1):
    V,E=map(int,input().split())
    arr=[[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        u,v=map(int,input().split())
        arr[u][v]=1
    s,e=map(int,input().split())
    visited=[0]*(V+1)
    DFS(s)
    print('#{} {}'.format(tc,visited[e]))
```







### 11. SWEA_4864_문자열 비교

> brute force, 완전탐색

```python
for tc in range(1,int(input())+1):
    str1=input()
    str2=input()
    A=len(str1)
    B=len(str2)

    result=0
    for i in range(B-A+1):
        for j in range(A):
            if str2[i:i+A] == str1: #1
                result=1
                break
    print('#{} {}'.format(tc,result))
```

**Approach**

> ABC
>
> ZZZZZ**ABC**ZZZZZ
>
> 두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.
>  
>
> ABC
>
> ZZZZ**A**Z**BC**ZZZZZ
>
> 문자열이 일치하지 않으므로 0을 출력.
>
> 이런 문제인데, 완전탐색으로 풀어야 한다고 생각함. 그리고 초기값을 result=0으로 하고, 만약에 맞는게 있으면 1로 갱신하고 그순간 나옴(break) 

**Things confused**

- #1 : 하 범위설정 진짜 헷갈린다. 







### 12. SWEA_4865_글자수(count안쓰고 하고싶다)

```python
for tc in range(1,int(input())+1):
    str1=input()
    str2=input()
    A=len(str1)
    B=len(str2)
    cnt=0
    for i in str1: #1
        sub_cnt=0 #2
        for j in str2:
            if i==j:
                sub_cnt+=1
        if sub_cnt>cnt:
            cnt=sub_cnt
    print('#{} {}'.format(tc,cnt))
```



**things confused**

- #1: str1이 짧은 문자고, str2가 긴 문자임. 짧은 문자에 있는 한글자와 긴문자열에 있는 한글자한글자를 쫙 비교해야하기때문에 저렇게 순서가 나옴. 
- #2 : 그리고 짧은 문자열안에 한글자를 긴 문자열에서 다 세주고, 다음 문자열로 넘어갈때! 그때 sub_cnt는 초기화해야한다. 그래서 위치 저럼







### 13. SWEA_4861_회문

```python
for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    result=[]
    #가로부터 먼저 검사
    garo=[input() for _ in range(N)]
    for ga in garo:
        for i in range(N-M+1):
            if ga[i:i+M]==ga[i:i+M][::-1]:
                result.append(ga[i:i+M])

    #세로는 세로 쪼개서 가로처럼 만들기 먼저해야함...
    sero=[]
    for i in range(N):
        sero_sub = ''
        for ga in garo:
            sero_sub+=ga[i]
        sero.append(sero_sub)

    #다 만들었다! 세로검사 시작~
    for se in sero:
        for i in range(N-M+1):
            if se[i:i+M]==se[i:i+M][::-1]:
                result.append(se[i:i+M])
    print('#{} {}'.format(tc,result[0]))
```









### 14. SWEA_회문2부터 하자

## 이거 다시~~~~~~

```python
for tc in range(1,11):
    trash=input()
    result=1 #회문을 찾으면 result를 계속 갱신할것
    N=100
    #가로
    garo=[input() for _ in range(100)]

    for M in range(100,result,-1):
        for ga in garo:
            for i in range(N-M+1):
                if ga[i:i+M]==ga[i:i+M][::-1]:
                    if len(ga[i:i+M])>result:
                        result=len(ga[i:i+M])
        if result>M:
            break

    #세로
    sero=[]
    for i in range(100):
        sero_sub = ''
        for ga in garo:
            sero_sub+= ga[i]
        sero.append(sero_sub)

    #세로를 해보자~~~
    for M in range(100,result,-1):

        for se in sero:
            for i in range(N-M+1):
                if se[i:i+M] == se[i:i+M][::-1]:
                    if len(se[i:i+M])>result:
                        result=len(se[i:i+M])
        if result>M:
            break
    print('#{} {}'.format(tc,result))
```

**Approach**

> 가로, 세로 각각 읽음
>
> 그리고 가로행을 읽는데, 가장 100개를 처음에 읽고, 점점 줄여간다.

**things confused**

- if result>M, 이거 왜 바로 나오지? 그리고 생각대충해서 코드 과정 헷갈림





### 15. SWEA_4835_구간합

```PYTHON
for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    arr = list(map(int,input().split()))
    result=[]

    for i in range(N-M+1):
        total = 0
        total+=sum(arr[i:i+M])
        result.append(total)
    print('#{} {}'.format(tc,max(result)-min(result)))
```

**Approach**

> brute force, 완전 탐색





### 16. SWEA_4834_숫자 카드

```python
for tc in range(1,int(input())+1):
    b=int(input())
    a = list(map(int,input()))
    MAX=0
    result=0

    for i in range(len(a)):
        cnt=0
        cnt=a.count(a[i])

        if cnt>MAX:
            MAX=cnt
            result=a[i]
            
            if MAX==1:
                result=max(a)

    print('#{} {} {}'.format(tc,result,MAX))
```

**Approach**

> 





### 17. SWEA_4871_그래프 경로

```python
def DFS(s):
    global result #2
    visited[s]=1

    for i in range(1,V+1):
        if arr[s][i]==1 and visited[i]==0: #3
            if i == e: #4
                result=1 
                return result
            DFS(i)


for tc in range(1,int(input())+1):
    V,E =map(int,input().split())
    arr=[[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        u,v=map(int,input().split())
        arr[u][v]=1

    s,e=map(int,input().split())
    visited=[0]*(V+1)
    result=0
    DFS(s) #1

    print('#{} {}'.format(tc,result))
```

**Approach**

> start node에서 end node까지 갈 수 있으면, 1을 return함

**things confused**

- #1 : 여기서 나중에 뽑을 result를 선언함. DFS(s)를 호출하세요 하면 위의 함수로 올라감
- #2 : 밖에서 선언한 result를 조작해서 쓸거니까 global result를 선언
- #3 : `arr[s][i]==1 and visited[i]==0:` 인접행렬에 1이 적혀있고(경로가 존재), 아직 방문행렬에는 1이 적혀있지 않다면, 그리고 끝까지 돌다가 i==e(end node)와 같다면 result를 1로 바꿔준다. 





### 18. SWEA_4843_특별한 정렬

```python
for tc in range(1,int(input())+1):
    N=int(input())
    raw_num=list(map(int,input().split()))
    sorted_num=sorted(raw_num)

    result=[]

    while len(result) < 10:
        result.append(sorted_num[-1])
        result.append(sorted_num[0])
        sorted_num=sorted_num[1:len(sorted_num)-1]
    result=' '.join(map(str,result))
    print('#{} {}'.format(tc,result))
```

**Approach**

> 숫자를 받고(raw_num) 오름차순으로 정렬하고, while문을 돌리면서 result의 길이가 10보다 작을때까지!! 돌린다. 
>
> 그리고 오름차순 정렬된 리스트의 마지막 값을 result에 넣어주고(가장 큰 값)/ 가장 첫번째 값을 넣어주고(가장 작은 값), 그리고 정렬된 sorted_num의 가장 작은 수와 가장 큰 수를 잘라줘야 하니까 처음과 끝을 잘라줌 -> [1:len(sorted_num)-1] 이렇게 자르면 앞 뒤가 잘라짐. 그리고 지금 result에는 [1,2,3]이런식으로 리스트형식으로 담겨있는데, 이거를 문자열로 그대로 뽑아주기 위해!! 
>
> `result=' '.join(map(str,result))` 이렇게 해줌! 그러면 1,2,3이 그대로 문자열형태로 나오게 됨. 





### 19. BOJ 단지번호

```PYTHON
#우좌하상
di=[0,0,1,-1]
dj=[1,-1,0,0]

#이 체크함수는 뭉텅이안으로 들어온거임. 뭉텅이안에 있는 1을 세준다
def check(i,j):
    global home_cnt
    visited[i][j] = True
    home_cnt+=1

    for d in range(4):
        ni=i+di[d]
        nj=j+dj[d]

        if ni<0 or ni>=N or nj<0 or nj>=N:
            continue
        if visited[ni][nj]==True:
            continue
        if home_list[ni][nj]==False:
            continue
        check(ni,nj)


N=int(input())
home_list=[list(map(int,list(input()))) for _ in range(N)]
visited=[[0]*N for _ in range(N)]
home=[]
#home_list를 읽어주면서 만약에 원소가 1이고, visited에는 0이 찍혀있으면? 그때 home_cnt를 초기화함.그때 새로운 뭉텅이를 찾았다는 뜻임
#그리고 check함수를 불러올건데 이 함수는 뭉텅이안에 1을 다 세준다.
#그리고 그 체크함수를 통해서 나온 다 센 뭉텅이 하나를 리스트에 어펜드해준다

for i in range(N):
    for j in range(N):
        if home_list[i][j]==1 and visited[i][j]==False:
            home_cnt=0
            check(i,j)
            home.append(home_cnt)
print(len(home))
for h in sorted(home):
    print(h)

```





### 20. 섬의 개수 구하기

```python
di=[0,0,1,-1,-1,1,-1,1] #우좌하상 우상대 우하대 좌상대 좌하대
dj=[1,-1,0,0,1,1,-1,-1]

def DFS(i,j):
    visited[i][j]=True
    for d in range(8):
        ni=i+di[d]
        nj=j+dj[d]

        if ni<0 or ni>=N or nj<0 or nj>=N:
            continue
        if island_list[ni][nj]==False:
            continue
        if visited[ni][nj]==True:
            continue

        DFS(ni,nj)


for tc in range(1,int(input())+1):
    N=int(input())
    island_list=[list(map(int,list(input().split()))) for _ in range(N)]
    visited=[[0]*N for _ in range(N)]
    num=0 #이건 테스트케이스가 달라질때마다 초기화를 시켜야하니까!!

    #island_list를 돌면서, 만약에 값이 들어있고, 또 visited에는 0이 있으면,
    #그건 그때 새로운 뭉텅이의 첫째 값이 진입했다는 것이다.
    #그러면 나는 뭉텅이의 개수를 구하는 것이기 때문에 num에 +1을 해주고
    #그 주위를 탐색하면서, 조건에 맞는데까지 계속 돌리면서!!

    for i in range(N):
        for j in range(N):
            if island_list[i][j] and visited[i][j]==False:
                num+=1
                DFS(i,j)
    print('#{} {}'.format(tc,num))
```





### 21. 미로1

```python
def DFS(i,j):
    global result
    visited[i][j]=1

    if board[i][j]==3:
        result=1
        return

   else:
        for d in range(4):
            ni=i+di[d]
            nj=j+dj[d]

            if ni<0 or ni>=16 or nj<0 or nj>=16:
                continue
            if visited[ni][nj]==True:
                continue
            if board[ni][nj]==1:
                continue
            DFS(ni,nj)



for tc in range(1,11):
    N=int(input())
    board=[list(map(int,list(input()))) for _ in range(16)]
    visited=[[0]*16 for _ in range(16)]
    result=0 #결과 초기화!! 테스트케이스마다
    for i in range(16):
        for j in range(16):
            DFS(1,1)

    print('#{} {}'.format(tc,result))
```

