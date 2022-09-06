# for x in range(1,11,1):
#     if x%3==0:
#         continue
#     print(x)

# for y in range(1,11,1):
#     print(y)
#     if y%5==0:
#         break

z=1
while z <= 10:
    print("Hello: ",z)
    if z % 3 == 0:
        break #while문을 빠져나감
    z += 1
else :
    print("성공 반복완료")