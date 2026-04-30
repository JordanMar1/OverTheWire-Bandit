from pwn import *
from colors import *

file = open("flag6.txt", "r")
pwd = file.read()

print(JAUNE + "Connecting to ssh...")

shell = ssh('bandit6', 'bandit.labs.overthewire.org', password=pwd, port=2220)
if shell['whoami'].decode() == "bandit6":
    print(VERT + GRAS + "Connected to the ssh")
else:
    print(ROUGE + GRAS + SOULIGNE + "Error, check that everything is okay in previous tasks")


print(JAUNE + "Launching Command to get flag...")
try:
    sh = shell.run('find / -user bandit7 -group bandit6 -size 33c 2>/dev/null')
    files = [line.strip() for line in sh.recvall().decode().splitlines() if line.strip()]
    print(files)
    if not files:
        raise ValueError('Aucun fichier trouvé avec les critères demandés')
    flag_file = files[0]
    sh = shell.run('cat ' + flag_file)
    flag = sh.recvall().decode().strip()
    print("Flag Discovered:" + JAUNE + flag)
    print(BLEU + "Writing the flag inside the " + SOULIGNE + "flag7.txt" + RESET + BLEU + " file...")
    with open("flag7.txt", "w") as f:
        f.write(flag.strip())
        print(VERT + GRAS + "Task 7 terminée et écrite dans " + SOULIGNE + "flag7.txt" + RESET)
except Exception as e:
    print(ROUGE + GRAS + SOULIGNE + "Flag undiscovered because of the error: " + str(e))

