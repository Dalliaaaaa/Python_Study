hight = float(input("키가 몇 cm에요? "))
proper = ( hight - 100 ) * 0.9
over_danger = proper * 1.2
low_danger = proper * 0.8

print("당신의 신장 : ", hight)
print("적정 몸무게 : ", proper)
print("과체중 위험 몸무게 : ", over_danger)
print("저체중 위험 몸무게 : ", low_danger)