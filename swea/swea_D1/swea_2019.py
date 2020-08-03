

import sys
sys.stdin = open("input.txt", "r")

#주어진 숫자가 8임
#2의 0승, 2의 1승, 2의 8승까지 곱해야함
#range(8+1)로 곱해줌, 리스트 뽑으세염~

T = int(input())
for i in range(T+1):
    print(2**i,end=' ')



