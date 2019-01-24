#Returns the children of a given parent in a tree
#The parent is defined by their position in the tree,
#it is expected that this is used in conjuntion with
#find or find_all
def children(tree, parent_start_index):
    #Keep track of parens, have somewhere to put
    #children, and have away to start mid-tree
    parenCount = 0
    childList = []
    #Guarantees a successful start by beginning at the start
    #of a part of speech. As this seeks forwards, the parent tag
    #will not be included in the resulting child string
    treePos = tree.find('(', parent_start_index)
    while(parenCount!=-1):
        #We have a problem if we hit a close parens before an open!
        #means either the end of a section of children or a poor start
        #but we eliminate poor start above
        while(tree[treePos]!='('):
            #We've hit the end of the section so leave
            if(tree[treePos]==')'):
                parenCount -= 1
            treePos+=1
        #Child is set with an open parens for use in recursive searchings
        child='('
        treePos+=1
        parenCount=1
        #Bookkeeping to know if we are within a branch
        while(parenCount != 0):
            if(tree[treePos]=='('):
                parenCount+=1
            if(tree[treePos]==')'):
                parencount-=1
            child+=tree[treePos]
            treePos+=1
        #append a close parens to child for use in further runs
        #maybe an arbitrary open should follow?
        child+=')'
        childList.append(child)
    #new index is returned for use in a later function
    #will be removed if no longer necessary due to changes
    return childList, treePos+parent_start_index

#Grabs a word from a pos tag block by cycling through non close parens or space characters
def word(element):
    pos = 0
    i=0
    while(element[i]!=' '):
        i+=1
    while(element[i]!=')'):
        pos+=element[i]
        i+=1
    return element

#Should take a pos tagged segment and find the
#desired children of it as words. Should allow modularity
#regarding multiargument statements
def findPartOfSpeech(lst, tag):
    position = -1
    wordList = []
    while(True):
        parenCount = 1
        position = lst.find(tag,position+1)
        if(position==-1):
            break
        desiredWord = word(lst[position:])
        wordList.append(desiredWord)
    return wordList

#Change the following functions to use findPartOfSpeech
#should make them simpler and more modular.

#Used when NP breaks down to NP and PP, function will be in the NP
#and will be something like 'equals', while the two variables will
#be in the PP
def NP_PP(lst):
    function = word(lst[0])
    tree = children(lst[1], 0)
    variable_location = children(tree[1], 0)
    variable1 = word(variable_location[0])
    variable2 = word(variable_location[2])
    clause = [function, variable1, variable2]
    return clause

#Used when NP breaks down to NP and VP, finds variable in first NP then
#gets the rest from the VP
def NP_VP(lst):
    variable1 = word(lst[0])
    tree = children(lst[1], 0)
    variable_location = children(tree[1], 0)
    function = word(variable_location[0])
    variable2 = word(variable_location[1])
    clause = [function, variable1, variable2]
    return clause 

#We know where the NP ends here, so get the children of its sibling
def NN(tree, lst, endPos):
    variable1 = word(lst[0])
    sibling = children(tree, endPos)
    NP = children(VP[1])
    function = word(children(children(NP)[0])[2])
    variable2 = word(children(children(NP)[1])[1])
    clause = [function, variable1, variable2]
    return clause
