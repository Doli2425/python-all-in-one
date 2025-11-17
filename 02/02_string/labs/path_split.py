# path = input("Path: ")
path = "/etc/security/pam_security.so"

print(f"path: {'/'.join(path.split('/')[:-1])}")
print(f"file: {path.split('/')[-1]}")
