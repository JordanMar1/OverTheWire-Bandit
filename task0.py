from pwn import *
from colors import *

print(JAUNE + "Connecting to ssh...")

shell = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0', port=2220)
if shell['whoami'].decode() == "bandit0":
    print(VERT + GRAS + SOULIGNE + "Connected to the ssh")
else:
    print(ROUGE + GRAS + SOULIGNE + "Error, check that everything is okay")
