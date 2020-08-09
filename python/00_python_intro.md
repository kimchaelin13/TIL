# Python 기초



## 1. 기초문법(Syntax)



- 파이썬 코드는 '1줄에 1문장'이 원칙이다.

- 기본적으로 파이썬에서는 `;`을 작성하지 않는다.

- 한 줄로 표기할때는 `;`을 작성하여 표기할 수 있다.

  
  
  ```python
  #파이썬 문법은 한 줄을 뛰어넘으면 다른 코드로 인식하기 때문에 아래 코드는 에러가 발생한다. 
  
  print("안녕
  나는
python이야")
  ```
  
  ```python
  #줄바꿈을 위해서는 ''',''' 이런식으로 많이 쓴다.
  
  print('''
  안녕
  나는 
  python이야
''')
  ```
  





## 2. 변수(Variable)



### 2-1 할당 연산자(Assignment Operator) : `=`



- 변수는 `=`을 통해 할당된다.

- 해당 데이터 타입을 확인하기 위해서는 `type=()`을 활용한다. 

- 해당 값의 메모리 주소를 확인하기 위해서는 `id()`를 활용한다.

  
  
  ```python
  #같은 값을 동시에 할당할 수 있다.
  x=y='happy'
  print(x)
print(y)
  
  >ssafy 
  >ssafy 
  ```
  
  ```python
  #다른 값을 동시에 할당 가능하다.
  a,b = 2020,4

  #아래와 같이 변수와 값이 대응되지 않으면 오류가 나타난다.
  a,b = 10,20,30
  a,b,c = 10,20
  ```
  
  ```python
  #변수 a와 b의 값을 바꿔볼 수 있다.
  a=10
  b=20
  
  a,b = b,a
  print(a)
  print(b)
  
  
  >20
  >10
  ```





### 2-2 식별자(Identifiers)



- 식별자의 이름은 영문알파벳(대문자와 소문자), 밑줄(_), 숫자로 구성된다.

- 첫 글자에 숫자가 올 수 없다.

- 길이에 제한이 없다.

- 대소문자(case)를 구별한다.

- 아래의 예약어는 사용할 수 없다.

  ```python
  [False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
  ```

- 내장함수나 모듈의 이름으로도 만들면 안된다.

  ```python
  #내장함수의 이름으로 사용하면 에러가 발생함.
  
  print = 'ssafy' #print를 변수의 이름으로 사용할수는 있지만
  print(print)    #print(print)하면 에러가 발생함
  
  #print은 이제 'hi'라는 값으로 인식되기 때문에 이전의 기능을 수행하지 못합니다
  ```





## 3. 데이터타입

> 숫자(number)타입, 글자(string)타입, 참/거짓(boolean) 타입



### 3.1 숫자(Number) 타입 



(1) `int`(정수, ingteger)

- 모든 정수는 `int`로 표현된다.

- 8진수:`0o` / 2진수:`0b`/ 16진수: `0x` 로도 표현 가능하다

  ```python
  binary_number=0b10
  print(binary_number) #2
  
  octal_number=0o10
  print(octal_number) #8
  
  hexadecimal_number = 0x10
  print(hexadecimal_number) #16
  ```

  



(2) `float`(실수, floating point number)

- 실수는 `float`로 표현된다. 다만, 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값으로 일치되지 않는다.(floating point rounding error) 

- 이는 컴퓨터가 2진수를 통해 숫자를 표현하는 과정에서 생기는 오류이며, 대부분의 경우에는 중요하지 않으나 값을 같은지 비교하는 과정에서 문제가 발생할 수 있다.

  ```python
  3.5 - 3.2 == 0.3 
  
  > False
  ```

  ```python
  round(3.5-3.2,2) == 0.3 #2번째 자리에서 반올림하겠다
  
  > True
  ```

- 두 개의 값이 같은지 확인해보자.

  ```python
  print(3.5-3.2)
  print(0.3)
  
  > 0.2999999999999998
  > 0.3
  ```

- 따라서 다음과 같은 방법으로 처리할 수 있다.

  ```python
  #1. sys 모듈을 통해 처리
  #1-1. 'epsilon'은 부동소수점 연산에서 반올림을 함으로써 발생하는 오차 상환
  
  import sys
  print(sys.float_info.epsilon)
  
  abs(a-b)
  
  >2.220446049250313e-16
   True
  ```

  ```python
  #2. math 모듈을 통해 처리
  
  import math
  
  num1 = 0.1*3
  num2 = 0.3
  
  #값 a와 b가 서로 가까이 있으면 True를, 그렇지 않으면 False를 반환합니다.
  math.isclose(num1,num2)
  
  >True
  ```



