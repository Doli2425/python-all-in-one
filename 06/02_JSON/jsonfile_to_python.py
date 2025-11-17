import json

file = 'seoul.json'
fd = open(file)
data = json.load(fd)
fd.close()

print(data)
data["population"] = 9600000
print(data)

fd = open(file, 'w')
data["city"] = "Busan"
data["population"] = 3249975
json.dump(data, fd)
fd.close()

print(open(file).read())
