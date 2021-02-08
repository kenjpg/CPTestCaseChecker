import os
from subprocess import call
import check
import time
import pathlib

current_dir = pathlib.Path(__file__).parent.absolute()
print(current_dir)
settings = open(str(current_dir) + "/settings.txt", "r")

for line in settings:
    if (line.split("=")[0] == "env"):
        env_folder = line[3:].rstrip("\n").rstrip(" ").lstrip("=")

cpp_file = input("Enter Path: ")
problem = input("Problem: ")

task = problem[-1]
problem = problem[0:3]
problem_cd = "/".join([env_folder, problem, task]) + "/"

# Compiling with MINGW
os.system("g++ " + cpp_file + ' -std=c++17 -o '+"runcompile")

first = time.time()

list_INPUT = os.listdir(problem_cd+"in")
for file in list_INPUT:
    textfile = open(problem_cd+"in/"+file, 'r')
    writefile = open(problem_cd+"out/"+file.rstrip(".txt")+"check.txt",'w')
    rc = call(['runcompile'], stdin = textfile, stdout = writefile)

finaltime = time.time()
results = check.checkcase(problem_cd+"out/")

if results[-1].split(" | ")[0:2] == "WA":
    print(results[-1])
else:
    print("------------")
    print("| Accepted |")
    print("------------")
    
print("Time:",round((finaltime-first) * 1000),"ms")
