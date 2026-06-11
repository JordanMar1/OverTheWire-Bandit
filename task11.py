from pwn import *
from colors import *
import codecs

file = open("flag10.txt", "r")
pwd = file.read()

print(JAUNE + "Connecting to ssh...")

shell = ssh('bandit10', 'bandit.labs.overthewire.org', password=pwd, port=2220)
if shell['whoami'].decode() == "bandit10":
    print(VERT + GRAS + "Connected to the ssh")
else:
    print(ROUGE + GRAS + SOULIGNE + "Error, check that everything is okay in previous tasks")


print(JAUNE + "Launching Command to get flag...")
try:
    sh = shell.run('strings data.txt | base64 -d')
    flag = sh.recvall().decode().split(" ")[3].split()[0]
    print("Flag Discovered:" + JAUNE, flag)
    print(BLEU + "Writing the flag inside the " + SOULIGNE + "flag11.txt" + RESET + BLEU + " file...")
    with open("flag11.txt", "w") as f:
        f.write(flag)
        print(VERT + GRAS + "Task 11 terminée et écrite dans " + SOULIGNE + "flag11.txt" + RESET)
except Exception as e:
    print(ROUGE + GRAS + SOULIGNE + "Flag undiscovered because of the error: " + str(e))
finally:
    shell.close()