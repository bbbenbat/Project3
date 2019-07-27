from cx_Freeze import setup, Executable
import os.path

#Permet d'éviter une erreur de type "KeyError: TCL_LIBRARY"
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
options = {
    'build_exe': {
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ],
    },}

#Si vous souhaitez pouvoir exporter sur un autre système d'exploitation, ces lignes sont nécessaires.
base = None
if sys.platform == "win32":
    base = "Win32GUI"

#Fichier que l'on souhaite inclure dans le dossier de l'exécutable
includefiles = ["yubilogo.ico", "yubilogo.png"]

#Paramètres de l'exécutable
target = Executable(
    script = "yubicode.py",
    copyright= "Copyright © 2018 YubiGeek.com",
    icon = "yubilogo.ico",
    base = base)

setup( name = "YubiCode",
	version = "0.1" ,
	description = "" ,
	options = {'build_exe': {'include_files':includefiles}},
	executables = [target])