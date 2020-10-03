from subprocess import run
from elevate import elevate
from os import chdir ,getcwd
elevate(show_console=False)
current_dir = getcwd()
chdir(current_dir)
run("START cmd", shell=True)
