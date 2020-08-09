## 1st week_리뷰



### 단어 뒤집기

> 입력으로 짧은 영어 단어 word가 주어질때, 해당 단어를 역순으로 뒤집을 결과를 출력하시오.

```python
words=input()
words_reversed = '' #역순 string을 저장할 빈string

for word in words:
    words_reversed = word+words_reversed
    
print(words_reversed)
```

words_reversed = word+words_reversed 

- 출력 방식에 대해 헷갈려서 볼때마다 헷갈려서 출력을 다시 해봤다.

```python
words = input() #apple을 입력함
words_reversed=''

for word in words:
    words_reversed = word + words_reversed 
    #'a'='p'+'a'
    #'pa'='p'+'pa'
    #'ppa'='l'+'ppa'
    #'lppa'='e'+'lppa'
    #elppa
    print(words_reversed)
```

```python
apple #apple을 입력함
a 
pa
ppa
lppa
elppa
```



### 최댓값과 등장 횟수 구하기

> 주어진 리스트의 요소 중에서 최댓값과 등장 횟수를 출력하시오.
>
> [출력 예시]
>
> 22 3

```python
numbers = [7, 10, 22, 7, 22, 22]
max_num = numbers[0]
cnt = 0

for number in numbers:
    if max_num < number: #설정된 최댓값보다 큰 값을 만나면 
        max_num=number #그 값으로 최댓값을 초기화한다.
        cnt=1 #그리고 카운트도 1로 초기화한다.
        
    if max_num == number: #최댓값과 같은 숫자가 있으면
        cnt += 1  #cnt에 1을 더해준다. 
        
print(max_num, cnt)
```

- ??? 궁금한 점 : if 문이 두개가 있는데 첫번째 if문을 다 돌고, 그 다음에 두번째 if문을 시작하는건가? 

  numbers를 끝까지 돌면서 max_num을 찾고, 마지막 숫자인 22에서 cnt를 1로 초기화하고,

  그다음 if문에서 다시 이미 찾은 22라는 max_num과 같은 number가 있으면 카운트를 하나씩 올라가는 식인가??? 



### 더블더블 

> 자연수 number을 입력받아 1부터 주어진 자연수 number까지 홀수는 2, 짝수는 3을 곱한 값을 출력하시오

```python
number = int(input())

total = 0

for i in range(1,number+1): #1부터 그 넘버까지 하나씩 해야하므로 범위 range로 for문을 돈다
    if i % 2==0: #i가 짝수이면
        total += i*2 #total에 i*2를 더해주세요
        
     else:
        total += i*3
        
        
print(total)
```



### 간단한 소수 판별 

> 조건, 반복문을 응용하여 numbers 리스트의 요소들이 소수인지 아닌지 판단하는 코드를 작성하시오.

------

```
[출력 예시]
26은(는) 소수가 아닙니다. 2은(는) 26의 인수입니다.
39은(는) 소수가 아닙니다. 3은(는) 39의 인수입니다.
51은(는) 소수가 아닙니다. 3은(는) 51의 인수입니다.
53은(는) 소수입니다.
57은(는) 소수가 아닙니다. 3은(는) 57의 인수입니다.
79은(는) 소수입니다.
85은(는) 소수가 아닙니다. 5은(는) 85의 인수입니다
```

```python
numbers = [26, 39, 51, 53, 57, 79, 85]

# 아래에 코드를 작성하시오.

for number in numbers:
    for i in range(2,number):
        if number%i == 0:
            print(f'{number}는 소수가 아닙니다.{i}는 {number}의 인수입니다')
            break
            
    else:
        print(f'{number}는 소수입니다.')
```



### all() 직접 구현하기

> `all()`은 인자로 받는 iterable(range, list)의 모든 요소가 참이거나 비어있으면 True를 반환합니다.
>
> 파이썬 내장 함수 `all()`을 직접 구현한 `my_all()`을 작성하시오.

```python
def my_all(elements):
    result = True #초기값이 True고, 하나라도 False면 False반환
    for element in elements:
        if bool(element)==False: #하나라도 false면
            result = False #False를 반환하고
            break #for문을 탈출한다
    return result  

print(my_all([1, 2, 5, '6']))
```



