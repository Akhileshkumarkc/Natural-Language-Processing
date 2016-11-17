import nltk
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
#modules
debugFile = open('debug.out','w')
def DebugWrite(obj):
    debugFile.write(str(obj))
def DebugWriteNL(obj):
    DebugWrite(obj)
    DebugWrite("\n")
def DebugWriteSeperate():
    DebugWriteNL("**********************************************")
def printSynset(word,sent,synset):
    print("\n The Word to disambigated:"+word)
    print("\n The Sentence it occurs :\n")
    print(sent)
    print("\nSynset:")
    print(synset)
    print("\nMeaning of the word:")
    print(synset.definition())
    print("\n examples:")

    for example in synset.examples() :
        print(example)
        print("\n")
    print("\n")



def computeOverlap(lemsignature,lemcontext) :
    count =0
    DebugWrite("Matched words: ||")
    for token in lemcontext:
        for word in lemsignature:
            if(word == token):
                DebugWrite(word+"|")
                count+=1
    DebugWriteNL("|")
    return count




def simplifiedlesk(word,sent) :
    context = sent.split(" ")

    DebugWriteSeperate()
    DebugWriteNL("context")
    DebugWriteNL(context)

    # lematize
    lemcontext = [wnl.lemmatize(word) for word in context]
    DebugWriteNL("lemcontext")
    DebugWriteNL(lemcontext)
    synsets = wn.synsets(word)
    best_sense = synsets[0]
    max_overlap = 0

    for synset in synsets:

        examples = synset.examples()
        meaning =synset.definition()
        DebugWriteSeperate()
        DebugWriteSeperate()

        DebugWriteNL("synset:")
        DebugWriteNL(synset)
        DebugWrite("meaning :")
        DebugWriteNL(meaning)
        signature = []
        word =meaning.split()
       # signature.insert(len(signature),word)
        signature.extend(word)
        DebugWriteNL("Example:")
        for example in examples:


            DebugWriteNL(example)

            word = example.split()
            #signature.insert(len(signature),word)
            signature.extend(word)


        DebugWriteSeperate()
        DebugWriteSeperate()
        DebugWriteNL("signature:")
        DebugWriteNL(signature)
        DebugWriteSeperate()
        DebugWriteSeperate()
        lemsignature = [wnl.lemmatize(sign) for sign in signature]
        DebugWriteNL("lemsignature:")
        DebugWriteNL(lemsignature)
        overlap = 0
        overlap = computeOverlap(lemsignature,lemcontext)
        DebugWriteSeperate()
        DebugWrite("overlap =")
        DebugWriteNL(overlap)
        DebugWrite("max_overlap =")
        DebugWriteNL(max_overlap)
        DebugWriteSeperate()

        if(overlap > max_overlap):
            max_overlap = overlap
            best_sense = synset
            DebugWrite("synset Changed!!!")
            DebugWriteNL(synset)

    return best_sense



#    best_sense = ""
#    max_overlap = 0
#    context =sentence.split()
#    for sense in context :
#       signature
#       overlap = computerOverlap(signature,context)
#       if overlap > max_overlap then
#            max_overlap = overlap
#            best_sense =sense
#    return best_sense

#modules end

word ="run"
sent = "Hillary runs for President"

#sent ="The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities"
#word = "bank"
DebugWrite("word :")
DebugWriteNL(word)
DebugWrite("sent :")
DebugWriteNL(sent)

sense = simplifiedlesk(word,sent)
printSynset(word,sent,sense)

