# 0805 TIL



## 2차원 배열

`arr=[[0,1,2,3],[4,5,6,7]]`

- 배열 순회 : n * m 배열의 n*m개 모든 원소를 빠짐없이 조사하는 방법

- 행 우선 순회

  ```python
  #i행의 좌표
  #j열의 좌표
  
  for i in range(len(Array)):
      for j in range(len(Array[i])):
          Array[i][j]
  ```

  

- 열 우선 조회

  ```python
  #i행의 좌표
  #j열의 좌표
  
  for j in range(len(Array[0])): #열
      for i in range(len(Array)): #행
          Array[i][j]
  ```

  

- 델타를 이용한 2차 배열 탐색

  > <델타를 이용한 연습문제1>
  >
  > 5*5 2차 배열에 무작위로 25개의 숫자를 초기화 한후 
  >
  > 25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오
  >
  > 25개의 각 요소에 대해 모두 조사하여 총합을 구하시오
  >
  > 벽에 있는 요소는 이웃한 요소가 없다! `[0][0] `은 이웃한 요소가 2개이다.

  ```python
  dx=[-1,0,0,1]
  dy=[0,-1,-1,0]
  
  arr= [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,3,2,1],
        [1,2,3,4,5],
        [3,4,5,3,2]
        ]
  
  #누적합이 들어가는 변수
  res=0
  N=len(arr)
  M=len(arr[0])
  
  for i in range(5):
      for j in range(5):
          for k in range(4):
              #새로운 좌표를 만들어줌
              #만약 i=0,j=0,k=0이면 (-1,0)이 됨
              #인덱스 아웃되므로 if문 통과못함
              
              x=i+dx[k]
              y=j+dy[k]
              
              if 0<= x < 5 and 0<= y < 5:
                  res += abs(arr[i][j]-arr[x][y])
                  
  print(res)       
  ```

  

- 전치 행렬

  ```python
  # i : 행의 좌표,len(arr)
  # j : 열의 좌표,len(arr[0])
  ```

  ```python
  #입력을 받는 방법
  
  
  #1
  N,M=map(int,input().split())
  mylist=[0 for _ in range(N)]
  #mylist=[0]*N
  
  for i in range(N):
      mylist[i]=list(map(int,input().split()))
  print(mylist)
  
  #2
  N,M=map(int,input().split())
  mylist=[]
  for i in range(N):
      mylist[i].append(list(map(int,input().split())))
  
      
      
      
  #3
  N,M=map(int,input().split())
  mylist=[ list(map(int,input().split())) for _ in range(N)]
  print(mylist)
  ```

  ```python
  #0으로 초기화하는 방법
  
  N=3
  M=4
  
  #1
  V=[[0]*M for _ in range(N)]
  ```

  ```PYTHON
  #전치행렬
  N,M=map(int,input().split())
  mylist=[ list(map(int,input().split())) for _ in range(N)]
  
  for i in range(N):
      for j in range(i+1,M):
          if i<j:
              arr[i][j],arr[j][i] = arr[j][i], arr[i][j]
  ```

  ```python
  #두 개씩 고를때 전치행렬처럼
  #1,2 1,3 1,4 2,3 2,4 3,4
  arr=[1,2,3,4]
  for i in range(lenn(arr)-1):
      for j in range(i+1, len(arr)):
          print((arr[i], arr[j]), end=" ")
  ```



## 부분집합

- 비트 연산으로 간단하게 부분집합을 생성하는 방법

  ```python
  arr = [3,6,7,1,5,4]
  
  n=len(arr) 
  
  for i in range(1<<n): #부분집합의 개수
      for j in range(n): #원소의 수만큼 비트를 비교
          if i & (1<<j): #i의 j번째 비트가 1이면 j번째 원소 출력
              print(arr[j],end=" ")
      print()
      
  print()
  
  #i=0일때는 아무것도 실행하지 않고, 줄바꿈이 일어남.print()
  #맨처음은 공집합을 출력하는거고 그 다음은 원소가 하나인 부분집합 {1}{2}{3}이 나옴
  ```

  

