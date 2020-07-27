# 0728_TIL

> 오늘 배운 것들을 정리합니다.
>
> - Error
> - Data Structure



## 1. 에러와 예외처리

> 에러는 크게 두가지이다. 문법 에러(Syntax Error) 와 예외 에러(Exception)



## 1-1 에러

###  문법에러(Syntax Error)

- 문법 에러가 있는 프로그램은 실행되지 않는다. 

- if문에서 `:`를 쓰지 않았을때 `SyntaxError: invalid syntax` 가 뜬다

- 또는 `print('hi)`처럼 str을 열어놓고 닫지 않았을때는 `SyntaxError: EOL while scanning string literal` 에러문이 뜬다.

  `EOL`는 end of line이다. 파이썬은 문자열이 열리면 닫히기를 기대하는데, 닫히지 않은 것임. EOL을 보면 코드 어디선가 str을 닫지 않은 것이다.

- `print('hi'` 를 입력하면, 에러코드가 `SyntaxError: unexpected EOF while parsing` 이 뜬다. `EOF`는 end of file이다. 닫는 괄호를 찾으려고 하는데, 닫는 괄호가 없다. 파싱을 하는 도중에 파일이 끝나버렸다고 하는 에러라고 해석하면 된다. 



### 예외(Exception)

- 실행 도중 예상하지 못한 상황(exception)을 맞이하면, 프로그램 실행을 멈춘다. 
- 문법적으로는 맞지만 실행시 발생하는 에러이다



#### (1) ZeroDivisionError : 0으로 나눌 수는 없습니다.

- 만약 `10*(1/0)` 이라는 코드를 실행하면, `ZeroDivisionError`가 발생한다.
- 문법상으로는 맞지만 컴퓨터가 처리할 수 없다.



#### (2) NameError : 정의되지 않은 변수를 호출했을때 

- 지역 혹은 전역 이름 공간내에서 유효하지 않은 이름



#### (3) TypeError : 자료형에 대한 타입 자체가 잘못되었을때 

- `1+'1'`과 같이 데이터 타입이 다른 것에 대한 연산을 실행했을때

- `round('3.5')` : round()는 반올림해주는 함수이다, which means ()안에는 숫자(int,float)가 들어가야 한다. 

- 필수 argument를 누락했을때/ argument 개수 초과했을때

  (이건 아직 뭔지 잘 모르겠다)

  

#### (4) ValueError : 자료형에 대한 타입은 올바르나 값이 적절하지 않는 경우

- int('3.5') : int()안에 글자를 넣는 것은 맞으나 3.5는 안된다. float타입이기 때문임

- 또는 numbers=[1,2] 인데 numebrs.index(3) 처럼 존재하지 않는 값을 찾고자 할때

  ```python
  # 존재하지 않는 값을 찾고자 할 경우
  numbers = [1, 2]
  numbers.index(3) #에러발생
  ```

  ```python
  # 존재하지 않는 값을 찾고자 할 경우
  numbers = [1, 3]
  numbers.index(3) #1 출력, 이건 왜지???? 
  ```

  

#### (5) KeyError : dict에서 key가 없는 경우



#### (6) ModuleNotFoundError : 모듈을 찾을 수 없는 경우



## 1-2 예외처리

> try , except 문을 이용해서 예외처리를 할 수 있다. 



#### 활용법

```python
try:
    <코드 블럭 1> #이 코드를 먼저 시도해보는 것, 
                  #이 코드는 오류,예외가 발생할 확률 높은 코드임
except (예외):
    <코드 블럭 2> #예외가 발생하면, 코드블럭2를 실행하라
```

- `try` 아래의 코드블락(code block)이 실행된다.
- 예외가 발생되지 않으면, **`except`없이 실행이 종료 된다.**
- 예외가 발생하면, **남은 부분을 수행하지 않고**, `except`가 실행된다.



**[예시]**

```python
#사용자로부터 값을 받아 정수로 변환하여 출력한다. 

#
num = input('숫자를 입력하시오 : ') 
#사용자로부터 입력받은 값은 str으로 나옴
print(int(num))
print(num/2)

#사용자가 숫자가 아닌 '백'같이 다른 것을 입력하면 에러가 뜬다
```

- 예외 처리를 해보자

```python
#
try:
    num = input('값을 입력하시오 : ') #일단 코드블록을 시도한다
    print(int(num))
    
except:
    print('숫자를 다시 입력해주세요:')
    num = input('값을 입력하시오 : ')
    print(int(num))    #위에서 에러가 나는 순간,에러를 내는 대신
```



#### (1) 예외 메시지 처리 `as`

> 에러 메시지를 넘겨줄 수도 있다. 



#### 활용법[¶](http://localhost:8891/notebooks/05_error_exception.ipynb#활용법)

```python
try:
    <코드 블럭 1>
except 예외 as err:
    <코드 블럭 2>
```

