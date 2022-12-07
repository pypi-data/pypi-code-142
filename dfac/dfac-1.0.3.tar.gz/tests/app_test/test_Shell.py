import unittest
from dfac.app.Shell import Shell
from random import randint

class ShellTestMethods(unittest.TestCase):
    
    def test_Commands(self):
        shell = Shell()
        stringlist = "-t a -v n".split()
        with self.assertRaises(TypeError):
            shell.check_for_errors(3)
        shell.parse(stringlist)
    
    def test_all_commands_string(self):
        shell = Shell()
        strings=["-t s -v n", "-t s -v a","-t s -v u","-t s -v l","-t s -v y","-t s -v a -0 "+str(randint(1,100)), "-t s -v l -x xyz", "-t s -v u -x" ]
        for s in strings:
            x=s.split()
            shell.parse(x) 

    def test_all_commands_array(self):            
        shell= Shell()        
        strings=["-t a -v n", "-t a -v a","-t a -v u","-t a -v l -L 7 -H 90","-t a -v i","-t a -v o","-t a -v d","-t a -v y","-t a -v a -0 "+str(randint(1,100)), "-t a -v l -x xyz", "-t a -v u -x" ]
        for s in strings:
            x=s.split()
            shell.parse(x)