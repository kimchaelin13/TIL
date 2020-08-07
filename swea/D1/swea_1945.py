
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in reversed(range(T+1)):
    print(i, end=' ')
