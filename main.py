import subprocess as sp, os;
import gpulist
import gpudetect
debugMode = True;
#Fuck this will probably be abandoned soon, im still gonna try though

print("Welcome, What would you like to do?")
print("1) Detect GPUs")

curentChoice = input();

match curentChoice:
    case "1":
        print("test")
