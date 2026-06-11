from pwn import *
from colors import *
import codecs

file = open("flag12.txt", "r")
pwd = file.read().strip()

print(JAUNE + "Connecting to ssh...")

shell = ssh('bandit12', 'bandit.labs.overthewire.org', password=pwd, port=2220)
if shell.run('whoami').recvall().decode().strip() == "bandit12":
    print(VERT + GRAS + "Connected to the ssh")
else:
    print(ROUGE + GRAS + SOULIGNE + "Error, check that everything is okay in previous tasks")

print(JAUNE + "Launching Command to get flag...")

try:
    cmd = (
        "MY_TMP=$(mktemp -d) && cd $MY_TMP && "
        "cp ~/data.txt ./hexdump_data && "
        "xxd -r hexdump_data data && "
        "while ! file data | grep -q 'ASCII text'; do "
          "case $(file data) in "
            "*gzip*) mv data data.gz && gzip -d data.gz ;;"
            "*bzip2*) mv data data.bz2 && bzip2 -d data.bz2 ;;"
            "*tar*) mv data data.tar && tar xf data.tar && rm data.tar && mv $(ls | head -n1) data ;;"
          "esac; "
        "done; cat data"
    )
    sh = shell.run(cmd)
    resp = sh.recvall().decode().strip()
    flag = resp.split()[-1] 

    print("Flag Discovered: " + JAUNE + flag + RESET)
    print(BLEU + "Writing the flag inside the " + SOULIGNE + "flag13.txt" + RESET + BLEU + " file...")
    with open("flag13.txt", "w") as f:
        f.write(flag)
    print(VERT + GRAS + "Task 13 terminée et écrite dans " + SOULIGNE + "flag13.txt" + RESET)

except Exception as e:
    print(ROUGE + GRAS + SOULIGNE + "Flag undiscovered because of the error: " + str(e) + RESET)
finally:
    shell.close()