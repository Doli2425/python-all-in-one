num1 = int(input("첫번째 숫자를 입력하시오: "))
num2 = int(input("두번째 숫자를 입력하시오: "))

if num1 > num2:
    print(num1)
    if num1 % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    print(num2)
    if num2 % 2 == 0:
        print("even")
    else:
        print("odd")