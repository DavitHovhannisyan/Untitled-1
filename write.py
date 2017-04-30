from os import *
import sys

file = open("bpm.txt", "w")
file.write(sys.argv[1])
file.close()
    
