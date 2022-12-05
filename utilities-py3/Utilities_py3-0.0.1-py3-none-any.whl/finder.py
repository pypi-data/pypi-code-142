import os

def find_file(target,local):
    pathName = lambda root,x: os.path.join(root,x)
    for root, dirs, files in os.walk("C:\\"):
        if(target in files):
            return pathName(root,target)
            
if __name__ == "__main__":
    target = input("> ")
    find_file(target,"C:\\")