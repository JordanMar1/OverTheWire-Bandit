from pwn import *
from colors import *

file = open("flag5.txt", "r")
pwd = file.read()

print(JAUNE + "Connecting to ssh...")

shell = ssh('bandit5', 'bandit.labs.overthewire.org', password=pwd, port=2220)
if shell['whoami'].decode() == "bandit5":
    print(VERT + GRAS + "Connected to the ssh")
else:
    print(ROUGE + GRAS + SOULIGNE + "Error, check that everything is okay in previous tasks")


print(JAUNE + "Launching Command to get flag...")
try:
    sh = shell.run('find /home/bandit5/inhere/ -type f -size 1033c \! -executable -exec file {} \;')
    files = sh.recvall().decode().split("\n")
    for file in files:
        if "ASCII" in file:
            flag_file = file.split(':')[0]
    sh = shell.run('cat ' + flag_file)
    flag = sh.recvall().decode().strip()
    print("Flag Discovered:" + JAUNE + flag)
    print(BLEU + "Writing the flag inside the " + SOULIGNE + "flag6.txt" + RESET + BLEU + " file...")
    with open("flag6.txt", "w") as f:
        f.write(flag.strip())
        print(VERT + GRAS + "Task 6 terminée et écrite dans " + SOULIGNE + "flag6.txt" + RESET)
except Exception as e:
    print(ROUGE + GRAS + SOULIGNE + "Flag undiscovered because of the error: " + str(e))

