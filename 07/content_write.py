file = 'file.txt'

fd = open(file, 'a')
for i in range(1, 11):
    data = f"{i}번째 줄입니다.\n"
    fd.write(data)
fd.close()
