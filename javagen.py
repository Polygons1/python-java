import platform
import os

os.chdir("build")

is_jdk = 0
download = 0
filesnum = 0
chk_filesnum = 0

def start():
	print("you need jdk added in the path to continue")
	print("you can get jdk in https://www.oracle.com/java/technologies/downloads/#java17")
	print("java 17 is recommended")
	print("if you want the script will install jdk 17 for you")
	os.system("pause")

def check_jdk():
	os.chdir("C:\\Program Files")
	for chk in os.listdir():
		filesnum = filesnum + 1
	for e in os.listdir():
		chk_filesnum = chk_filesnum + 1
		if e == "Java":
			os.chdir("Java")
			for l in e:
				if os.name == "nt" and e == "r":
					is_jdk = False
					break
				elif os.name == "posix" and e == "r":
					is_jdk = False
					break
				else:
					print("you have jdk, you good!")
					is_jdk = True
					break
		elif chk_filesnum == filesnum:
			is_jdk = False
			break
		else:
			break
	if is_jdk == False:
		while True:
			yn = input("you want to download jdk 17? y/n")
			if yn == "y" or yn == "Y":
				download = True
				break
			elif yn == "n" or yn == "N":
				download = False
				break
		if download == True:
			if os.name == "nt" and platform.version() > 10:
				os.system("curl -L https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.msi -o jdksetup.msi")
				os.system("jdksetup.msi")
			elif os.name == "posix" and platform.system() == "Darwin":
				os.system("curl -L https://download.oracle.com/java/17/latest/jdk-17_macos-x64_bin.dmg -o jdksetup.dmg")
def generate_file(fn, inmain):
	open(f"{fn}.java", "w").write(
		f'class {fn} ' + '{\n	public static void main(String[] args) {' + f'\n		{inmain};' + '\n	}\n}'
		)
	return fn

def compile(fn):
	os.system(f"javac {fn}.java")
	open("MANIFEST.MF", "w").write(f"Manifest-Version: 1.0\nMain-Class: {fn}\n\n")
	os.chdir("output")
	os.system(f"jar -cmvf ../MANIFEST.MF {fn}.jar ../{fn}.class")
	return fn

def run_jar(fn):
	os.system(f"java -jar {fn}.jar")