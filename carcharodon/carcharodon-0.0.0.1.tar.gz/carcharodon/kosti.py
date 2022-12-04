#!/usr/bin/env python3
import socket, sys, random

getnum = lambda : random.randint(0, 6)
kosti = lambda : (getnum(), getnum())

def main(conn):
    show = True
    while True:
        if show:
            conn.send(b"Enter T to play. Enter Q to exit.\r\n")
        d = conn.recv(1)
        if d in [b'\r', b'\n']:
            show = False
        elif d == b'T':
            a = kosti()
            conn.send(f"({a[0]}, {a[1]})\r\n".encode('ascii'))
            show = True
        elif d == b'Q':
            break
    return 0

if __name__ == '__main__':
    sys.exit(-1)
