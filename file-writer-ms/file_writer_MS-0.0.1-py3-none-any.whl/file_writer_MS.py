
class FileManipulator:
    '''
    A class that provides file manipulation including:
    open, close, read and write to a file
    '''
    def open_file(self, path, mode = 'read'):
        ''' 
        To open a file either in read or write mode
        '''

        mode_dict = {'read':'r', 'write':'w'}
        try:
            self.file = open(path, mode_dict[mode])
            
        except Exception as e:
            print(f"The file could not be opened due to this error\n {e}")
            return False
        return True

    def close_file(self):
        '''
        To close the previousely opened file
        '''
        if hasattr(self, 'file'):
            if not self.file.closed:
                self.file.close()
            return True
        else:
            return False

    def write_to_file(self, content):
        '''
        To write a content in the file
        '''
        if hasattr(self, 'file'):
            try:
                if not self.file.closed:
                    self.file.write(content)
                else:
                    return False
            except Exception as e:
                print(f"Writing to file was not successful\n {e}")
                return False
            return True
        else:
            return False

    def read_a_file(self):
        '''
        To read content of a file
        '''
        if hasattr(self, 'file'):
            try:
                if not self.file.closed:
                    return self.file.read()
                else:
                    return False
            except Exception as e:
                print(f"Writing to file not successful\n {e}")
                return False
        else:
            return False

import sys

def show_help_menu():
    '''
    to print out help menu
    '''
    help_text = """ This is the help menu
    
    -t (text): to feed a text\n
    -o (filename): to write text to output file\n
    -r (filename): to read a file\n
    to quit the program just type "quit" or "exit"\n
    example: to write "sample text" to "output.txt" file:
    python test.py -t "sample text" -o output.txt\n
    example2: to copy a file to another:
    python test.py -r original.txt -o copy.txt"""
    print(help_text)
    

def greeting():
    '''
    called when no arguments are passed.
    '''
    print("""Welcome to file manipulator. If you know how to work with me, go ahead and  
    type the command. otherwise type "-h" to get help.""")
    

def parse_argv(argv):
    '''
    To look for options and arguments to create commands
    '''
    if '-h' in argv or '--help' in argv: return {'-h':None}
    commands = {}
    for opt,arg in zip(argv, argv[1:]):
        if opt.startswith("-") and not arg.startswith("-"):
            if opt in ['-r', '-o', '-t']:
                commands[opt] = arg
            else:
                print(f'Bad command used: {opt}')
    return commands

def input_commands(argv = None):
    '''
    To ask input from the user
    '''
    if not argv:
        argv = input().split()
        if argv == ['exit'] or argv == ['quit']:
            exit(0)
    commands = parse_argv(argv)
    return commands

if __name__ == '__main__':

    # if no argument is passed at the starting, greeting will be called
    if len(sys.argv) == 1: 
        commands = {}
        while commands == {}:
            greeting()
            commands = input_commands()
    else:
        commands = input_commands(sys.argv[1:])

    # To make sure the user reads the help menu
    while "-h" in commands.keys() or '--help' in commands.keys():
        show_help_menu()
        commands = input_commands()

    while '-t' not in commands.keys() and '-r' not in commands.keys():
        print('''There is nothing to write to the file. 
        Please use -t followed by a text 
        or -r followed by a filename as the source text''')
        commands = input_commands()
    
    file_man = FileManipulator()
    
    if '-t' in commands.keys():
        text = commands['-t']
    elif '-r' in commands.keys():
        if file_man.open_file(commands['-r']):
            text = file_man.read_a_file()
            file_man.close_file()
        else:
            text = None
            
    # -o is for output file. As long as there is no output file
    # it asks the user to enter it.
    while '-o' not in commands.keys():
        print("Please add a '-o' command followed by a filename to write the content")
        commands = input_commands()
    
    if file_man.open_file(commands['-o'], mode = 'write'):
        if file_man.write_to_file(text):
            print(f'Written to file successfully')
    file_man.close_file()
    
