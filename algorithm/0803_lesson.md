# 0803 TIL

- 알고리즘
- 



## 1. 시간복잡도

- 시간 복잡도란 실제 걸리는 시간을 측정, 실행되는 명령문의 개수를 계산
- 시간 복잡도 = 빅-오(O)표기법 (*뭔말인지 모르겠,,*)



## 2. 배열 

### 1. Gravity

- 상자들이 쌓여 있는 방이 있다. 방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할때, 낙차가 가장 큰 상자를 구하여 그 낙차를 리턴하는 프로그램을 작성하시오

  - 중력은 회전이 완료된 후 적용된다.

  - 상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.

  - 방의 가로길이는 항상 100이며 세로길이도 항상 100이다.

  - 즉, 상자는 최소 0 , 최대 100 높이로 쌓을 수 있다.

  - ![]()![image-20200803205659021](C:\Users\kimch\AppData\Roaming\Typora\typora-user-images\image-20200803205659021.png)

  - ```python
    #오른쪽으로 회전한후 중력작용으로 떨어진다.
    #두번째 그림을 보면 왼쪽 값과 비교할 필요가 없음(위로 올라가지않으니까)
    #따라서 자신 인덱스보다 오른쪽에 있는 값만 비교한다.
    #첫번째 값인 7을 생각해보자,
    #오른쪽 값에서 떨어질때 걸리는건? 7과 똑같은 7번째 인덱스! 
    #그래서 7보다 오른쪽에 있는 값중에 7보다 작은 값을 모두 세주면 
    #그게 낙차값이 됨
    
    
    a=[7,4,2,0,0,6,0,7,0]
    #cnt=0
    max=0
    #a의 인덱스를 다 돌아주세요
    for i in range(9):
        cnt=0
        #i 인덱스의 오른쪽에 있는 값들을 비교하면서 다 돌아주세요
        for j in range(i+1,9):
            if a[i] > a[j]:
                cnt += 1
        
        if max<cnt:
            max=cnt
    
    print(max)
    
    ```

### **~~[whatidontgettoday]~~**

- ```python
  #cnt 변수의 위치
  a=[7,4,2,0,0,6,0,7,0]
  #cnt=0 왜 여기 있으면 19가 되는거지.........? 
  max=0
  for i in range(9):
      #cnt=0 무슨 차이일까,,,,,,,,
      for j in range(i+1,9):
          if a[i] > a[j]:
              cnt += 1
      
      if max<cnt:
          max=cnt
  
  print(max)
  ```



**[해결]**

```python
#cnt 변수의 위치
a=[7,4,2,0,0,6,0,7,0]
cnt=0 
#만약에 cnt가 이 위치에 있으면
#i가 0,1,2로 반복할동안 초기화되지 않고 계속 더해진다. 
#누적값이 나옴
max=0
for i in range(9):
    for j in range(i+1,9):
        if a[i] > a[j]:
            cnt += 1
    
    if max<cnt:
        max=cnt

print(max)


```





### 2. Baby-gin Game

- 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을때, 3장의 카드가 연속적인 번호를 갖는 경우 run이라 하고, 3장의 카드가 동일한 번호를 갖는 경우 triplet이라고 한다.

- 그리고 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin이라고 한다.

- 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라.

- **순열을 이용한 문제다**

  - 순열? 서로 다른 것들 중 몇개를 뽑아서 한 줄로 나열하는 것

  - n개중 r개를 선택하는 순열은 아래와 같이 표현한다. `nPr`

    ```python
    #{1,2,3}을 포함하는 모든 순열을 생성하는 함수
    for i1 in range(1,3+1):
        for i2 in range(1,3+1):
            if i2 != i1:
                for i3 in range(1,3+1):
                    if i3 != i1 and i3 != i2:
                        print(i1,i2,i3)
        
    ```