```python

try: 
    empty_list = [] #빈 리스트
    print(empty_list[-1]) #인덱스가 없는데? which is index error
    
except IndexError as error: 
    #인덱스에러라고 하면 나오는 에러메세지가 그대로 as뒤에 'error'에
    #저장되고, as구문을 통해서
    #error message를 그대로 deliever 가능
    print(error)
```

> list index out of range라는 에러메시지가 그대로 출력된다.



#### (2) 복수의 예외처리

하나 이상의 예외를 모두 처리할 수 있다. 괄호가 있는 튜플로 여러 개의 예외를 지정할 수 있습니다.



#### 활용법

```python
#예외가 두개라도 하나로 처리할 수밖에 없는 반면
try:
    <코드 블럭 1>
except (예외1, 예외2):
    <코드 블럭 2>


#상세하게 구분 가능함 
    try: 
    <코드 블럭 1>
except 예외1:
    <코드 블럭 2>
except 예외2:
    <코드 블럭 3>
```



100을 사용자가 입력한 값으로 나눈 후 출력하는 코드를 작성해보자. 발생할 수 있는 에러를 예측해보면, 형변환 에러가능성(value error), 그리고 0으로 나눌 수 없기 때문에 zerodivsionerror 2개이다.

```python
try:
    num=input('100으로 나눌 값을 입력하시오:')
    print(100/int(num))

except (ValueError, ZeroDivsionError):
    print('무언가가 잘못되었습니다')
```

#만약 숫자가 아닌 str이나 0을 입력하면 `무언가가 잘못되었습니다`가 실행된다. 

아래처럼 각각 다른 오류를 출력할 수 도 있다.

```python

try:
    num = input('100으로 나눌 값을 입력하시오: ')
    100/int(num)
    
except ValueError:
    print('글자가 아닌 숫자를 입력해주세요')

    
except ZeroDivisionError:
    print('0으로는 나눗셈을 할 수 없습니다')
```



중요한건 에러가 순차적으로 수행되므로, 가장 작은 범주부터 시작해야 한다. 아레 예를 보면 이해가 쉽다.

```python
#
try: 
    num = input('100으로 나눌 값을 입력하시오: ')
    100/int(num)
    
except Exception: #다 커버가능한 매우 큰 범주
    print('에러가 났어요')
    
except ValueError:
    print('글자가 아닌 숫자를 입력해주세요')

    
except ZeroDivisionError:
    print('0으로는 나눗셈을 할 수 없습니다')
```

만약 사용자가 0을 입력하면 '0으로는 나눗셈을 할 수 없습니다'가 아닌 더 큰 범주인 첫번째 except를 실행하고, 에러가 났어요를 출력한다. 



#### (3) else

- 에러가 발생하지 않는 경우 실행 시킬 문장은 `else`를 활용한다.
- `else`는 `except` 코드 뒤에 와야 한다.
- `try` 코드 블럭이 예외를 일으키지 않았을 때, 실행되어야 하는 코드에 사용된다.

#### 활용법

```python
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
else:
    <코드 블럭 3>
```



- for-else와 비슷하다. for else는 반복문이 다 끝나면 실행된다. 이건 try코드가 다 실행됐을때 else뒤에 실행된다. 

  

```python
#
try:
    numbers = [1, 2, 3]
    number = numbers[2]

except IndexError:
    print('오류 발생') #만약 오류가 발생하지 않는다면??
    
else:
    print(number) #try안에 코드가 잘 돌아갔을때 성공적일때 실행
```



#### (4) finally

- 어떤 경우에든 반드시 실행해야하는 코드에는 `finally`를 활용한다.
- 즉, 모든 상황에 실행되어야만 하는 코드를 정의하는데 활용한다.
- 예외의 발생 여부과 관계없이 항상 실행된다.

#### 활용법

```python
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
finally:
    <코드 블럭 3>
```

```python
#
try:
    languages = {'python': 'good'}
    languages['java'] 
except KeyError as err:
    print(f'{err}는 딕셔너리에 없는 키입니다.')
    
finally:
    print('감사합니다') #잘되든 아니든, 감사해야하니까, ㅋㅋ
                        #exception으로 넘어간 경우
```



#### (5) 예외 발생시키기

`raise`를 통해서 예외를 강제로 발생시킬 수 있다. 

#### 활용법

```python
raise <에러>('메시지')
```

`assert`를 통해서도 예외를 발생시킬 수 있다. 보통 상태를 검증하는데 사용되고 무조건 AssertionError가 발생한다. 



**활용법**

```python
assert Boolean expression, error message

assert type(1) == int, '문자열을 입력하였습니다.'
```

------

위의 검증식이 거짓일 경우를 발생합니다.

`raise`는 항상 예외를 발생시키고, 지정한 예외가 발생한다는 점에서 다릅니다.