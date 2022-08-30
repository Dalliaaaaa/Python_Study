current_time = int(input("지금 몇시인가요? "))
before_time = current_time - 6

if before_time <= 0 :
    before_time = current_time + 18

print("현재 시간 : %d시" %current_time)
print("이전 시간 : %d시" %before_time)