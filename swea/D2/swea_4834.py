#숫자 카드

#5
#49679
#result=[4,9,6,7,9]로 만들어주고,
#count는 [0]*len(result)를 만들어주고
#result를 읽으면서 count[result[i]] +=1 해서 카운트를 완성시킨다.
import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1,int(input())+1): #1,2,3

    LEN=int(input())
    count = [0]*10
    nums = list(map(int,input()))
    #print(nums)

    for i in range(len(nums)):
        count[nums[i]] += 1

    print(count)

    max_index=0
    max_num=0

    for i in range(len(count)-1,-1,-1):
        if count[i] > max_index:
            max_index = count[i]
            max_num= i

    print(f'#{test_case} {max_num} {max_index}')
