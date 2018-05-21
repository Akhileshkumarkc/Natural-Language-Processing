'''
Created on Sep 21, 2016

@author: Akhilesh
'''
# #recog word.##

import sys


program = sys.argv[1]
if(program == 'p1'):
    print ("Task find all Biagrams and probability for given sentence")
    sent1 = sys.argv[3]
    print ('The Sentence is',sys.argv[3])

if(program == 'p2'):
    print("Find all Biagrams and Probability for 2 sentences")
filename = sys.argv[2]
print('The Argument corpus value is', filename)
# print('Number of arguments:', len(sys.argv), 'arguments.')# print('Argument List:', str(sys.argv))

file = open(filename, 'r')
debugFile = open('debug.out','w')



import re

# Modules

def DebugWrite(obj):
    #Write Debug Object
    debugFile.write(str(obj))
def DebugWriteNL(obj):
    DebugWrite(obj)
    DebugWrite("\n")
    
def findCountIn(row,col,sentStrings,filename):
    count = 0
    file1 = open(filename, 'r')
    patternStrings = re.findall('['+sentStrings[row]+'[\b]+'+ sentStrings[col]+']', file1.read())
    count = len(patternStrings)
    print(patternStrings)
    return count;
 
       
def findCount(row, col, SentStrings, extractedStrings):
    i, countString = 0, 0
    while i < len(extractedStrings) - 1:  
 #       print(extractedStrings[i] ,extractedStrings[i + 1])      
        if ((extractedStrings[i] == SentStrings[row]) & (extractedStrings[i + 1] == SentStrings[col])) :
            countString = countString + 1
        i = i + 1

#    print("find Count Ends")
    DebugWrite(row),DebugWrite(col),DebugWrite(SentStrings[row]),DebugWrite(SentStrings[col]),DebugWriteNL(countString)
    return countString;

def findBiProb(row, col, SentStrings, extractedStrings,countBiMatrix):
    word = SentStrings[row]
    if (word in WordDict):
        wordCount = WordDict[word];
        if wordCount == 0.0000:
            return 0.0000
        else :
            return (countBiMatrix[row][col])/(wordCount)
    else :
        return 0.0000

#findBi1smoothProb

def findBi1smoothProb(row, col, SentStrings, extractedStrings,countBiMatrix):
    word = SentStrings[row]
    if (word in WordDict):
        wordCount = WordDict[word]
    else :
        wordCount = 0.0000
    return (countBiMatrix[row][col]+1)/(wordCount+distinctWordCount)
    


def printf(var):
    print(var, end='')


   

def displayMatrixTable(SentStrings, Matrix, SentLen,name):
    printf("***********************************")
    printf(name)
    print("************************************")
    printf('\t\t')
    
    for string in SentStrings:
        printf(string)
        printf('\t')
    print('') 
    for i in range(SentLen):
        printf(SentStrings[i])
        printf('\t')
        for j in range(SentLen):
            printf('\t')
            printf(Matrix[i][j])
        print('')
    printf("***********************************")
    printf("Displaying Table")
    print(" Ends***********************************")
    print("")       

