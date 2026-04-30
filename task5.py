from pwn import *
from colors import *

file = open("flag4.txt", "r")
pwd = file.read()

print(JAUNE + "Connecting to ssh...")

shell = ssh('bandit4', 'bandit.labs.overthewire.org', password=pwd, port=2220)
if shell['whoami'].decode() == "bandit4":
    print(VERT + GRAS + "Connected to the ssh")
else:
    print(ROUGE + GRAS + SOULIGNE + "Error, check that everything is okay in previous tasks")


print(JAUNE + "Launching Command to get flag...")
try:
    sh = shell.run('find /home/bandit4/inhere/ -type f -exec file {} \;')
    files = sh.recvall().decode().split("\n")
    for file in files:
        if "ASCII" in file:
            flag_file = file.split(':')[0]
    sh = shell.run('cat ' + flag_file)
    flag = sh.recvall().decode()
    print("Flag Discovered:" + JAUNE + flag)
    print(BLEU + "Writing the flag inside the " + SOULIGNE + "flag5.txt" + RESET + BLEU + " file...")
    with open("flag5.txt", "w") as f:
        f.write(flag)
        print(VERT + GRAS + "Task 5 terminée et écrite dans " + SOULIGNE + "flag5.txt" + RESET)
except Exception as e:
    print(ROUGE + GRAS + SOULIGNE + "Flag undiscovered because of the error: " + str(e))

