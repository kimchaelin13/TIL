

import sys
sys.stdin = open("input.txt", "r")

sentence=input()
#'_'를 기준으로 나눠서 리스트에 각각 저장함
#그리고 리스트를 읽으면서 대문자로 upper() 다시 새로운 리스트에 저장
#그리고 ,을 기준으로 _ 합쳐줌 join 

a=sentence.split('_')
#print(a)
b=[]
c=''
for i in a:
    b.append(i.upper())
#print(b)

c+="_".join(b)
print(c)

