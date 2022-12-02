import argparse
import distutils
import os
import sys


class Colors:
	BLACK = '\033[30m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	MAGENTA = '\033[35m'
	CYAN = '\033[36m'
	WHITE = '\033[37m'
	UNDERLINE = '\033[4m'
	RESET = '\033[0m'





def str2bool(v):
	return bool(distutils.util.strtobool(v))





parser = argparse.ArgumentParser(description='Volume Electron Microscopy REGistration (vEMreg) Example')
parser.add_argument("--dataDir", type=str, help="Path to the raw data to register/align.")
parser.add_argument('--imName', type=str, default=None, help='The name of the image to use as first target. Can be '
																'null, and defaulted to None.')
parser.add_argument('--transformation', type=str, default="Affine", help='The type of transformation to perform: '
																			'Affine or Bilinear. Default="Affine"')
parser.add_argument('--nIterations', type=int, default=7, help='The number of iterations to perform for each pair of'
												' images with a minimum of 5, but at least 7 recommended. Default=7.')
parser.add_argument('--aggressive', type=str2bool, nargs='?', const=True, default=False, help='Use aggressive (further '
																				'appart) point selection? Default=True')
parser.add_argument("--safetyLevel", type=int, default=2, help="The level of safety to use among 0 (no safety), "
																"1 (basic), 2 (advanced, recommended). Default=2.")
parser.add_argument("--resultsDir", type=str, default="./Registered/", help="Path to the registered/aligned images.")
parser.add_argument("--nCores", type=int, default=6, help="Number of cores to use during parallelization. Defaults=6.")
parser.add_argument('--debug', type=str2bool, nargs='?', const=True, default=True, help='Use debug mode? Default=True.')
parser.add_argument('--Java_Xms', type=str, default="8G", help='Java virtual machine starting memory option. Default=8G')
parser.add_argument('--Java_Xmx', type=str, default="32G",help='Java virtual machine maximum memory option. Default=32G')





def _Run_(dataDir: str, imName: str, transformation: str, nIterations:int, aggressive: bool, safetyLevel: int,
			resultsDir: str, nCores: int, debug: bool, Java_Xms: str, Java_Xmx: str):
	
	if dataDir is None or dataDir == "":
		print(Colors.RED + "Error - dataDir not defined." + Colors.RESET)
		raise Exception("dataDir not defined.")
	
	if transformation.lower() == "affine":
		trans = "StackRegistration.AFFINE"
	elif transformation.lower() == "bilinear":
		trans = "StackRegistration.BILINEAR"
	else:
		print(Colors.RED + "Error - Unknown transformation: '" + str(transformation) + "'. Expected: Affine or "
				"Bilinear." + Colors.RESET)
		raise Exception("Unknown transformation: '" + str(transformation) + "'. Expected: Affine or Bilinear.")
	
	if nIterations < 5:
		print(Colors.RED + "Error - nIterations < 5." + Colors.RESET)
		raise Exception("nIterations < 5")
	elif nIterations < 7:
		print(Colors.RED + "WARNING - " + Colors.RESET + " nIterations < 7. At least 7 iterations "
				"recommended.\n")
	
	if safetyLevel < 0:
		print(Colors.RED + "Error - safetyLevel < 0." + Colors.RESET)
		raise Exception("safetyLevel < 0")
	elif safetyLevel == 0:
		print(Colors.RED + "WARNING - " + Colors.RESET + " safetyLevel=0 => no check performed during processing.\n")
	elif safetyLevel == 1:
		print(Colors.RED + "WARNING - " + Colors.RESET + " safetyLevel=1 => Basic check performed during processing.\n")
	elif 2 < safetyLevel:
		print(Colors.RED + "Error - 2 < safetyLevel. O, 1, or 2 expected." + Colors.RESET)
		raise Exception("2 < safetyLevel. O, 1, or 2 expected.")
	
	if resultsDir is None or resultsDir == "":
		raise Exception("resultsDir not defined.")
	
	if nCores <= 0:
		print(Colors.RED + "Error - nCores <= 0." + Colors.RESET)
		raise Exception("nCores <= 0")
	
	Java_Path = "java"
	Javac_Path = "javac"
	JavaJarsPath = os.path.dirname(os.path.abspath(__file__))
	Java_ClassPath = "-classpath .:" + JavaJarsPath + "/FiReTiTiLiB.jar:" + JavaJarsPath + "/lib/*:."
	#Java_ClassPath = "-classpath .:FiReTiTiLiB.jar:lib/*:."
	Java_Options = "-noverify -Xms" + Java_Xms + " -Xmx" + Java_Xmx
	
	if debug:
		print("JavaJarsPath=" + JavaJarsPath)
		print("Java_ClassPath=" + Java_ClassPath)
		print("Java_Options=" + Java_Options)
		print()
	
	java = open("vEMreg.java", "w")
	
	java.write('import filesAndFolders.*;\n')
	java.write('import java.io.*;\n')
	java.write('import registration.turboreg.StackRegistration;\n\n')
	
	java.write('public class vEMreg\n')
	java.write('{\n\n')
	
	java.write('public static void main(String[] args) throws Exception\n')
	java.write('\t{\n')
	
	java.write('\tfinal int nbCPU = ' + str(nCores) + ' ;\n\n')
	java.write('\tStackRegistration sr = new StackRegistration() ;\n\n')
	java.write('\tsr.StochasticProcess("' + dataDir + '", ' + ('"' + imName + '"' if imName is not None else 'null')
				+ ', FileNameFilters.ImagesPNGorTIF, new HumanSort<File>(), ' + trans + ', ' + str(nIterations) + ', '
				+ ('true' if aggressive else 'false') + ', ' + str(safetyLevel) + ', null, "' + resultsDir + '", '
				+ str(nCores) + ', ' + str('true' if debug else 'false') + ') ;\n\n')
	java.write('\tSystem.exit(0) ;\n')
	java.write('\t}\n')
	java.write('}\n')
	java.close()
	
	exit = os.system(Javac_Path + " " + Java_ClassPath + " vEMreg.java")
	print("Java compilation done and exited with status " + str(exit) + "\n")
	if exit != 0:
		print(Colors.RED + "Error - Failed compilation." + Colors.RESET)
		return
	
	exit = os.system(Java_Path + " " + Java_Options + " " + Java_ClassPath + " vEMreg")
	print("Processing done and exited with status " + str(exit))
	if exit != 0:
		print(Colors.RED + "Error - Failed execution." + Colors.RESET)
	
	if not debug:
		os.remove("vEMreg.java")
	os.remove("vEMreg.class")





def Register(parameters: dict = None):
	if parameters is not None:  # Running from script with parameters in a dict.
		args = []
		for key in parameters.keys():
			args.append("--" + str(key) + "=" + str(parameters[key]))
		opt, unknown = parser.parse_known_args(args)
	else:  # Running from command line
		opt, unknown = parser.parse_known_args()
	
	if len(unknown) != 0:
		print(Colors.RED + "Error - Unknown argument" + ("" if len(unknown) == 1 else "s") + ":")
		print(unknown)
		print(Colors.RESET)
		sys.exit(1)
	
	if opt.debug:
		print("Debugging mode activated.")
		print("Command line arguments:")
		print(opt)
		print()
	
	_Run_(opt.dataDir, opt.imName, opt.transformation, opt.nIterations, opt.aggressive, opt.safetyLevel, opt.resultsDir,
			opt.nCores, opt.debug, opt.Java_Xms, opt.Java_Xmx)





if __name__ == '__main__':
	print("Let's go manual!")
	parameters = {'dataDir': "/Users/firetiti/Downloads/EM/Registration/101/",
					#'imName': "Image - SliceImage - 005.tif",
					#'transformation': "Affine",
					#'nIterations': 7,
					#'aggressive': False,
					#'safetyLevel': 2,
					#'nCores': 6,
					'debug': True}
	Register(parameters=parameters)
	#Register()
