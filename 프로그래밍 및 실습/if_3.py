# def main():
#   num = int(input("정수 입력: "))
#   if num % 2 == 0:
#     if num % 3 ==0 :
#       print("OK!")
#     else:
#       print("NO!")
#   else:
#     print("NO!")

def main():
  num = input("입력: ")
  if (num % 2) == 0 and (num % 3) == 0:
    print("OK!")
  else:
    print("NO!")

main()