### any() 직접 구현하기

> `any()`는 인자로 받는 iterable(range, list)의 요소 중 하나라도 참이면 True를 반환하고, 비어있으면 False를 반환합니다.
>
> 파이썬 내장 함수 `any()`을 직접 구현한 `my_any()` 함수를 작성하시오.

1. 초기값을 false로 지정한다.
2. 그리고 for문을 통해서 하나씩 돌다가, 하나라도 참이면true를 반환하고 반복문을 탈출한다.

```python
def my_any(elements):
    result = False
    for element in elements:
        if bool(element) == True:
            result = True
            break
            
    return result

my_any([1, 2, 5, '6'])
```



### 자릿수 더하기

> 자연수 number를 입력 받아, 각 자릿수의 합을 계산하여 출력하시오.

- number을 문자열로 바꾼다
- 문자열로 바꾸면 for문으로 돌릴 수 있으니까 하나하나 읽어주면서 더해주는데 그때 다시 int형으로 바꿔서 더해준다.

```python
def sum_of_digit(number):
    
    number_str = str(number)
    sum = 0
    
    for i in number_str:
        sum = sum+int(i)
        
    return sum

sum_of_digit(4321) #10 반환 
```

- 이 밖에도 재귀함수를 이용하는 방법이 있는데 이건 아직 잘 모르겠다. 보충학습이 필요함

```python
def sum_of_digit(number):
    #sod(4321) => 1+sod(432) => 1+2+sod(43) => 1+2+3+sod(4) => 1+2+3+4
    
    if number < 10:
        return number
    
    else: 
        remainder = number % 10
        number = number//10
        return remainder+sum_of_digit(number)

    
sum_of_digit(4321) #10 반환 
```



![]()![image-20200726022312682](C:\Users\kimch\AppData\Roaming\Typora\typora-user-images\image-20200726022312682.png)

```python
def list_sum(list):
    sum = 0 #sum=0초기화
    for i in list: #하나의 리스트의 원소를 하나씩 돌면서 
        sum += i #sum변수에 원소i를 하나씩 더해준다.
    return sum

list_sum([1,2,3])  #6반환 
```



![]()![image-20200726022541060](C:\Users\kimch\AppData\Roaming\Typora\typora-user-images\image-20200726022541060.png)

- 일단 예제는 리스트로 이루어져 있음
- 계속 dict 접근이 다른 컨테이너 타입에 비해 헷갈린다.

```python
a = [{'name':'kim','age':12},{'name':'Lee','age':14}]

type(a) #list

for i in a:
    print(i)

```

```
{'name': 'kim', 'age': 12} 
{'name': 'Lee', 'age': 14}
```

```python
for i in a:
    i['age'] #dict 형태로 이루어진 원소 i의 'age'(키값)입력하면 value값에 접근가능
    print(i)
    
```

```
12
14
```

- 최종 코드

```python
def dict_list_sum(list):
    sum = 0
    for i in list:
        sum += i['age']
     return sum


dict_list_sum([{'name':'kim','age':12},{'name':'Lee','age':14}]) #26출력

```

![]()![image-20200726023332554](C:\Users\kimch\AppData\Roaming\Typora\typora-user-images\image-20200726023332554.png)

```python
def all_list_sum(list):
    sum = 0
    for i in list: #리스트안의 원소를 하나씩 돌면서(근데 그 안에 i도 리스트로 되있어서 이중 for문)
        for j in i: #i원소 안에 있는 원소 j를 모두 더함.
            sum += j
     return sum
            
```



### 계단 만들기
>  자연수 number 를 입력 받아 , 아래와 같이 높이가 number 인 내려가는 계단을 출력하시오
>
> [입력 예시]
> 4
> [출력 예시]
> 1
> 1 2
> 1 2 3
> 1 2 3 4

```python
number = int(input('숫자를 입력하라:'))


for i in range(1,number+1):
    for j in range(1,i+1):
        print(j, end= ' ')
    print()
```

- 이거 계속 헷갈린다. 이중 for문이 어떤 문제는 이해가 되고 어떤 문제는 간단한데도 계속 헷갈린다.....