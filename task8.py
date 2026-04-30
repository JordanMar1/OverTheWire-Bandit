from pwn import *
from colors import *

file = open("flag7.txt", "r")
pwd = file.read()

print(JAUNE + "Connecting to ssh...")

shell = ssh('bandit7', 'bandit.labs.overthewire.org', password=pwd, port=2220)
if shell['whoami'].decode() == "bandit7":
    print(VERT + GRAS + "Connected to the ssh")
else:
    print(ROUGE + GRAS + SOULIGNE + "Error, check that everything is okay in previous tasks")


print(JAUNE + "Launching Command to get flag...")
try:
    sh = shell.run('grep millionth data.txt')
    flag = sh.recvall().decode().split()[1].strip()
    print("Flag Discovered:" + JAUNE + flag)
    print(BLEU + "Writing the flag inside the " + SOULIGNE + "flag8.txt" + RESET + BLEU + " file...")
    with open("flag8.txt", "w") as f:
        f.write(flag)
        print(VERT + GRAS + "Task 8 terminée et écrite dans " + SOULIGNE + "flag8.txt" + RESET)
except Exception as e:
    print(ROUGE + GRAS + SOULIGNE + "Flag undiscovered because of the error: " + str(e))

