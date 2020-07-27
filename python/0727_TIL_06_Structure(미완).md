# 0727_TIL

- Data Structure



# 데이터 구조(Data Structure) 

데이터 구조(Data Structure)란 데이터에 편리하게 접근하고, 변경하기 위해서 데이터를 저장하거나 조작하는 방법을 말한다. 

- 알고리즘에 빈번히 활용되는 순서가 있는(ordered) 데이터 구조

  - 문자열(String)
  - 리스트(List)

- 데이터 구조에 적용 가능한 Built-in Function

  - `map()`
  - `filter()`

  

두가지가 중요하다. 뭐가 들어와서 나가는지를 정의하기 위해 함수를 쓰는데, 여기서 중요한건 뭐를 집어넣을 수 있고, 어떤 것이 나오는지가 중요하다.

for more detail, 어떤 값을 자유롭게 넣을 수 있고(가변인자리스트,args) 더 중요한건 아웃풋파트에서 return값이 있는지! 값을 반환하는건지 아니면 원본 데이터를 수정하는지!

대부분 원본 데이터를 수정하는 코드들은 리턴값이 없는 경우가 많다.



## 문자열(String)

변경불가(immtable), 순서 있고(ordered), 순회 가능(iterable)

순서가 있으면 무조건 순회가능함

#### 

### (1) 조회/탐색

`.find(x)`

x의 첫번째 위치를 반환한다. 없으면 `-1`을 반환한다. 

```python
'apple'.find('p') #1 리턴
```

`.index(x)`

x의 첫번째 위치를 반환한다. 없으면 오류가 발생한다.

```python
'apple'.index('k') 
#ValueError: substring not found

#그런데 'apple'.find('f')은 -1을 반환해줌
```

- 핸들링을 해보자

  ```python
  try:
      'apple'.index('k')
      
  except ValueError:
      print('해당하는 값이 없습니다')
  ```



### (2) 값 변경

`.replace(old,new[,count])`

바꿀대상을 새로운 글자로 바꿔서 반환환다. count를 지정하면 해당 갯수만큼만 시행한다. 

이 함수는 리턴값이 있는 함수다

```python
#
result = 'yay!'.replace('a', '_')
print(result) 

#리턴 값이 있다면, result라는 변수에 담고 그걸 실행하면 결괏값이 있으면 리턴을
#하는 함수구나
#replace()는 return값이 있구나
```



`.strip([chars])`

특정한 문자들을 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip), 오른쪽을 제거합니다(rstrip). 지정하지 않으면 공백을 제거합니다.

```python
'    oh!\n'.strip() #아무것도 안넣으면 공백제거, 'oh!'반환
```

```python
'hehehihihihihi'.rstrip('hi') #hi라고 되어있는 패턴을 다 지움
#hehe 반환
```



`.split()`

문자열을 특정한 단위로 나누어 **리스트**로 반환합니다.

```python
#
'a_b_c'.split('_')
#리턴값이 있다.
#리턴값의 타입은 리스트
#split은 글자를 쪼개서 리스트를 반환한다. 
```

```
['a', 'b', 'c']
```



`'seperator'.join(iterable)`

특정한 문자열로 만들어 반환합니다.

반복가능한(iterable) 컨테이너의 요소들을 separator를 구분자로 합쳐(`join()`) **문자열**로 반환합니다.

```python
word = '배고파'

words = ['안녕', 'hello']

'!'.join(word)  #'배!고!파!'

' '.join(words) #'안녕 hello'
```



- 이 밖에도 문자변형 함수가 있는데 나중에 추가해야지





##  리스트(list)

변경 가능하고(mutable), 순서가 있고(ordered), 순회 가능한(iterable) 리스트는 변경가능함. str는 변경불가하다. 변경하면 새로운게 튀어나온다. 

리스트는 변경가능하기 때문에, 원본을 변경하는 애와 원본을 변경하지 않는애랑 크게 둘로 나뉘게 됨. 

원본 변경하는 건 `return None`인 경우가 많고, 원본 변경 x는 변경된 데이터가 return되게끔 되어 있다. 이 둘 차이가 매우매우 중요합니다.



### (1) 값 추가 및 삭제

`.append(x)`: 리스트에 값을 추가할 수 있다

```python
# 카페 리스트를 만들어봅시다.
cafe = ['starbucks', 'tomntoms', 'hollys']
print(cafe)

cafe.append('banapresso')
print(cafe) #변경값 없음

new_cafe = cafe.append('banapresso')
print(new_cafe) #그레서 이게 안됨
```

#원본을 조작하고, 리턴값이 없는 함수구나

`.extend(iterable)`

리스트에 iterable(list, range, tuple, string**[주의]**) 값을 붙일 수가 있습니다.

.append()는 ()안에 값이 들어간다. .extend()는 [1,2,3]+[4,5,6] > [1+2+3+4+5+6] 와 같다.

~~**이거 append랑 뭐가 다른지 비교하는거 추가해놓기**~~