- **완전 검색 방법(Exaustive Search)은 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법이다. 모든 경우의 수를 테스트 한 후, 최종해법을 도출한다. 일반적으로 경우의 수가 상대적으로 작을때 유용하다**
  - **고려할 수 있는 모든 경우의 수 생성하기**

    - 6개의 숫자로 만들 수 있는 모든 숫자 나열(중복 포함)

    - 입력으로 [2,3,5,7,7,7] 을 받았을 경우, 아래와 같이 순열을 생성할 수 있다.

      ![]()![image-20200803234143742](C:\Users\kimch\AppData\Roaming\Typora\typora-user-images\image-20200803234143742.png)

  

  - **해답 테스트하기**

    - 앞의 3자리와 뒤의 3자리를 잘라, run과 triplet 여부를 테스트하고 최종적으로 baby-gin을 판단한다. 

      ![]()![image-20200803234332053](C:\Users\kimch\AppData\Roaming\Typora\typora-user-images\image-20200803234332053.png)







- 탐욕 알고리즘으로 baby-gin 풀어보자

  > c=[0]*12 <-이해 x
  >
  > 

  ```python
  num=456789 #baby gin 확인할 6자리 수
  c=[0]*12 #6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
  
  for i in range(6):
      c[num%10] +=1 #c[9]+=1
      num //=10
      
  i=0
  tri=run=0
  while i<10:
      if c[i]>=3 : #triplete 조사후 데이터 삭제
          c[i] -= 3
          tri += 1
          continue;
          
      if c[i] >= i and c[i+1] >=1 and c[i+2] >=1: #run 조사 후 데이터삭제
          c[i] -=1
          c[i+1] -=1
          c[i+2] -= 1
          run+=1
          continue
          
      i += 1
      
  if run + tri == 2: print('Baby Gin')
  else: print('Lose')
          
  ```

  

### 3. Greedy

- 각 단계에서의 탐욕스런 선택이 최종 답을 구하기 위한 최적의 선택
- 여러 가지 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해나가는 방식으로 진행하여 최종적인 해답에 도달한다.

- 거스름돈 줄이기

  - 예를 들어 2000원을 내고 800원을 거슬러 줘야 한다.
  - 거스름돈을 줄여서 줘야한다!
  - 이것을 greedy하게 살펴보겠다
  - 단위가 큰 동전으로만 거스름돈을 만들면? n(동전의 개수)줄일 수 있다
  - 500원짜리 1개 + 300원 남음. 500원 또 추가할 수 없음
  - 그럼 그 아래 단위인 100원 추가 그럼 200원 남음 
  - 500원으로 돼? 안돼 그럼 100원 추가 100원 남음
  - 500원 1개+100원 1개+100원 1개+100원 1개

- 조폐공사에서 400원짜리 동전을 만들었다고 생각해보자

  - 500원 1개 300원 남음
  - 그럼아까랑 똑같이됨 
  - 정답은 400원짜리 2갠데,!
  - 만약에 400원짜리가 추가되면 greedy하게 풀리지 않는다.
  - 이 경우 완전검색해야 함. dp로 하거나

  ```python
  value = int(input()) #거스름돈 
  result = 0 #동전의 개수 
  
  result += value//500 #500으로 나눈것의 몫을 더해준다 
  value %= 500 #500 으로 나눠준것의 나머지 
  
  result += value // 100 
  value %= 100 
  
  result += value // 50 
  value %= 50 
  
  result += value // 10 
  value %= 10 print(result)
  
  출처: https://j-ungry.tistory.com/166 [정구리의 우주정복]
  ```

  





## 버블 정렬(Bubble Sort)

> 거품이 물에서 떠오르는 모양

![]()![image-20200803204754974](C:\Users\kimch\AppData\Roaming\Typora\typora-user-images\image-20200803204754974.png)

```python
def bubbleSort(myList):
    for i in range(0,len(myList)-1):
        for j in range(0,len(myList)-1-i):
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1]=myList[j+1],myList[j]
    return myList

theList=['b','d','f','a','c','e']
print(bubbleSort(theList))
```



