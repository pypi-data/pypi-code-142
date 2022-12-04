#!/usr/bin/env python3
import socket, sys, threading
try:
    from .kosti import main as kosti
except:
    from kosti import main as kosti
bbs = """\x1b[48;5;17m\x1b[38;5;240m\x1b[?25l
                     \x1b[38;5;255mI) Get example file\x1b[38;5;240m
          _______    \x1b[38;5;255mD) Play game of dice\x1b[38;5;240m
      ___/     _/    \x1b[38;5;255mQ) Quit\x1b[38;5;240m
    _/      __/      
   /   O  _/         
 _/     _/           
/     _/             
       ,,,__         
           /         
         _/          
     ___/           
\x1b[38;5;33m\x1b[48;5;0m
Hello, dear user. This is the Carcharodon BBS.










\x1b[?25h\x1b[0m"""

loremipsum = """\x1b[?25h\x1b[0m
Lorem ipsum dolor sit amet, consectetur 
adipiscing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua. Ut 
enim ad minim veniam, quis nostrud exercitation 
ullamco laboris nisi ut aliquip ex ea commodo 
consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum 
dolore eu fugiat nulla pariatur. Excepteur sint 
occaecat cupidatat non proident, sunt in culpa 
qui officia deserunt mollit anim id est laborum.

Enter y command to return to main screen
"""

def handle(conn):
    sndie = True
    while True:
        try:
            if sndie:
                conn.send(bytes(bbs, 'utf-8'))
                sndie = False
            data = conn.recv(1)
            sata = str(data, 'utf-8')
            if sata == 'Q':
                conn.send(bytes("\x1b[?25h\x1b[0m", "ascii"))
                conn.close()
                break
            elif sata == "I":
                conn.send(bytes(loremipsum, 'utf-8'))
                sndie = False
            elif sata == "y":
                sndie = True
            elif sata == "D":
                kosti(conn)
                sndie = True
            elif sata in ['\r', '\n']:
                pass
        except:
            continue

def main():
    sock = socket.socket(socket.SO_REUSEADDR)
    sock.bind(('', 9090))
    sock.listen(0)
    while True:
        conn, addr = sock.accept()
        if conn and addr:
            print('connected:', addr)
            t = threading.Thread(target=lambda:handle(conn))
            t.start()
        # conn.send(bytes(bbs, 'utf-8'))
        # data, addr = conn.recv(1)
        # print('connected:')
        # while True:
            # try:
                # data, addr = conn.recvfrom(1)
                # sata = str(data, 'utf-8')
                # if sata == 'Q':
                    # conn.send(bytes("\x1b[?25h\x1b[0m", "ascii"))
                    # break
                # elif sata == "I":
                    # conn.send(bytes(loremipsum, 'utf-8'))
                    # d = conn.recv(1)
                    # while d != b'y':
                        # d = conn.recv(1)
            # except:
                # continue
    conn.close()
    return 0

if __name__ == '__main__':
    sys.exit(main())
