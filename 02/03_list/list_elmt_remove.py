numbers = [1, 2, 3, 4, 5, 3, 2, 9, 10, 3]

numbers.remove(3)
print(f"output1: {numbers}")

new = []
for num in numbers:
    if num != 3:
        new.append(num)

print(f"output2: {new}")