(3) `complex`(복소수, complex number)

- 각각 실수로 표현되는 실수부와 허수부를 가진다. 복소수는 허수부를 `j`로 표현한다. 

### 



### 3.2 문자(String) 타입

​	(1) 따옴표 사용

- 문자열 안에 문장부호(`'`,`"`) 가 사용될 경우 이스케이프 문자 (`\`)를 활용 가능하다.

  ```python
  "그의 이름은 \'ssafy\'였다"
  
  >'그의 이름은 'ssafy' 였다'
  ```

- 여러줄에 걸쳐있는 문장을 표현해보자

  ```python
  print("""
  이건 
  여러줄에 걸친
  문자열
  """)
  
  >이건 
  여러줄에
  걸친
  문자열
  ```



​		(2) 이스케이프 시퀀스 

| 예약문자 |   내용(의미)    |
| :------: | :-------------: |
|    \n    |     줄바꿈      |
|    \t    |       탭        |
|    \r    |   캐리지리턴    |
|    \0    |    널(null)     |
|   \\\    |        \        |
|   \\'    | 단일인용부호(') |
|   \\"    | 이중인용부호(") |

- 예시

  ```python
  print('안녕\n나는\n김채린이야')
  
  >안녕
  나는
  김채린이야
  ```

  ```python
  #end 옵션은 이스케이프 문자열이 아닌 다른 것도 조작 가능하다. 
  #end안에 기본 값은 '\n'임.
  
  print('hello, end='\t')
```
  
  ```python
  print('hello',end='\\')
  print('bye')
  #hello\bye
  ```
  
  

#### **String interpolation**

[`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 이후 버전에서 지원

- 활용

```python
name = '철수'
print(f'내 이름은 {name}입니다.')

>내 이름은 철수입니다. 
```

- f-strings에서는 형식을 지정할 수 있다. 

``` python
import datetime
now = datetime.datetime.now()

print(now)

>2020-07-20 02:22:38.719355

        
#interpolation에서 출력형식을 지정할 수 있습니다.
f'올해는 {now:%Y}년 이번달은 {now:%m}월 오늘은 {now:%d}일'

>'올해는 2020년 이번달은 07월 오늘은 20일'
```



### 3-3 참/거짓(Boolean) 타입

파이썬에는 `True`와 `False`로 이뤄진 `bool` 타입이 있습니다.

비교/논리 연산을 수행 등에서 활용됩니다.

다음은 `False`로 변환됩니다.

```
0, 0.0, (), [], {}, '', None
```

### `None` 타입

파이썬에서는 값이 없음을 표현하기 위해 `None` 타입이 존재합니다.



## 4. 형변환(Type conversion, Typecasting)

파이썬에서 데이터타입은 서로 변환할 수 있습니다.

- 암시적 형변환

- 명시적 형변환

  

### 암시적 형변환(Implicit Type Conversion)

> 사용자가 의도하지 않았지만, 파이썬 내부적으로 자동으로 형변환 하는 경우입니다. 아래의 상황에서만 가능합니다. 
>
> -bool
>
> -Numbers (int, float, complex)

- boolean과 integer는 더할 수 있을까? 

  ```python
  True + 3 #True는 1로 변환되서 계산됨 
  
  >4 
  
  False + 3 #False는 0으로 변환되서 계산됨 
  
  >3 
  ```

  ```python
  #없는 값에 3을 더하는 것은 불가능함
  
  result = None 
  result + 3
  
  >TypeError                                 Traceback (most recent call last)
  <ipython-input-135-44eda8b60f6d> in <module>()
        1 result = None
  ----> 2 result+3
  
  TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
          
          
  ```

  ### 명시적 형변환(Explicit Type Conversion)

  > 위의 상황을 제외하고는 모두 명시적으로 형 변환을 해주어야합니다.

  - string -> intger : 형식에 맞는 숫자만 가능
  - integer -> string : 모두 가능

  > 암시적 형변환이 되는 모든 경우도 명시적으로 형변환이 가능합니다.

  - `int()` : string, float를 int로 변환

  - `float()` : string, int를 float로 변환

  - `str()` : int, float, list, tuple, dictionary를 문자열로 변환

    

- integer와 string 사이의 관계는 명시적으로 형변환을 해줘야만 한다.

  ```python
  str(1)+'등'
  
  >'1등'
  ```

- string 3을 integer로 변환해보자

  ```python
  number = int(input('숫자를 입력하세요:'))*2
  
  print(number)
  ```

- int('3.5')를 타이핑하면 오류가 난다.
- int(float('3.5')) 이렇게 해야 int인 3으로 형변환이 일어난다.

## 5. 연산자(Operator)

- 산술 연산자

- 비교 연산자

- 논리 연산자

- 복합 연산자

- 기타 연산자

  

### 5.1 산술 연산자

| 연산자 |      내용      |
| :----: | :------------: |
|   +    |      덧셈      |
|   -    |      뺄셈      |
|   *    |      곱셈      |
|   /    |     나눗셈     |
|   //   |       몫       |
|   %    | 나머지(modulo) |
|   **   |    거듭제곱    |

- `divmod`는 나눗셈과 관련된 함수이다.

```python
a,b=divmod(5,2)
print(a) #2
print(b) #1
```



### 5.2 비교 연산자

우리가 수학에서 배운 연산자와 동일하게 값을 비교할 수 있습니다.

|  연산자  |          내용          |
| :------: | :--------------------: |
|   `<`    |          미만          |
|   `<=`   |          이하          |
|   `>`    |          초과          |
|   `>=`   |          이상          |
|   `==`   |          같음          |
|   `!=`   |        같지않음        |
|   `is`   |    객체 아이덴티티     |
| `is not` | 부정된 객체 아이덴티티 |

```python
3 == 3.0 #True
3.0 == 3.0 #True
```



### 5.3 논리 연산자

우리가 보통 알고 있는 `&` `|`은 파이썬에서 비트 연산자입니다.

| 연산자  |             내용             |
| :-----: | :--------------------------: |
| a and b |   a와 b 모두 True시만 True   |
| a or b  | a 와 b 모두 False시만 False  |
|  not a  | True -> False, False -> True |

- 파이썬에서 and는 a가 거짓이면 a를 리턴하고, 참이면 b를 리턴한다.
- 파이썬에서 or은 a가 참이면 a를 리턴하고, 거짓이면 b를 리턴한다.



#### *단축평가

> 포인트는 누가 키플레이어인지이다.

- 첫 번째 값이 확실할 때, 두 번째 값은 확인 하지 않음

- 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상

- and/or를 포함한 식에서

- 먼저 연산자 양쪽이 bool로 형변환이 일어난다.

- true or true 이런식으로 변함

- and 경우에는 첫번째 항목이 false일 경우, 두번째 항목과 관련없이 무조건 결과는 false!

  (and는 둘다 참이여야 참이기 때문)

- 첫번째 항목을 다시 원래대로 형변환한 결과를 돌려준다.

- 첫번째 항목이 true인 경우 두번째 항목도 살펴봐야 총 결과를 알 수 있으므로, 두번째 항목이 키플레이어가 된다.

```python
vowels = ['a','e','i','o','u']

'a' or 'b' 
#a 출력, or 같은 경우는, 앞에 있는게 true면 뒤를 볼 필요없이 true

'a' and 'b' 
#b 출력, and 같은 경우는 앞이 참이라도 뒤에까지 참이여야 참이기 때문에 b까지 봐야함. 따라서 b를 출력

False or 'b' 
#b 출력, or는 앞이 false더라도 뒤에가 트루면 트루를 반환하기 때문에 b를 출력

False and 'b'
#False 출력, 뒤에 볼 필요도 없이 앞이 이미 False이기 때문에 False 반환

```



and와 or의 돌아가는 방향이 다름.

- `and` 는 둘 다 True일 경우만 True이기 때문에 첫번째 값이 True라도 두번째 값을 확인해야 하기 때문에 'b'가 반환된다.
- `or` 는 하나만 True라도 True이기 때문에 True를 만나면 해당 값을 바로 반환한다.



### 5.3 복합 연산자

복합 연산자는 연산과 대입이 함께 이뤄집니다.

가장 많이 활용되는 경우는 반복문을 통해서 개수를 카운트하거나 할 때 활용됩니다.

| 연산자  |    내용    |
| :-----: | :--------: |
| a += b  | a = a + b  |
| a -= b  | a = a - b  |
| a *= b  | a = a * b  |
| a /= b  | a = a / b  |
| a //= b | a = a // b |
| a %= b  | a = a % b  |
| a **= b | a = a ** b |



- 활용

  ```python
  cnt = 0
  while cnt<5:
    print(cnt)
    cnt += 1 #오른쪽항을 왼쪽에 대입
  
  ```

  