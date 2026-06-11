from pwn import *
from colors import *
import codecs

file = open("flag11.txt", "r")
pwd = file.read()

print(JAUNE + "Connecting to ssh...")

shell = ssh('bandit11', 'bandit.labs.overthewire.org', password=pwd, port=2220)
if shell['whoami'].decode() == "bandit11":
    print(VERT + GRAS + "Connected to the ssh")
else:
    print(ROUGE + GRAS + SOULIGNE + "Error, check that everything is okay in previous tasks")


print(JAUNE + "Launching Command to get flag...")
try:
    sh = shell.run('cat data.txt')
    resp = sh.recvall().decode().split()[3]
    print(resp)
    flag = codecs.decode(resp, 'rot13')
    print("Flag Discovered:" + JAUNE, flag)
    print(BLEU + "Writing the flag inside the " + SOULIGNE + "flag12.txt" + RESET + BLEU + " file...")
    with open("flag12.txt", "w") as f:
        f.write(flag)
        print(VERT + GRAS + "Task 12 terminée et écrite dans " + SOULIGNE + "flag12.txt" + RESET)
except Exception as e:
    print(ROUGE + GRAS + SOULIGNE + "Flag undiscovered because of the error: " + str(e))

