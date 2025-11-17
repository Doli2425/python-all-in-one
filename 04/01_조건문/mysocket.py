import socket

ip = "192.168.10.60"
port = 21

s = socket.socket()
s.connect((ip, port))
ans = s.recv(1024)
print(ans)


if "vsFTPd 2.0.5" in str(ans):
    print("[-] 'CWD' (Authenticated) Remote Memory Consumption")
elif "vsFPTd 2.3.2" in str(ans):
    print("[+] Denial of Servoce")
elif "vsFTPd 2.3.4" in str(ans):
    print("[+] Backdoor Command Execution (Metasploit)")
else:
    print("[-] Not vulnerable")