#For
n = int(input("몇 부터 더할까요? "))
m = int(input("몇 까지 더할까요? "))
res = 0

if n >= m:
     print("시작하는 수가 끝나는 수보다 크거나 같으면 안됩니다.")

else:
    for res in range (n,m,1):
        res += n
    print("%d부터 %d까지 더한 값은 %d입니다."% (n, m, res))
