
import spacy
from spacy import displacy

def parseGenerator(ListTokens, pos):
    if(pos==0):
        return '('+tokenList[pos][0]
    elif(pos+1==len(ListTokens)):
        return tokenList[pos][0]+')'
    else:
        for j in range(i+1, len(tokenList)):
            if(tokenList[pos][1]==tokenList[j][1]): 
                for k in range(pos):
                    if(tokenList[pos][1]==tokenList[k][1]):
                        return tokenList[pos][0]
                return '('+tokenList[pos][0]
        return tokenList[pos][0]+')'


nlp = spacy.load('en')
#inpString=input()
inpString = "Prove that 2 + 2 = 4"
doc = nlp(inpString)
#displacy.serve(doc, style='dep')

tempList=[]
tokenList=[]
for token in doc:
    tempList.append(token.text)

    tempList.append(token.head.text)


    tokenList.append(tempList)
    tempList=[]

#print(tokenList)

parseString=''

for i in range(len(tokenList)): 
    parseString+=parseGenerator(tokenList, i)
print(parseString)
'''
    if(i==0):
        parseString+='('+tokenList[i][1]
    elif(i < len(tokenList)-1):
        for j in range(i+1, len(tokenList)):
            if(tokenList[i][1]==tokenList[j][1]): 
                for k in range(i):
                    if(tokenList[i][1]==tokenList[k][1]):
                        parseString+=tokenList[i][0]
                        break;
                parseString+=tokenList[i][0]+')' 
            break;
        else:
            parseString+=tokenList[j][0]+')'
            break;
    else:
        parseString+=tokenList[i][0]+')'
        break;
    parseString+= ' '
print(parseString)
'''
