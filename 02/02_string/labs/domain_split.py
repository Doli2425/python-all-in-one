url = input("address: ")

print(f"domain: {url.split('/')[2].split('.')[-1]}")