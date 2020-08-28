## 재귀함수와 스택

재귀함수 : 반복문의 효과, 반목문의 대체제, 3중 for문으로 하기는 유연성이 떨어지는 것들을 재귀함수를 이용해서 풀면 유용성을 향상시킬 수 있다.

- n이 입력되면 

```python
import sys
sys.stadin = open('input.txt','r')

def DFS(x): #n값을 x라는 지역변수로 받는다
    print(x)
    
    if x>0: #if문없으면 영원히 출력
        DFS(x-1)#x에서 1이 감소된 값이 새로운 함수의 매개변수로 값이 전달됨
    	print(x,end="")
    
    
if __name__=="__main__":
    n=int(input())
    DFS(n) #n을 받았으니까 n을 넘기는걸로, 함수호출
    
    
```

```python
n=3 
3
2
1
0
-1
-2
(...) 계속 무한히 돈다
```

```PYTHON
1
2
3
```