# viterbi algo
# input Matrix Prob and Transition
# sequence.
# Need to find likely hood of the weater

#Hard coding Markov Model.

import sys
from _hashlib import new

#===============================================================================
# filename = sys.argv[1]
# file = open(filename, 'r')
#===============================================================================
debugFile = open('debug.out','w')

import re

# Modules

def DebugWrite(str1,obj):
    debugFile.write(str1)
    debugFile.write(str(obj))
def DebugWriteNL(str1,obj):
    DebugWrite(str1,obj)
    debugFile.write("\n")
def DebugWriteMatrix(Matrix):
    debugFile.write(str(Matrix))
    debugFile.write("\n")
def DebugWriteStr(str1):
    debugFile.write(str1)
    debugFile.write('\n')
def maxfunc(a,statea,b,stateb):
    if(a>=b):
        return a,statea
    else :
        return b,stateb
    

def ViterbiMethod(matrixStart,state,obMatrix,sequence) :
    seqlength = len(sequence)
    stateLength = len(state)
    VM = [[0.0 for i in range(stateLength)] for j in range(seqlength)]
    #0,0 nothing.
    BackpointerMatrix = [[3 for i in range(stateLength)] for j in range(seqlength)]
    for stateindex in range(stateLength) :
        VM[0][stateindex] = matrixStart[stateindex]   * obMatrix[(int(sequence[0])-1)][stateindex]
    seqIndex =1
    DebugWriteStr("Start Viterbi Algo")
    #Till End of Sequence
    while seqIndex < seqlength :
        evalstateIndex=0
        # Each State Viterbi Value for Each sequence
        while evalstateIndex < stateLength :
            stateIndex =0
            maxvalue =0;
            maxPrevState =0;
            #Debug
            if(seqIndex == 6):
                DebugWriteStr('debug now')
            #Iter to find max from the state
            while stateIndex < stateLength :
                avalue= (VM[seqIndex-1][stateIndex])* (MatrixHotCold[stateIndex][evalstateIndex])*obMatrix[int(sequence[seqIndex])-1][evalstateIndex]
                maxvalue,maxPrevState =maxfunc(maxvalue,maxPrevState,avalue,stateIndex)
                VM[seqIndex][evalstateIndex] = maxvalue
                BackpointerMatrix[seqIndex-1][evalstateIndex] = maxPrevState #sequence -1
                DebugWriteStr("***********************************************************")
                DebugWrite("seqIndex = ",seqIndex)
                DebugWriteStr("")
                DebugWrite("evalstateIndex = ",evalstateIndex)
                DebugWriteStr("")
                DebugWrite("Maxvalue", maxvalue)
                DebugWriteStr("")
                DebugWrite("maxPrevState", maxPrevState)
                DebugWriteStr("")
                DebugWriteStr("Three values:")
                DebugWrite("\n value 1 (previous Value)", VM[seqIndex-1][stateIndex])
                DebugWrite("\n value 2 (Hot/cold sequence)", MatrixHotCold[stateIndex][evalstateIndex])
                DebugWrite("\n value 3 (seq/(hot/cold)", obMatrix[int(sequence[seqIndex])-1][evalstateIndex])
                DebugWriteStr("\n fewmore")
                DebugWrite("\n stateIndex =",stateIndex)
                DebugWrite("\n evalstateIndex =",evalstateIndex)
                DebugWrite("\n VM[seqIndex][evalstateIndex] = maxvalue ",maxvalue)
                DebugWriteStr("\n***********************************************************")
                
                stateIndex+=1
            evalstateIndex+=1
        seqIndex+=1     
    DebugWriteStr("done")
    # End of Max,Min Calculation
    DebugWriteStr("===========================================================")
    i = 0
    while(i<seqlength):
        j=0
        DebugWrite("\n currentSequence:  ",(i))
        DebugWrite("  =  ",sequence[i])
        DebugWriteStr("\n")
        while(j<stateLength):
            DebugWrite('State ',j)
            DebugWrite('\t',VM[i][j])
            DebugWrite("Previous State(", (BackpointerMatrix[i-1][j]))
            DebugWriteStr(")")
            j+=1
        DebugWriteStr('')
        i+=1
    DebugWriteStr("===========================================================")
    
    # getSequence
    seqIndex = seqlength-1
    stateindex = stateLength-1
    maxiVal = 0
    maxState = 0
    while(stateindex >= 0):
        new = VM[seqIndex][stateindex]
        if(new>maxiVal):
            maxiVal = new
            maxState = stateindex
        stateindex-=1
    DebugWrite("\n maxvalue",maxiVal)
    seqIndex=seqlength
    stateSequence=[3 for i in range(seqIndex)]
    stateSequence[seqIndex-1] = maxState
    seqIndex-=1
    DebugWriteStr("\n SI : ")
    print("The most likely weather for the Sequence is",sequence)
    while(seqIndex >0):
        DebugWriteStr(str(seqIndex))
        stateSequence[seqIndex-1] =BackpointerMatrix[seqIndex-1][stateSequence[seqIndex]]
        seqIndex-=1
    for state in stateSequence:
        if(state == 0):
            print("Hot")
            DebugWriteStr("\t Hot")
        else:
            print("Cold")
            DebugWriteStr("\t Cold")

    

#End Module
#Matrix Structure.
# start,HOT,COLD, End.
# Start -HOT = .8 ,Start - cold =.2
#        HOT   COLD
# HOT    .7    .3
# COLD   .4    .6
#
MatrixStart = [.8,.2]
MatrixHotCold = [[.7,.3],[.4,.6]]
state = ['hot','cold']
#Matrix of 1,2,3 and HOt COLD 
##   Hot(0) COLD(1) 
#0 1  .2  .5
#1 2  .4  .4
#2 3  .4  .1
ObMatrix = [[.2,.5],[.4,.4],[.4,.1]]
DebugWriteNL("MatrixStart", MatrixStart)
DebugWriteNL("MatrixHotCold", MatrixHotCold)
DebugWriteNL("ObMatrix",ObMatrix)
#sequence1 = '331'
#sequence1 = '3311223'
sequence1 = '331122313'
sequence2 = '331123312'

sequence=sequence1
ViterbiMethod(MatrixStart,state,ObMatrix,sequence)
sequence=sequence2
ViterbiMethod(MatrixStart,state,ObMatrix,sequence)