- 버블 정렬 알고리즘의 개념 

  - 서로 인접한 두 원소를 검사하여 정렬하는 알고리즘
    - 인접한 두개의 레코드를 비교하여 크기가 순서대로 되어 있지 않으면 서로 교환한다.

- 버블 정렬 알고리즘 구체적 개념

  - 버블 정렬은 첫번째 자료와 두번째 자료를, 두번째 자료와 세번째 자료를. 세번째와 네번째,이런식으로 (마지막-1)번째 자료와 마지막 자료를 비교하여 교환하면서 자료를 정렬한다.

  - 1회전을 수행하고 나면 가장 큰 자료가 맨 뒤로 이동하므로, 2회전에서는 맨 끝에 있는 자료는 정렬에서 제외되고, 2회전을 수행하고 나면 끝에서 두번째 자료까지는 정렬에서 제외된다. 이렇게 정렬을 1회전 수행할때마다 정렬에서 제외되는 데이터가 하나씩 늘어난다

  - ![]()![image-20200803215446060](C:\Users\kimch\AppData\Roaming\Typora\typora-user-images\image-20200803215446060.png)

    

    

    ```python
    #bubble example
    
    a=[3,2,4,1]
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                
    ```





## Counting Sort: 계수 정렬

- O(n)의 시간복잡도를 갖는다. 

- 범위 조건이 있는 경우에 한해서 빠른 알고리즘이 계수 정렬이다. (속도가 n)
- 숫자들을 서로 비교하는게 아니다 
- 계수를 이용하여 정렬 ; 실제 숫자를 세는 방법으로 숫자가 몇개인지를 기록한다



## Counting Sort(추가)

> 교재설명이 이해가 안가서 아래 링크 블로그 참조
>
> https://bowbowbow.tistory.com/8 



수열 A를 정렬해야 하는 상황이 있다 

`A : 5,5,3,4,5,1,0,4,1,3,0,2,4,2,3,0`

- 첫 번째로 각 숫자가 몇 번 등장하는지 세어준다.

![]()![image-20200803231159866](C:\Users\kimch\AppData\Roaming\Typora\typora-user-images\image-20200803231159866.png)

- 등장 횟수를 누적합으로 바꿔준다.

![]()![image-20200803231235025](C:\Users\kimch\AppData\Roaming\Typora\typora-user-images\image-20200803231235025.png)

- 이 누적합에서 알 수 있는것은 숫자 0은 1~3인덱스에 위치하고, 숫자 2는 4~7 인덱스에 위치한다는 것이다**~~(왜 숫자2가 4~7인덱스에 위치????)~~**
- 정렬할 배열 A를 뒤에서 앞으로 순회하면서 정렬된 배열 B에 넣어준다. 2번 과정에서 구한 누적합이 배열 A의 숫자가 배열 B의 어디에 위치해야 할지 정확하게 알려준다. 

![]()![image-20200803231517860](C:\Users\kimch\AppData\Roaming\Typora\typora-user-images\image-20200803231517860.png)

![]()![image-20200803231551172](C:\Users\kimch\AppData\Roaming\Typora\typora-user-images\image-20200803231551172.png)

![]()![image-20200803231611373](C:\Users\kimch\AppData\Roaming\Typora\typora-user-images\image-20200803231611373.png)

![]()![image-20200803231625420](C:\Users\kimch\AppData\Roaming\Typora\typora-user-images\image-20200803231625420.png)

![]()![image-20200803231637671](C:\Users\kimch\AppData\Roaming\Typora\typora-user-images\image-20200803231637671.png)