- 부분집합을 리스트에 담자

  ```python
  num=[1,2,3]
  N=len(num)
  lst=[]
  
  for i in range(1<<N):
      sum_lst=[]
      for j in range(N):
          if i & (1<<j):
              sum_lst.append(num[j])
      lst.append(sub_lst)
  ```
  
  
  
  
  
  ```python
  arr=[1,2,3]
  N=len(arr)
cnt=0 #합이 0인 부분집합의 개수를 담는 변수
  
  for i in range(1<<N):
      sum=0 
      sub=[]
      #1개의 부분집합이 계산하게 됨
      #이 과정을 8번 하는 것
      #각각의 원소를 sum에 넣은 것임
      for j in range(N):
          if i & (1<<j):
              sub.append(arr[j])
              sum += arr[j]
     	if sum == 0:
          cnt += 1
          print(sub)
  print(cnt)
  ```
  
  

## 검색



### 순차탐색

- 첫번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다
- 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다
- 자료구조의 마지막에 이를때까지 검색 대상을 찾지 못하면 검색 실패



- 정렬되어 있지 않은 경우

  ```python
  def seq_search(a,n,k):
      i=0
      while i<n and a[i] != key:
          i+=1
      if i<n: return i
      else : return -1
  ```

- 정렬이 된 경우

   ```python
  def seq_serach(a,n,key):
      i=0
      while i<n and a[i]<key:
          i+=1
      if i<n and a[i]==key: return i
      else: return -1
      
  arr=[1,2,3,4,5,6,7,8,9,10]
  key=12
  ```

  

### 이진 검색

- 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 함
- 자료의 중앙에 있는 원소를 고른다
- 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다
- 목표값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 사로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
- 찾고자 하는 값을 찾을때까지 위 과정을 반복한다.

```python
#검색범위의 시작점과 종료점을 이용해서 검색 반복 수행
#이진검색의 경우 자료에 삽입이나 삭제가 발생했을때 배열의 상태를 항상 정렬 상태로 유지하는 추가작업이 필요함.

def binarySearch(a,key):
    start<=0 end <= length(a)-1
    while start<= end:
        middle=(start+end)//2
        if a[middle]==key: #검색성공
            return True
        
        elif a[middle]>key:
            end=middle-1
        else:
            start=middle+1
    return false #검색실패
```





## 선택정렬

주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

- 리스트 중 최솟값을 찾는다
- 그 값을 리스트 맨 앞에 위치한 값과 교환한다.
- 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.

```python

def SelectionSort(a):
    #i=0~ len(a)-1
    for i in range(len(a)-1): #0,1,2,3,4 
        #최소값 찾기
        min=i
        for j in range(i+1,len(a)):
            if a[min] > a[j]:
                min=j
        a[i],a[min]=a[min],a[j]

arr=[64,25,10,22,11]
slectionsort(arr)
print(arr)

```





### 셀렉션 알고리즘

- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법을 셀렉션 알고리즘이라 한다.
- 최소값, 최대값 혹은 중간값을 찾는 알고리즘이라고 한다
  - 정렬 알고리즘을 이용해서 자료 정렬학;
  - 원하는 순서에 있는 원소 가져오기

```python
#k번째로 작은 원소를 찾는 알고리즘
arr=[64,25,10,22,11]
def selection(a,k):
    for i in range(k):
        min=i
        for j in range(i+1,len(a)):
            if a[min] > a[j]:
                min=j
        a[i], a[min] = a[min], a[i]
     return a[k-1]
```



### 선택 정렬 알고리즘

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택 하여 위치를 교환하는 방식
  - 주어진 리스트 중 최소값을 찾는다.
  - 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
  - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다

  ```python
  def selectionSort(a):
      for i in range(0,len(a)-1):
          min=1
          for j in range(i+1,len(a)):
              if a[min] > a[j]:
                  min=j
          a[i],a[min]=a[min],a[j]
  ```

  