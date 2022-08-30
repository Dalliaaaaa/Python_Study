# hight = int(input("키: "))
# result = (hight - 100) * 0.9

# print("제안: %.1fkg"% result)


for hight in range(150,181,3):
    result = (hight - 100) * 0.9
    print("키: %d cm, 제안: %.1f kg" % (hight, result))