import subprocess

def vampDecorator(str1, str2, str3):
    return ''+subjectList[(3*i)+1]+'('+subjectList[(3*i)]+','+subjectList[(3*i)+2]+')'

def vampFileFormat(lst):
    initString='fof(thm1,conjecture,((\n'
    for i in range(len(lst)-1):
        initString+='('+lst[i]+')'
        if(i < len(lst)-2):
            initString+='\n&'
        else:
            initString+=')\n'
    initString+='=>'+lst[-1]+')).'
    return initString


parens = -2
passArg = input()
output = subprocess.check_output(["python", "stanfordParse.py", passArg])
output = output[:-2]
#print(output)
subjectList = []
varMethodList = []

for i in range(len(output)-1):
    j = 3
    strings = ''
    if(output[i] == ord('N') and output[i+1] == ord('N')):
        while(output[i+j] != ord(')')):
            #print(chr(output[i+j]))
            strings+=chr(output[i+j])
            j+=1;
        subjectList.append(strings)
for i in subjectList:
    print(i)

for i in range(int(len(subjectList)/3)):
    vampString = vampDecorator(subjectList[(3*i)+1],subjectList[(3*i)],subjectList[(3*i)+2])
    varMethodList.append(vampString)

#for i in varMethodList:
#    print(i)
vampText=vampFileFormat(varMethodList)
print(vampText)

vampFile = open('vampRead.tptp', 'a')
vampFile.write(vampText)
vampFile.close()

print(subprocess.check_output(['./vampire_rel_master_4011', 'vampRead.tptp']).decode('utf-8'))

subprocess.call(['rm', 'vampRead.tptp'])