def findAllProb(sent1) :
    # biagram.
    print("************************************* Start of the Sentence Calculation *************************************")
    SentStrings = re.findall('[\w/-/%@#%^&/*\']+', sent1)
    SentStrings = [word.lower() for word in SentStrings]
    print("Sentence:",sent1)
    DebugWrite(sent1)
    DebugWrite(SentStrings)
    
    SentLen = len(SentStrings)
    #===========================================================================
    # monogram.
    #===========================================================================
    # monogram.
    monogram = [0.00000 for j in range(SentLen)]
    monogramWc = [0 for j in range(SentLen)]
    i=0
    for row in range(SentLen) :
        word = SentStrings[i]
        if (word in WordDict): 
            wordCount = WordDict[word]
        else :
            wordCount = 0
        monogramWc[i] = wordCount
        monogram[i] = wordCount/distinctWordCount
        i+=1
    print("MonoGram Count")
    print(monogramWc)
    print("MonoGram Probability")
    print(monogram)
    # monogram with 1 smoothing.
    i=0
    monogram1smoothing = [0.00000 for j in range(SentLen)]
    
    for row in range(SentLen) :
        word = SentStrings[i]
        monogram1smoothing[i] = (monogramWc[i] +1)/distinctWordCount
        i+=1
    print("Monogram with 1 Smoothing")
    print(monogram1smoothing)
    #===========================================================================
    # Bi Gram
    #===========================================================================
    # 1. Count Bi Matrix.              
    countBiMatrix = [[0.00000 for j in range(SentLen)] for i in range(SentLen)]
    DebugWrite(countBiMatrix)
    for row in range(SentLen) :
        for col in range(SentLen):
            countBiMatrix[row][col] = findCount(row, col, SentStrings, extractedStrings)
    #        countBiMatrix[row][col] = findCountIn(row, col, SentStrings,filename)
            DebugWrite(row)
            DebugWrite(col) 
            DebugWrite(countBiMatrix[row][col])
    
    
    
    print("count Bigram Matrix")
    displayMatrixTable(SentStrings, countBiMatrix, SentLen,"1.count Biagram Matrix")
    
    DebugWriteNL(countBiMatrix)
    
    # 2. Prob Bi Matrix (diagram)
    probBiMatrix = [[0.00000 for j in range(SentLen)] for i in range(SentLen)]
    
    for row in range(SentLen) :
        for col in range(SentLen):
            probBiMatrix[row][col] = findBiProb(row, col, SentStrings, extractedStrings,countBiMatrix)
    #        print(row, col, probBiMatrix[row][col])
    print("BiGram Probability")
    displayMatrixTable(SentStrings, probBiMatrix, SentLen,"2. BiGram Probability")
    
    DebugWriteNL(probBiMatrix)   
        
    countBi1SmoothMatrix = [[0.00000 for j in range(SentLen)] for i in range(SentLen)]
    
    for row in range(SentLen) :
        for col in range(SentLen):
            countBi1SmoothMatrix[row][col] = countBiMatrix[row][col] + 1
    #        print(row, col, probBiMatrix[row][col])
    print("1Smoothing counting")
    displayMatrixTable(SentStrings, countBi1SmoothMatrix, SentLen,"3. 1-Smoothing counting")
    # 3.Prob Bi Matrix (diagram)
    probBi1SmoothMatrix = [[0.00000 for j in range(SentLen)] for i in range(SentLen)]
    
    for row in range(SentLen) :
        for col in range(SentLen):
            probBi1SmoothMatrix[row][col] = findBi1smoothProb(row, col, SentStrings, extractedStrings,countBiMatrix)
    #        print(row, col, probBiMatrix[row][col])
    print("1Smoothing Probabilty")
    displayMatrixTable(SentStrings, probBi1SmoothMatrix, SentLen,"4. 1-Smoothing probability")
    
    DebugWriteNL(probBiMatrix)  
     
    print("count of Good Turing Smoothing")
    countBiDiscntMatrix = [[0.00000 for j in range(SentLen)] for i in range(SentLen)]
    for row in range(SentLen) :
        for col in range(SentLen):
            countBiDiscntMatrix[row][col] = countBiMatrix[row][col]
        
    displayMatrixTable(SentStrings, countBiDiscntMatrix, SentLen,"5a. count before Good Turing Smoothing")
    
    # Discount Frequency Matrix.
    countDict ={}
    totalFreqcount = 0
    for row in range(SentLen) :
        for col in range(SentLen):
            val =countBiDiscntMatrix[row][col]
            if (not(val in countDict)):
                countDict[val] = 1
                continue
            else :
                countDict[val] = (countDict.get(val) + 1)
                nextStr = extractedSortedStrings[i]
                continue
    print("Count of Frequency of the Biagram Occurence")
    print(countDict)
    print("Count of Frequency of the Biagram Occurence")
    DebugWriteNL(countDict)
    newCountDict = copy.copy(countDict)
    for key in countDict.keys() :
        totalFreqcount +=  countDict[key]   
    print(totalFreqcount)
    # contains <count, adjusted count>
     
    keys = sorted(countDict.keys())
    i=0
    while i < len(keys)-1:
        countKey =keys[i]
        DebugWrite("countkey   CountDict[countkey]") 
        DebugWrite(countKey)
        DebugWrite("    ")
        DebugWrite(countDict[countKey])
        count = countDict[countKey]
        nextCountKey = keys[i+1]
        if(nextCountKey in countDict) :
            newCount = (countKey+1)*((countDict[nextCountKey])/(countDict[countKey]))
            # C* =(c+1) * (N(c+1),N(c))
            newCountDict[countKey] = newCount
            DebugWrite("    ")
            DebugWriteNL(newCount)
        i+=1
    # add the new counts and construct the count table.
    for row in range(SentLen) :
        for col in range(SentLen):
            val =countBiDiscntMatrix[row][col]
            if(val in newCountDict) :
                val = newCountDict[val]
                countBiDiscntMatrix[row][col] =val
    displayMatrixTable(SentStrings, countBiDiscntMatrix, SentLen,"5b. count after Good Turing Smoothing")
    
    # Construct the Probabilty Bi Discounting table.
    probBiDiscntMatrix = [[0.00000 for j in range(SentLen)] for i in range(SentLen)]
    DebugWriteNL(probBiDiscntMatrix)
    DebugWrite("DiscountMatrix")
    for row in range(SentLen) :
        for col in range(SentLen):
            word = SentStrings[row]
            if (word in WordDict):
                wordCount = WordDict[word]
            else:
                wordCount = 0
            probBiDiscntMatrix[row][col] = ((countBiDiscntMatrix[row][col])/(wordCount+totalFreqcount))
            #===================================================================
           
                            # DebugWrite("probaDis value =")
            #===================================================================
            DebugWrite(probBiDiscntMatrix[row][col] )
            DebugWrite("Count Value =")
            DebugWrite(countBiDiscntMatrix[row][col])
            DebugWrite("totalWordCount =")
            DebugWriteNL(totalWordCount)
    
    displayMatrixTable(SentStrings, probBiDiscntMatrix, SentLen,"6. Probability for Good Turing Smoothing")
    
    #sent start count
    countStart = 0
    i =0
    while i < (len(extractedStrings) - 2):  
        if ((extractedStrings[i] == '.') & (extractedStrings[i+1] == SentStrings[0])) :
            countStart = countStart + 1
        i = i + 1
    probstart = countStart/WordDict['.']
    print(probstart)
    #sent end count
    countEnd,i = 0,0
    while i < len(extractedStrings) - 1:  
        if ((extractedStrings[i] == SentStrings[SentLen-1]) & (extractedStrings[i + 1] == '.')) :
            countStart = countStart + 1
        i = i + 1
    probEnd = countEnd/WordDict['.']
    print(probEnd)
    
    i=0
    probSent=1
    while (i < SentLen-1):
        probSent = probSent * probBiMatrix[i][i+1]
        i+=1
    printf("The Probability of the Sentence using No Smoothing")
    printf("=")
    print(probSent)
    
    i=0
    probSent=1
    while (i < SentLen-1):
        probSent = probSent * probBi1SmoothMatrix[i][i+1]
        i+=1
    printf("The Probability of the Sentence using 1Smoothing")
    printf("=")
    print(probSent)   
    
    i=0
    probSent=1
    while (i < SentLen-1):
        probSent = probSent * probBiDiscntMatrix[i][i+1]
        i+=1
    printf("The Probability of the Sentence using Good Turing Discount")
    printf("=")
    print(probSent) 
    
    print("\n************************************* End Sentence Calculation *************************************\n")



