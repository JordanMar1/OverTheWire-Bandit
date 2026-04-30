from pwn import *
from colors import *

file = open("flag1.txt", "r")
pwd = file.read()

print(JAUNE + "Connecting to ssh...")

shell = ssh('bandit1', 'bandit.labs.overthewire.org', password=pwd, port=2220)
if shell['whoami'].decode() == "bandit1":
    print(VERT + GRAS + "Connected to the ssh")
else:
    print(ROUGE + GRAS + SOULIGNE + "Error, check that everything is okay")


print(JAUNE + "Launching Command to get flag...")
try:
    sh = shell.run("cat ./-")
    flag = sh.recvall().decode().strip()
    print("Flag Discovered:" + JAUNE + flag)
    print(BLEU + "Writing the flag inside the " + SOULIGNE + "flag2.txt" + RESET + BLEU + " file...")
    with open("flag2.txt", "w") as f:
        f.write(flag)
        print(VERT + GRAS + "Task 2 terminée et écrite dans " + SOULIGNE + "flag2.txt" + RESET)
except Exception as e:
    print(ROUGE + GRAS + SOULIGNE + "Flag undiscovered because of the error: " + str(e))

