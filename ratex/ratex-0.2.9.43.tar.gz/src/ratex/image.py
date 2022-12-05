import os, shutil

# // Image class
class Image(object):
    def __init__(self, path: str, scale: int = 1) -> None:
        path_split: list[str] = path.split("/")
        file_name: str = "".join(f"\\{a}" for a in path_split[1:len(path_split) - 1])
        if not os.path.exists(f"{self.file_dir}/build/{file_name}"):
            os.mkdir(f"{self.file_dir}/build/{file_name}")
        shutil.copy(path, f"{self.file_dir}/build/{file_name}")
        self.path = path
        self.scale = scale
    
    def __str__(self) -> str:
        return f"\includegraphics[scale={self.scale}]{{{self.path}}}"
    