- 파이썬으로 구현해보자

  - counts, countSum 이해x
  - #숫자 등장 횟수 누적합 구하기
    - for i in range(1,**MAX_NUM+1**): <- 이해X
  - B=[0]*(**N+1**) <-? 이해 X
  - #수열 A를 정렬한 결과인 수열 B를 출력한다.
    - for i in range(1,N+1):
          result += str(B[i]) + "" <-이해x

  ```python
  #입력 예시 : 1 3 17 5 7
  #출력 예시 : 1 3 5 7 17
  
  #입력될 수 있는 숫자의 최대 크기를 의미한다.
  MAX_NUM=1000
  
  #A는 입력된 숫자를 저장하는 배열
  A = list(map(int,input().split()))
  
  #N은 입력된 숫자의 개수입니다.
  N=len(A)
  
  #0으로 초기화된 입력될 MAZ_NUM+1 길이의 배열 count를 생성합니다.
  count=[0]*(MAX_NUM+1) 
  #countSum은 누적합을 저장하는 배열입니다.
  countSum=[0]*(MAX_NUM)+1
  
  #숫자 등장 횟수 세기
  for i in range(0,N):
     	count[A[i]] += 1
      
  #숫자 등장 횟수 누적합 구하기
  countSum[0] = count[0]
  for i in range(1,MAX_NUM+1):
      countSum[i]=countSum[i-1]+countSum[i]
      
  #B는 정렬된 결과를 저장하는 배열
  B=[0]*(N+1) 
  
  for i in range(N-1,-1,-1):
      B[countSum[A[i]]] = A[i]
      countSum[A[i]] -=1
  
  #수열 A를 정렬한 결과인 수열 B를 출력한다.
  result=""
  
  for i in range(1,N+1):
      result += str(B[i]) + ""
      
  print(result)
  
  
  ```

  

- 정리

  `Counting Sort` 알고리즘의 시간복잡도는 O(n) 으로 `Quick Sort`보다 훨씬 유리해보입니다. 그러나 `Counting Sort`는 대부분의 상황에서 엄청난 `메모리 낭비`를 야기할 수 있습니다.

  누적합 배열에 대한 접근을 O(1)에 달성하기 위해 정렬할 배열에 포함된 숫자의 최댓값 만큼의 메모리를 필요로 합니다. 

  아까 추가로 예시든 <img src="https://t1.daumcdn.net/cfile/tistory/2626824156E755510D" alt="img" style="zoom:50%;" /> 배열에 Counting Sort 알고리즘으로 정렬하기 위해서는 누적합 배열의 길이를 100으로 잡는 낭비를 해야합니다. 만약 배열에 최댓값으로 10억이 포함되어 있다면 엄청난 낭비가 되겠죠.

  따라서 `Counting Sort`는 위에서든 예시처럼

  <img src="https://t1.daumcdn.net/cfile/tistory/2554D94E56E7555107" alt="img" style="zoom: 50%;" />

  정렬하는 숫자가 `특정한 범위`(위 예시 : 0~5) 안에 있을 때 사용하게 됩니다.

  

  `Counting Sort`를 대표적으로 활용하는 사례는 `26개의 알파벳`으로 이루어진 문자열에서 `Suffix Array`를 얻는 경우인데 이때 Counting Sort를 사용하기 때문에 일반적인 Sort를 사용해서 Suffix Array를 얻때 시간복잡도 <img src="https://t1.daumcdn.net/cfile/tistory/2616844456E7555111" alt="img" style="zoom:50%;" />보다 빠른 <img src="https://t1.daumcdn.net/cfile/tistory/211A5E4456E755510E" alt="img" style="zoom:50%;" />에 Suffix Array를 얻는 것이 가능합니다

  

  

  출처: https://bowbowbow.tistory.com/8 [멍멍멍]



## List1_0803_(hw)

```python
for test_case in range(1,11):
    N=int(input())
    a=list(map(int,input().split()))
    sum=0
    
    for i in range(2,len(a)-2):
        max_num=max(a[i-2],a[i-1],a[i+1],a[i+2])
        
        if a[i] > max_num:
            result = a[i]-max_num
            sum += result
            
   print(f'#{test_case} {sum}')
    
```

