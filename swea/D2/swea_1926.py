# 10



# for i in range(1,int(input())+1):
#     a = ['-' for i in str(i) if i == '3' or i == '6' or i == '9']

#     if a:
#         print(''.join(a),end=" ")
#     else:
#         print(i,end=" ")
        

a=['-' for i in range(1,int(input())+1)) if i % 3 == 0]
if a:
    print(''.join(a),end=' ')
else:
    print(i,end= " ")
