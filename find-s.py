import sys
from os import path
import csv

'''
Vihan Patel
Suada Demirovic
Luke Kurlandski
'''

def handleInput():

    ###############################################################################################

    #ask the user which csv file he/she wants to use for concept learning
    
    print()

    file = input('Enter a relative or absolute path to a csv file: ')
    index = file.find('.csv')
    
    if(index == len(file) - 4):
        value = path.exists(file)
        if(value == False):
            print()
            print('Sorry,', file, 'does not exist.')
            print()
            sys.exit(0)
        #
    else:
        print()
        print('Sorry,', file, 'is an invalid input.')
        print()
        sys.exit(0)
    #

    ###############################################################################################
    
    #read the csv file and find all the possible values that X (set of instances) can be mapped to

    outputs = []

    string = file
    file = open(file, 'r')
    reader = csv.reader(file)

    lines = []
    for row in reader:
        lines.append(row)
    #

    for x in range(0, len(lines)):
        word = lines[x][len(lines[x]) - 1]
        outputs.append(word)
    #

    outputs.pop(0)
    outputs = set(outputs)

    if(len(outputs) > 2):
        print()
        print('Sorry, concept learning cannot be done on ', file, '.')
        print()
        sys.exit(0)
    #

    print()
    print('For this csv file, X ->', outputs)
    print('For this csv file, the table header is', lines[0])
    print()

    ###############################################################################################
    
    #decide what value can X (set of instances) map to for the positive examples
        
    outputs = list(outputs)
    condition1 = (outputs[0].lower() == "no") & (outputs[1].lower() == "yes")
    condition2 = (outputs[0].lower() == "yes") & (outputs[1].lower() == "no")
    outputForPos = ''
    
    if(condition1):
    
        outputForPos = outputs[1]
        
    elif(condition2):
    
        outputForPos = outputs[0]
        
    else:
        
        value = input('For positive examples, do you want (X -> '  + outputs[0] + ')? ')
        
        if(value.lower() == "yes"):
            outputForPos = outputs[0]
        elif(value.lower() == "no"):
            outputForPos = outputs[1]
        else:
            print()
            print('Invalid response was given. You can only type a yes or no.')
            print()
            sys.exit(0)
        #
        
    #

    ##############################################################################################
    
    return [outputForPos, lines]

#

#makes necessary changes to a hypothesis using a newly encountered positive example
def getNewHyp(currHyp, line, outputForPos):
    
    if(line[len(line) - 1] == outputForPos):
        for x in range(0, len(line)):
            if(currHyp[x] == 'NULL'):
                currHyp[x] = line[x]
            elif(currHyp[x] != line[x]):
                currHyp[x] = '?'
            #
        #
    #
    
    return currHyp
        
#

#meant to produce the trace that we need for task 2 of the project
def getTraceForFindS(linesInCsvFile, outputForPos):

    length = len(linesInCsvFile[0])
    hyp = []

    for x in range(0, length):
        hyp.append('NULL')
    #

    copyOfHyp = []
    for x in range(0, len(hyp) - 1):
        copyOfHyp.append(hyp[x])
    #

    hypotheses = [copyOfHyp]

    for x in linesInCsvFile:
        hyp = getNewHyp(hyp, x, outputForPos)
        copyOfHyp = []
        for x in range(0, len(hyp) - 1):
            copyOfHyp.append(hyp[x])
        #
        hypotheses.append(copyOfHyp)
    #

    return hypotheses

#

#prints output of the Find-S algorithm
#prints the trace needed for task 2 of the project
def main():

    material = handleInput()
    outputForPos = material[0]
    linesInCsvFile = material[1]
    categories = linesInCsvFile[0]
    linesInCsvFile.pop(0)
    hypotheses = getTraceForFindS(linesInCsvFile, outputForPos)
    finalHyp = hypotheses[len(hypotheses) - 1]
    
    print()
    print('----------------------------------------')
    print()
    print('TRACE')
    for x in range(0, len(hypotheses)):
        string = 'h_' + str(x)
        print(string, ' =', hypotheses[x])
    #
    print()
    print('final hypothesis =', finalHyp)
    print('----------------------------------------')
    print()

#

main()
