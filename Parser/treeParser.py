import subprocess
#Takes the argument we would like to test, then passes through using the Stanford parser
#to produce a tree to parse, and eliminates the \n from the end of the string
passArg = input('Please enter the claim you wish to test:\n')
output = subprocess.check_output(["python", "stanfordParse.py", passArg])
output = output.decode('utf-8')