# Modules End


# Matching words.
#extractedStrings = re.findall('[\w/-/%@#%^&/*\']+', file.read())
# Match '.' as well.




extractedStrings = re.findall('[\w/-/%@#%^&/*\']+|[.]', file.read())
extractedStrings = [string.lower() for string in extractedStrings]
    
DebugWriteNL(extractedStrings)
import copy
extractedSortedStrings = copy.copy(extractedStrings)   
extractedSortedStrings.sort()
DebugWriteNL("String that is sorted...")
DebugWriteNL(extractedSortedStrings)
DebugWriteNL("String that is not sorted")
DebugWriteNL(extractedStrings)

# remove
# extractedStrings =['abc','abc','def','def']
WordDict = {}
i = 0
while (i < len(extractedSortedStrings)):
#    print(i)
    if (not(extractedSortedStrings[i] in WordDict)):
        WordDict[extractedSortedStrings[i]] = 1
        i = i + 1
        continue        
    else :
        currStr = extractedSortedStrings[i]
        nextStr = extractedSortedStrings[i + 1]          
        while (nextStr == currStr) :
            i = i + 1
            WordDict[currStr] = (WordDict.get(currStr) + 1)
            nextStr = extractedSortedStrings[i]
            continue
        i = i + 1
    

DebugWriteNL(WordDict)

totalWordCount = len(extractedStrings)-WordDict['.']
print("The Total Word Count = ", totalWordCount)
distinctWordCount = len(WordDict) - 1
print("The Total Distinct Word Count =",distinctWordCount)
#===============================================================================
# if(not(sys.argv[2] == 1)):
#     findAllProb(sent1)
# else:
#     sent1 = "The president has relinquished his control of the company's board."
#     sent2 = "The chief executive officer said the last year revenue was good."
#     findAllProb(sent1);
#     findAllProb(sent2);
#===============================================================================
if(program=='p1'):
    findAllProb(sent1)
if(program=='p2'):
    sent_1 = "The president has relinquished his control of the company's board."
    sent_2 = "The chief executive officer said the last year revenue was good."
    findAllProb(sent_1);
    findAllProb(sent_2);




     


