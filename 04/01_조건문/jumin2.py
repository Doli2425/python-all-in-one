jumin = input("주민번호를 입력하세요(예시: 123456-7890123): ")

num = [2,3,4,5,6,7,8,9,2,3,4,5]
jumin_num = []
sum = 0

for i in jumin:
    if i == '-':
        continue
    else:
        jumin_num.append(int(i))

for i in range (len(num)):
    sum += jumin_num[i] * num[i]

result = sum % 11

if (11-result) == int(jumin_num[-1]) :
    print("유효하다.")
else:
    print("유효하지 않다.")
