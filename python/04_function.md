# 함수(Function) 2

- 함수와 스코프
- 재귀 함수



## 함수와 스코프(scope)

함수는 코드 내부에 공간(scope)를 생성합니다. 함수로 생성된 공간은 `지역 스코프(local scope)`라고 불리며, 그 외의 공간인 `전역 스코프(global scope)`와 구분됩니다.

- **전역 스코프(`global scope`)**: 코드 어디에서든 참조할 수 있는 공간
- **지역 스코프(`local scope`)**: 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간

- **전역 변수(`global variable`)**: 전역 스코프에 정의된 변수

- **지역 변수(`local variable`)**: 로컬 스코프에 정의된 변수

  ```python
  # 전역 스코프(global scope)
  a = 10 # 전역 변수(global)
  
  def func(b):
      # 지역 스코프(local scope)
      c = 20 # 지역 변수(local variable)
      a = 30
      print(a) #밖에도 a라는 물이 있고, 안에도 a라는 물			이 있다. 그래서 그냥 안에 있는 물 먹음(30)
      print(b)
  
  
  # 변수 c는 접근 불가합니다.
  # print(c)
  # 함수 속 공간(동생방) 밖 가족은 침투 불가, 근데 안에 있는 동생은 다 돌아디닐 수 있음
  # a는 조회 가능, c는 안을 못봄
  ```

  ```python
  # 50을 인자로 전달하여 출력할 수 있습니다.
  func(50)
  ```

  > 30
  >
  > 50 



## 이름 검색 규칙

파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있습니다.

이것을, `LEGB Rule` 이라고 부르며, 아래와 같은 순서로 이름을 찾아나갑니다.

(안에서부터 시작해서 바깥으로 조회해가는)

- `L`ocal scope: 정의된 함수

- `E`nclosed scope: 상위 함수

- `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈

- `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

```python
print = 'ssafy'
print(3)
```

1. `print()` 코드가 실행되면
2. 함수에서 실행된 코드가 아니기 때문에 `L`, `E` 를 건너 뛰고,
3. `print`라는 식별자를 Global scope에서 찾아서 `print = 'ssafy`'를 가져오고,
4. 이는 함수가 아니라 문자열이기 때문에 `not callable`하다라는 오류를 내뱉게 됩니다.
5. 우리가 원하는 `print()`은 Built-in scope에 있기 때문입니다.

```python
a = 10
b = 20 

def enclosed():
    a = 30
    
    def local():
        c = 40
        print(a,b,c)
        
    local() #이 코드의 의미??? 왜 없으면 enclosed()가 출력되지 않는거지??, 와 아직도 이해가 안간다
    a=50
```

```python
enclosed() #30,20,40 출력 
```

- 전역변수를 바꿔보자

```python
global_num = 3

def local_scope():
    global_num=5
    return f'global_num이 {global_num}으로 설정됐다'

print(local_scope())
print('global_num:', global_num)
```

> ```
> global_num이 5으로 설정되었습니다.
> global_num: 3
> ```

- 굳이 전역에 있는 변수를 바꾸고 싶다면, 아래와 같이 선언할 수 있습니다.

```python
global_num = 3
def local_scope():
    global global_num 
    #전역에 있는 함수를 끌고와서 건드릴수있게 
    #선언 후 다시 값을 설정해주는게 필요하다.
    global_num = 5
    return f'global_num이 {global_num}으로 설정되었습니다.'

print(local_scope())
print('global_num:', global_num)
```





## 재귀 함수

재귀 함수는 함수 내부에서 자기 자신을 호출 하는 함수를 뜻합니다.

알고리즘을 설계 및 구현에서 유용하게 활용됩니다.

### 팩토리얼 계산

> 팩토리얼은 1부터 n 까지 양의 정수를 차례대로 곱한 값이며 `!` 기호로 표기합니다. 예를 들어 3!은 3 * 2 * 1이며 결과는 6 입니다.
>
> `팩토리얼(factorial)`을 계산하는 함수 `fact(n)`를 작성하세요.
>
> n은 1보다 큰 정수라고 가정하고, 팩토리얼을 계산한 값을 반환합니다.



- 반복문을 이용한 팩토리얼 계산

```python
def fact(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

fact(5) #120 출력
```

- 재귀를 이용한 팩토리얼 계산

```
1! = 1
2! = 1 * 2 = 1! * 2 
3! = 1 * 2 * 3 = 2! * 3
```

```python
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

factorial(5) #120
```





## 반복문과 재귀함수

```python
factorial(3)
3 * factorail(2)
3 * 2 * factorial(1)
3 * 2 * 1
3 * 2
6
```

- 두 코드 모두 원리는 같다!

1. 반복문 코드
   - n이 1보다 큰 경우 반복문을 돌며, n은 1씩 감소한다.
   - 마지막에 n이 1이면 더 이상 반복문을 돌지 않는다.

1. 재귀 함수 코드
   - 재귀 함수를 호출하며, n은 1씩 감소한다.
   - 마지막에 n이 1이면 더 이상 추가 함수를 호출하지 않는다.

- 재귀함수는 기본적으로 같은 문제이지만 점점 범위가 줄어드는 문제를 풀게 된다.
- 재귀함수를 작성시에는 반드시, `base case`가 존재 하여야 한다.
- `base case`는 점점 범위가 줄어들어 반복되지 않는 최종적으로 도달하는 곳이다.
- 재귀를 이용한 팩토리얼 계산에서의 base case는 **n이 1일때, 함수가 아닌 정수 반환하는 것**이다.

- 자기 자신을 호출하는 재귀함수는 알고리즘 구현시 많이 사용된다.
- 코드가 더 직관적이고 이해하기 쉬운 경우가 있다.
- 팩토리얼 재귀함수를 [Python Tutor](https://goo.gl/k1hQYz)에서 확인해보면, 함수가 호출될 때마다 메모리 공간에 쌓이는 것을 볼 수 있다.
- 이 경우, 메모리 스택이 넘치거나(Stack overflow) 프로그램 실행 속도가 늘어지는 단점이 생긴다.
- 파이썬에서는 이를 방지하기 위해 1,000번이 넘어가게 되면 더이상 함수를 호출하지 않고, 종료된다. (최대 재귀 깊이)



## 피보나치 수열

첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열입니다.

(0), 1, 1, 2, 3, 5, 8

> 피보나치 수열은 다음과 같은 점화식이 있습니다.
>
> 피보나치 값을 리턴하는 두가지 방식의 코드를 모두 작성해주세요.

𝐹0=𝐹1=1F0=F1=1

𝐹𝑛=𝐹𝑛−1+𝐹𝑛−2(𝑛∈{2,3,4,…})Fn=Fn−1+Fn−2(n∈{2,3,4,…})

1) `fib(n)` : 재귀함수

2) `fib_loop(n)` : 반복문 활용한 함수

- 재귀를 이용한 코드

  ```python
  def fib(n):
      if n <= 1:
          return 1
      else:
          return(fib(n-1)+fib(n-2))
      
  fib(4)  #3출력
  ```

  

- 반복문을 이용한 코드

  ```python
  #1
  def fibonacci(num):
      f = [0, 1]
      for i in range(2, num + 1):
          f.append(f[i - 2] + f[i - 1])
      return f[num]
  print(fibonacci(3))
  ```
  
  ```python
  #2
  def fib(n):
      a, b = 1, 1
    if n == 1 or n == 2:
          return 1
      for i in range(n):
          a,b=b,a+b
      return a
  
  print(fib(5))
  ```
  
  

