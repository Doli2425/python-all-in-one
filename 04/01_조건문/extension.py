filenames = ['intra.h', 'intra.c', 'input.txt', 'run.py']

result = []

for filename in filenames:
    if filename.split('.')[-1] == 'h' or filename.split('.')[-1] == 'c':
        result.append(filename)

print(result)
