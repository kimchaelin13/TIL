# #++++
# +#+++
# ++#++
# +++#+
# ++++#

#대각선으로 #을 만들어야한다.
#첫번째는  


# s = '#++++'
# print(s[-1:]+s[:-1]) #'+'
# #print(s[:-1]) #'#+++'

# print(s[-2:]) #'++'
# print(s[:-2]) #'#++'
# # for i in range(5):
# #     print(s[-i:]+s[:-i])

line='#++++'
for i in range(5):
    print(line[-i:]+line[:-i])
