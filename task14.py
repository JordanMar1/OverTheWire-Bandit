from pwn import *
from colors import *
try:
    with open("flag13.txt", "r") as file:
        pwd = file.read().strip()
except FileNotFoundError:
    print(ROUGE + "Error: flag13.txt not found!" + RESET)
    exit(1)
print(JAUNE + "Connecting to bandit13 to fetch the private key..." + RESET)
shell13 = ssh('bandit13', 'bandit.labs.overthewire.org', password=pwd, port=2220)
print(VERT + "Connected! Downloading sshkey.private content..." + RESET)
key_data = shell13.run('cat ~/sshkey.private').recvall().decode().strip()
shell13.close()
key_path = "./sshkey.private"
with open(key_path, "w") as f:
    f.write(key_data)
import os
os.chmod(key_path, 0o600)
print(JAUNE + "Connecting to bandit14 using the private key..." + RESET)
try:
    shell14 = ssh('bandit14', 'bandit.labs.overthewire.org', keyfile=key_path, port=2220)
    print(VERT + GRAS + "Successfully connected to bandit14!" + RESET)
    print(JAUNE + "Retrieving flag14..." + RESET)
    flag14 = shell14.run('cat /etc/bandit_pass/bandit14').recvall().decode().strip()
    print("Flag Discovered: " + JAUNE + flag14 + RESET)
    print(BLEU + "Writing the flag inside flag14.txt..." + RESET)
    with open("flag14.txt", "w") as f:
        f.write(flag14)
    print(VERT + GRAS + "Task 14 terminée et écrite dans flag14.txt" + RESET)

except Exception as e:
    print(ROUGE + GRAS + "Error connecting to bandit14: " + str(e) + RESET)

finally:
    if os.path.exists(key_path):
        os.remove(key_path)
    if 'shell14' in locals():
        shell14.close()