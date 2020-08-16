import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
# for tc in range(1, T + 1):
#     nums = set()
#     a = int(input())
#     n = a #1을 n에 넣는다.
#     while len(numbers) < 10:
#         for i in str(n):
#             numbers.add(i)
#             if len(numbers) == 10:
#                 print('#{} {}'.format(tc, n))
#                 break
#
#         n += a #n=n+a, n에 a를 더한다!,이게 배수임,

T = int(input())
for test_case in range(1,T+1):
    nums=set()
    a=int(input())
    cnt=1
    while len(nums) < 10:
        n = cnt * a
        for i in str(n):
            nums.add(i)
            if len(nums) == 10:
                print('#{} {}'.format(test_case, cnt))
                break
        cnt+=1
