@Author Akhilesh Kumar Kagalvadi Chinnaswamy
UTD ID : axk167131

Different files Needed:

sentProb.py - python program for both problems.
debug.out - debug logs.
The required output is put into the console.(Using print function.)

Please follow below steps to run the program.
 1) For the problem 1 of finding probabiity of any sentence please use below format : (p1)
    python sentProb.py p1 NLPCorpusTreebank2Parts.txt "This is any sentence"
 2) For the problem 2 of finding probabiity of the given 2 sentences please use below format : (p2)
   python sentProb.py p2 NLPCorpusTreebank2Parts.txt

   *Note : 'p1' and 'p2' stands for program 1 and program 2 in the output

Explanation of sample output is also attached. Describe how output comes.
Key aspects:
1) The output first mentions about whether it is p1 or p2.
     For program 1,
     Task find all Biagrams and probability for given sentence
     The Sentence is This is any sentence
     The Argument corpus value is NLPCorpusTreebank2Parts.txt
     The Total Word Count =  26349
     The Total Distinct Word Count = 4373
     
     For program 2,
     Find all Biagrams and Probability for 2 sentences
     The Argument corpus value is NLPCorpusTreebank2Parts.txt
     The Total Word Count =  26349
     The Total Distinct Word Count = 4373

2) Matrix values printed might have tab spacing problem due to words being of different length, so kindly read it accordingly, if it side tracked.

3) The probability of sentence is calculated at end for each operation.
4) The sentence with higher probability is the one that is more probable.

Assumptions and Limitation:
1) Token : '.' is tokenized, but not considered for word count. so if there is a structure like end. Start, then for biagram count of (end start) this is not counted.
2) The comparsion is not case sensitive. (The corpus words are converted to small and compared.)
3) The program caculates monogram probailities that should be ignored.
4) Incase of good turing smoothing, if Nc gets 0 count, this causes a problem for the new count.
        which is C* = (C+1) * (Nc+1/Nc). 
    in this case, For simplicity i have considered. the next Nc+1 that has some occurence. 
    for example: if N3 =0 , N4= 1, N2 = 4. then here i consider N4.(for simplicity)
    Good turing probability = C* / (unigramcount +total frequency in table). 
    // for simplicty as we are calculting biagram counts only for the sentence.
5) For the probability of sentence, beginning of sentence and end of sentence probability are not considered. As in this execrise, i have not considered
    the tokenization of end sentence and begin of sentence, Which is needed for them.
    That can be done by calculating biagram count of start of sentence word followed by '.' and Then last word sentence followed by "."
    That is not considered for this program
   