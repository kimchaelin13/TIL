def fib(n):
    a, b = 1, 1
    if n == 1 or n == 2:
        return 1
    for i in range(n):
        a,b=b,a+b
    return a

print(fib(5))


def fibonacci(num):
    f = [0, 1]
    for i in range(2, num + 1):
        f.append(f[i - 2] + f[i - 1])
    return f[num]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))