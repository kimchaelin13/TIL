# 0802 SWEA_REVIEW

> D1 거꾸로 출력해 보아요



## SWEA_1945

> 입력 8
>
> 출력 8 7 6 5 4 3 2 1 0

```python
T = int(input())

for i in reversed(range(T+1)):
    print(i, end=' ')
```

- `reversed(range(T+1))` 을 사용해서 원래는 0,1,2,3,,8 인데 숫자를 뒤집어서 8,7,6,,0까지 출력해준다.



## SWEA_2027

> 아래와 같이 출력하는 문제
>
> #++++
> +#+++
> ++#++
> +++#+
> ++++#

```python
line='#++++'
for i in range(5):
    print(line[-i:]+line[:-i])
```

- 문자열을 [-1:] 이렇게 slicing 하는게 어색하다. 
- 쪼개서 연습!

```python
print(line[0:]) #'#++++'
print(line[:0]) #''

print(line[-1:]) #'+'
print(line[:-1]) #'#+++'

print(line[-2:]) #'++'
print(line[:-2]) #'#++'
```

