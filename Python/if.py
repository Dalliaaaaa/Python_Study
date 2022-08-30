print("===짝수 홀수 판별 프로그램===")
num = int(input("정수를 입력하세요: "))

if num <= 0 : 
    print("판별할 수 없는 수를 입력하셨습니다.")
    print("양의 정수만 짝수/홀수 판별 가능합니다.")

else :
     print("정수 %d를 입력했군요." %num)
     if num % 2 == 0 :
        print("당신이 입력한 수는 짝수입니다.")
     else :
        print("당신이 입력한 수는 홀수입니다")