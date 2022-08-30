#연필과 펜의 갯수를 입력하고 총액에 30%를 할인한 가격
# num_pencil = int(input("연필은 몇 개를 구입하시겠습니까? "))
# num_pen = int(input("펜은 몇 개를 구입하시겠습니까? "))

# total_price = (num_pencil * 3000) + (num_pen * 4000)
# price = 0.7 * total_price

# print("총 가격은 %.1lf 원 입니다." %price)


#총액이 20,000원이 넘으면 10% 할인
pencil = 2000
pen = 3000
num_pencil = int(input("연필 개수 입력: "))
num_pen = int(input("펜 개수 입력: "))

total_price = num_pencil * pencil + num_pen * pen

if total_price > 20000 :
    total_price *= 0.9
    print("할인되었습니다.")

print("총합 %.1lf원" %total_price)