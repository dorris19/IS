#Returns the children of a given parent in a tree
#The parent is defined by their position in the tree,
#it is expected that this is used in conjuntion with
#find or find_all
def children(tree, parent_start_index):
    #Keep track of parens, have somewhere to put
    #children, and have away to start mid-tree
    parenCount = 0
    childList = []
    child = ''
    #Guarantees a successful start by beginning at the start
    #of a part of speech. As this seeks forwards, the parent tag
    #will not be included in the resulting child string
    treePos = parent_start_index
    while(parenCount>=0 and (treePos+1)<len(tree)):
        child = ''
        #We have a problem if we hit a close parens before an open!
        #means either the end of a section of children or a poor start
        #but we eliminate poor start above
        while(tree[treePos]!='(' and (treePos+1)<len(tree)):
            if(tree[treePos]==')'):
                parenCount= -1
            treePos+=1
        parenCount=1
        child+='('
        treePos+=1
        while(parenCount>0 and (treePos+1)<len(tree)):
#            print(treePos)
#            print(tree[treePos])

            child+=tree[treePos]
            if(tree[treePos]=='('):
                parenCount+=1
            if(tree[treePos]==')'):
                parenCount-=1
#            print(parenCount,'\n')
            treePos+=1
        childList.append(child)

    #new index is returned for use in a later function
    #will be removed if no longer necessary due to changes
    child+=')'
    childList.append(child)
    return childList, treePos+parent_start_index

#Grabs a word from a pos tag block by cycling through non close parens or space characters
def word(element, posTarget, shift=0):
    pos=''
    i=element.find(posTarget,shift)
    while(element[i]!=' '):
        i+=1
    i+=1
    while(element[i]!=')'):
        pos+=element[i]
        i+=1
    return pos, i+shift

#Courtesy of StackOverflow user Pratik Deoghare
def find_all(a_str, sub):
    start = 0
    locList = []
    while True:
        start = a_str.find(sub, start)
        if start == -1: return locList
        locList.append(start)
        start += len(sub) # use start += 1 to find overlapping matches
    return locList

def check_not(a_str, stopVal):
    if(a_str.find('not',0,stopVal)!=-1):
        return True
    else:
        return False

#Used when NP breaks down to NP and PP, function will be in the NP
#and will be something like 'equals', while the two variables will
#be in the PP
def NP_PP(lst, j):
    function = word(lst[j],'NN')[0]
    variable_location = find_all(lst[j+1],'NN')
    variable1 = word(lst[j+1],'NN')[0]
    variable2 = word(lst[j+1],'NN',shift=variable_location[1])[0]
    print(lst[j])
    if(check_not(lst[j],word(lst[j+1],'NN')[1])):
        function='~'+function
    clause = [function, variable1, variable2]
    return clause

#Used when NP breaks down to NP and VP, finds variable in first NP then
#gets the rest from the VP
def NP_VP(lst, j): 
    variable1 = word(lst[j],'NN')[0]
    #print(variable1)
    print(lst)
    tree = children(children(lst[j+1], 0)[0][1],0)[0] 
    print(tree) 
    variable_location = find_all(lst[j+1],'NN')
    #print(variable_location)
    function = word(tree[0],'NN')[0]
    #print(function)
    variable2 = word(tree[1],'NN',shift=variable_location[0]+1)[0]
    #print(variable2)
    if(check_not(lst[j+1],word(tree[1],'NN')[1])):
        function='~'+function 
    clause = [function, variable1, variable2] 
    if 'VBZ' in variable2:
        print("hi!")
        variable1 = word(lst[j],'NN')[0]
        #print(variable1)
        tree = children(children(lst[j+1], 0)[0][1],0)[0] 
        print(tree) 
        variable_location = find_all(lst[j+1],'NN')
        #print(variable_location)
        function = word(tree[0],'VBZ',shift=len('VBZ'))[0]
        #print(function)
        variable2 = word(tree[1],'NN',shift=variable_location[0])[0]
        #print(variable2)
        if(check_not(lst[j+1],word(tree[1],'NN')[1])):
            function='~'+function 
        clause = [function, variable1, variable2]
    return clause 


#We know where the NP ends here, so get the children of its sibling
def NN(lst, j):
    variable1 = word(lst[j],0)[0]
    VP = children(lst[j+1], 0)
    NP = children(VP[0][1], 0)
    function = word(VP[0][0],'VBZ')[0]
    if(VP[0][1].find('CD')!=-1):
        valType = 'NN'
    else:
        valType = 'CD'
    variable2 = word(VP[0][1],valType)[0]
    print(lst[j+1])
    if(check_not(lst[j+1],word(VP[0][1],valType)[1])):
        function='~'+function 
    clause = [function, variable1, variable2]
    return clause
