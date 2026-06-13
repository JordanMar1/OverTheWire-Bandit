from pwn import *
from colors import *

try:
    with open("flag14.txt", "r") as file:
        pwd = file.read().strip()
except FileNotFoundError:
    print(ROUGE + "Error: flag14.txt not found!" + RESET)
    exit(84)

print(JAUNE + "Connecting to bandit14..." + RESET)
shell14 = ssh('bandit14', 'bandit.labs.overthewire.org', password=pwd, port=2220)
print(VERT + "Connected! Sending password to port 30000..." + RESET)

io = shell14.remote('localhost', 30000)
io.sendline(pwd.encode())
response = io.recvall(timeout=5).decode().strip()
io.close()
shell14.close()

print(BLEU + "Response: " + response + RESET)

lines = [l.strip() for l in response.splitlines() if l.strip()]
flag15 = lines[-1] if lines else None

if not flag15 or "Wrong" in response:
    print(ROUGE + GRAS + "Failed to retrieve flag!" + RESET)
    exit(84)

print("Flag Discovered: " + JAUNE + flag15 + RESET)
print(BLEU + "Writing the flag inside flag15.txt..." + RESET)

with open("flag15.txt", "w") as f:
    f.write(flag15)

print(VERT + GRAS + "Task 15 terminée et écrite dans flag15.txt" + RESET)