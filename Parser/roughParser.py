import subprocess

#Simple function which converts three strings to a string in TPTP form
def vampDecorator(str1, str2, str3):
    return ''+str2+'('+str1+','+str3+')'

#Currently unused
#Takes all variables and places them into a 'for all' TPTP definition block
def forAllDecorator(lst):
    presence_dict = {}
    key_count = 0
    for i in range(len(lst)-1):
        if(len(lst[i]) < 2 and lst[i] not in presence_dict):
            presence_dict[lst[i]] = 1
    string = '! ['
    for i in presence_dict.keys():
        key_count += 1
        if(len(presence_dict.keys())==key_count):
            string+=i+']:\n'
        else:
            string+=i+', '
    return string

#Takes a list of strings, and creates a conjecture named thm1 to insert in a TPTP file
#for Vampire to read
def vampFileFormat(lst):
    initString='fof(thm1,conjecture,((\n'
    #initString+=forAllDecorator(lst2)
    for i in range(len(lst)-1):
        initString+='('+lst[i]+')'
        if(i < len(lst)-2):
            initString+='\n&'
        else:
            initString+='\n'
    initString+='=>'+lst[-1]+'))).'
    return initString

#Forms the list of subjects within the sentence
def findSubject(byteString):
    #Loop through the string produced by the Stanford parser
    notFound = False
    ownershipClaim = False
    ownershipCount = 0
    subjectList=[]
    for i in range(1, len(output)-1):
        j = 3
        strings = ''
        #If we find the term 'NN' in our tree, we have either something to perform or a variable
        if(output[i] == ord('N') and output[i+1] == ord('N')):
            #We look through the string, copying down characters until we reach a closing parens
            while(output[i+j] != ord(')')):
                #print(chr(output[i+j]))
                strings+=chr(output[i+j])
                j+=1;
            #Add the string we found to the list of subjects
            if(notFound is True):
                subjectList.append('~'+strings)
                notFound = False
            else:
                subjectList.append(strings)
            if ownershipClaim is True and ownershipCount == 1:
                ownershipCount = 0
                ownershipClaim = False
                subjectList[-1], subjectList[-3] = subjectList[-3], subjectList[-1]
            elif ownershipClaim is True:
                ownershipCount += 1
        elif(output[i] == ord('R') and output[i+1] == ord('B') and output[i+3]!=ord('t')):
            #Found RB, so we have not in operator
            notFound = True 
        elif(output[i] == ord('h') and output[i+1] == ord('a') and output[i+2] == ord('s')):
            ownershipClaim = True
    return subjectList



#Takes the argument we would like to test, then passes through using the Stanford parser
#to produce a tree to parse, and eliminates the \n from the end of the string
passArg = input('Please enter the claim you wish to test:\n')
output = subprocess.check_output(["python", "stanfordParse.py", passArg])
output = output[:-2]
#print(output)
#Initialize lists for future use

varMethodList = []
#forAlls = []

subjectList = findSubject(output)

#for i in subjectList:
#    print(i)


#Decorate each pair of three subjects

for i in range(int(len(subjectList)/3)):
    vampString = vampDecorator(subjectList[3*i],subjectList[(3*i)+1],subjectList[(3*i)+2])
    varMethodList.append(vampString)

#for i in varMethodList:
#    print(i)
#Convert our formatted text to a full conjecture
vampText=vampFileFormat(varMethodList)
print(vampText + '\n')

vampFile = open('vampRead.tptp', 'a')
axioms = open('axioms/algebraAxioms.tptp', 'r')
for line in axioms:
    vampFile.write(line)
axioms.close()

#Place our converted text into a file for reading
vampFile.write(vampText)
vampFile.close()

#Run Vampire on our converted file
print(subprocess.check_output(['./vampire_rel_master_4011', 'vampRead.tptp']).decode('utf-8'))

#Remove the file when we finish with it (Optional step for now, but plan to use append to a copied file of axioms, so will be non-optional in the future
subprocess.call(['rm', 'vampRead.tptp'])
