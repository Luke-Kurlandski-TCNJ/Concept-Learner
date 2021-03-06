"""
Vihan Patel, Suada Demirovic, Luke Kurlandski
March 2021

Implementation of the Find-S algorithm and vertification that it produces the trace found in class.

Structural description: 
    handleInput() reads the training examples from a .csv file and defines the values that X
    can be mapped to. getNewHyp() makes necessary changes to a hypothesis when a new positive
    example is passed through. getTraceForFindS() verifies the implementation of the Find-S 
    algorithm and main() prints the trace.

Run this program from the command line like

    > python3 find_s.py training_examples.csv

    where training_examples.csv is a formatted csv file with a header describing the features 
    and the target concept, then each row describing a training example that defaults to 
    training_examples.csv if nothing is specified.

"""

import csv
from os import path
import random
import sys

def handleInput():

    ###############################################################################################

    # Allows the user to supply the name of a csv file to use for concept learning as a command line argument.
    # Otherwise, a set of training examples will be automatically provided.
    
    file = sys.argv[1] if len(sys.argv) > 1 else 'training_examples.csv'

    if not path.exists(file):
        print(file, "could not be not found")
        sys.exit()

    ###############################################################################################
    
    # Read the csv file and find all the possible values that X (set of instances) can be mapped to

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
    print('The concept learning task maps X ->', outputs)
    print('For this csv file, the table header is', lines[0]) # Describes the attributes and EnjoySport.
    print()

    ###############################################################################################
    
    # Decide what value can X (set of instances) map to for the positive examples
        
    outputs = list(outputs)
    condition1 = (outputs[0].lower() == "no") & (outputs[1].lower() == "yes")
    condition2 = (outputs[0].lower() == "yes") & (outputs[1].lower() == "no")
    outputForPos = ''
    
    if(condition1):
        outputForPos = outputs[1]
        
    elif(condition2):
        outputForPos = outputs[0]
        
    #

    ##############################################################################################
    
    return [outputForPos, lines]

#

# Makes necessary changes to a hypothesis using a newly encountered positive example
# If it is not satisfied, replace the attribute with the next more general constraint that is satisfied by X.
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

# Produces the trace that is needed for task 2 of the project
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

# Prints output of the Find-S algorithm
# Prints the trace needed for task 2 of the project
def main():

    material = handleInput()
    outputForPos = material[0]
    linesInCsvFile = material[1]
    linesInCsvFile.pop(0)
    hypotheses = getTraceForFindS(linesInCsvFile, outputForPos)
    finalHyp = hypotheses[len(hypotheses) - 1]

    print()
    print('----------------------------------------')
    print('TRACE')
    for x in range(0, len(hypotheses)):
        string = 'h_' + str(x)
        print(string, ' =', hypotheses[x])
    #
    print()
    print('Final hypothesis =', finalHyp)
    print('----------------------------------------')
    print()
    
if __name__ == "__main__":

    main()
    
############################################################################################################################
