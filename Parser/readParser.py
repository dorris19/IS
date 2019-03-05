import subprocess
import glob
from treeRead import *

  #Takes a list of strings, and creates a conjecture named thm1 to insert in a TPTP file
  #for Vampire to read
def vampFileFormat(lst, string):
    initString='fof(thm1,conjecture,((\n'
    initString+=string+'('
    for i in range(len(lst)-1):
        initString+='('+lst[i]+')'
        if(i < len(lst)-2):
            initString+='\n&'
        else:
            initString+='\n'
    initString+='=>'+lst[-1]+')))).'
    return initString

#Simple function which converts three strings to a string in TPTP form
def vampDecorator(str1, str2, str3):
      return ''+str1+'('+str2+','+str3+')'


#Takes the argument we would like to test, then passes through using the Stanford parser
#to produce a tree to parse, and eliminates the \n from the end of the string
PassArg = input('Please enter the claim you wish to test:\n')
output = str(subprocess.run(["python", "stanfordParse.py", PassArg], capture_output=True).stdout, 'UTF-8')
#New part to change product and sum
baseTree = children(output,0)[0][0]
print(baseTree)
sLocations = find_all(baseTree,'S')
print(sLocations)
statementList = []
for i in sLocations:
    treeForNN = children(baseTree, i)[0]
    for j in range(len(treeForNN)):
        checkIfNP = treeForNN[j]
#        print(j)
        if(len(checkIfNP) > 3):
            #if(checkIfNP[1] +checkIfNP[2] != 'NP'):
                #print('Who cares about this one!\n')

            #else:
            if(checkIfNP[1] +checkIfNP[2] == 'NP'):
#                print('There is vital information here!\n')
#                print(treeForNN[j])
                #childrenOfNP = children(checkIfNP,0)[0]
                #print(childrenOfNP[1])
                if(type(treeForNN[1])==None):
                    statement = NN(treeForNN, j)
                    statementList.append(statement)
                    print(statement)
                elif(treeForNN[1][1]+treeForNN[1][2]=='PP'):
                    statement = NP_PP(treeForNN, j)
                    statementList.append(statement)
                    print(statement)
                elif(treeForNN[1][1]+treeForNN[1][2]=='VP'):
                    statement = NP_VP(treeForNN, j)
                    statementList.append(statement)
                    print(statement)
print(statementList)
claimList=[]
forAllList=[]
for i in statementList:
    if i[1] not in forAllList:
        forAllList.append(i[1])
    if i[2] not in forAllList:
        forAllList.append(i[2])
    #if i[0] == '=' or i[0] == '!=':
    #    claim = i[1] + ' ' + i[0] + ' ' + i[2]
    claim = vampDecorator(i[0],i[1],i[2])
    claimList.append(claim)
forAllString = '!['
for i in forAllList:
    forAllString += i + ':$i'
    if forAllList.index(i) < len(forAllList) - 1:
        forAllString+=', '
forAllString+=']: \n'
print(forAllString)
present = 0
for i in claimList:
    if 'set' not in i and 'element' not in i:
        present = 1
if present == 1:
    convertClaims = vampFileFormat(claimList, forAllString)
else:
    convertClaims = vampFileFormat(claimList, '')
convertClaims = convertClaims.replace('is', 'equals')
convertClaims = convertClaims.replace('does', 'equals')
#while('sum' in convertClaims or 'product' in convertClaims):
#    holder1 = ''
#    holder2 = ''
#    split = convertClaims.find('equals')
#    loc = split + len('equals(')
#    while(convertClaims[loc]!=','):
#        holder1+=convertClaims[loc]
#        loc+=1
#    loc+=2
#    while(convertClaims[loc]!=')'):
#        holder2+=convertClaims[loc]
#        loc+=1
#    convertClaims = convertClaims[:split] + holder1 + ' = ' + holder2 + convertClaims[split+len(holder1)+len(holder2)+10]
print(convertClaims)

vampFile = open('vampRead.tptp', 'a')
if 'element' in convertClaims or 'set' in convertClaims:
    axioms = open('axioms/setAxioms.tptp', 'r')
#elif 'sum' in convertClaims or 'product' in convertClaims:
else:
    axioms = open('axioms/algebraAxioms.tptp', 'r')
#else:
#    axioms = open('axioms/absoluteGeometryAxioms.tptp', 'r')
#axiomFiles = glob.glob("axioms/*.tptp")
#print(axiomFiles)
#for i in axiomFiles:
#    axioms = open(i, 'r')
#    for line in axioms:
#        vampFile.write(line)
for line in axioms:
    vampFile.write(line)
axioms.close()
          
#Place our converted text into a file for reading
vampFile.write(convertClaims)
vampFile.close()
              
#Run Vampire on our converted file
print(subprocess.check_output(['./vampire_rel_master_4011', 'vampRead.tptp']).decode('utf-8'))
                  
#Remove the file when we finish with it (Optional step for now, but plan to use append to a copied file of axioms, so will be non-optional in the future
subprocess.call(['rm', 'vampRead.tptp'])
