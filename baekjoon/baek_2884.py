'''
알람
'''
h, m = map(int,input().split())
min=m-45
if min>0:
    print(h,min)

elif min<0:
    min=min+60
    h=h-1
    if h < 0:
        h=h+24
        print(h,min)

