from pwn import *
from colors import *

print(JAUNE + "Connecting to ssh...")

shell = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0', port=2220)
if shell['whoami'].decode() == "bandit0":
    print(VERT + GRAS + "Connected to the ssh")
else:
    print(ROUGE + GRAS + SOULIGNE + "Error, check that everything is okay")


print(JAUNE + "Launching Command to get flag...")
try:
    sh = shell.run('cat readme')
    sh.recvuntil("The password you are looking for is: ").decode()
    flag = sh.recvall().decode().strip()
    print("Flag Discovered:" + JAUNE + flag)
    print(BLEU + "Writing the flag inside the flag1.txt file...")
    with open("flag1.txt", "w") as f:
        f.write(flag)
        print(VERT + GRAS + "Task 1 terminée et écrite dans " + SOULIGNE + "flag1.txt" + RESET)
except Exception as e:
    print(ROUGE + GRAS + SOULIGNE + "Flag undiscovered because of the error: " + str(e))

