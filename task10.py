from pwn import *
from colors import *

file = open("flag9.txt", "r")
pwd = file.read()

print(JAUNE + "Connecting to ssh...")

shell = ssh('bandit9', 'bandit.labs.overthewire.org', password=pwd, port=2220)
if shell['whoami'].decode() == "bandit9":
    print(VERT + GRAS + "Connected to the ssh")
else:
    print(ROUGE + GRAS + SOULIGNE + "Error, check that everything is okay in previous tasks")


print(JAUNE + "Launching Command to get flag...")
try:
    sh = shell.run('strings data.txt | grep "=="')
    flag = sh.recvall().decode().strip().split('\n')[3].split()[1]
    print("Flag Discovered:" + JAUNE, flag)
    print(BLEU + "Writing the flag inside the " + SOULIGNE + "flag10.txt" + RESET + BLEU + " file...")
    with open("flag10.txt", "w") as f:
        f.write(flag)
        print(VERT + GRAS + "Task 10 terminée et écrite dans " + SOULIGNE + "flag10.txt" + RESET)
except Exception as e:
    print(ROUGE + GRAS + SOULIGNE + "Flag undiscovered because of the error: " + str(e))

