from os import path, walk


class GetFilesFromFolder:
    
    def __init__(self, path, exts):
        self.file_path = path
        self.file_exts = exts.split(",")

    def file_list(self):
        file_list = []
        for root, dirs, files in walk(self.file_path):
            for ext in self.file_exts:
                [file_list.append(path.join(root, name)) for name in files if name.endswith("."+ext)]
        return file_list


class MoveFileToFolder:
    def __init__(self, flist, dest_folder):
        self.flist = flist
        self.dest_folder = dest_folder

    def move2folder(self):
        pass


if __name__ == "__main__":
    lists = GetFilesFromFolder(path=r"C:\Users\sha-gregh\Desktop\edoc_Auto-Index", exts="pdf").file_list()
    print(len(lists))
