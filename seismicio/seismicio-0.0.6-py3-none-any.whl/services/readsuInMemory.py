import fs
from ..Models.InOutSuModel import InOutSu

def readsuInMemory(file_path):
	# Read a binary file in .su format
	# from in-memory temporary file system
	mem_fs = fs.open_fs('mem://')
	with mem_fs.open(file_path, 'rb') as file:
		return InOutSu.unpack_su(file)
