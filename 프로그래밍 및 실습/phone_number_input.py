#is_phone_num.py
#isdigit : 숫자로만 이루어져 있는가
#isalpha : 문자로만 이루어져 있는가
#startswitch : ~~로 시작하는가
#endswitch : ~~로 끝나는가

def main():
  pnum = input("휴대폰 번호 입력: ")
  if pnum.isdigit() and pnum.startswith("010"):
    print("정상적인 입력입니다.")
  else:
    print("정상적이지 않은 입력입니다.")

main()
