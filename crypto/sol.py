from pwn import *
import re


r = remote('0.cloud.chals.io', 16499)

key = []


def tick():
    ans = r.recvuntil("$ enter your number")
    print(ans)
    stringy = re.search("A.{1,10}n", str(ans)).group()
    number = "".join([str(x) for x in stringy if x.isdigit()])
    key.append(number)
    r.send(str(number)+"\n")


run = 1
while run:
    try:
        tick()
    except:
        print(r.recv())
        # for i in key:
        #     print(chr(int(i)), end='')
        print([hex(int(x)) for x in key])
        print(len(key))
        run = 0
