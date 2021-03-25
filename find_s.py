
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

#prints output of the Find-S algorithm
#prints the trace needed for task 2 of the project
def Vihans_main():

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
    print('final hypothesis =', finalHyp)
    print('----------------------------------------')
    print()
    
############################################################################################################################

def find_s_iteration(current_hypothesis, new_training_example):
    
    """
    Run a single iteration of find-s algorithm, ie, the "stuff" in the 
        for loop, and return the new hypothesis.

    Arguments:
        current_hypothesis : list : the most current hypothesis to 
            generalize from, default is 
            ['NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL']
        new_training_example : (list, str) : the next training example
            to run through find-s algorithm
    
    Returns:
        next_hypothesis : list : having learned from the new training 
            example, returns the generalized hypothesis
    """

    answer = new_training_example[1]
    trainingEx = []
    
    for x in new_training_example[0]:
        trainingEx.append(x)
    #
    
    if(answer == 'no'):
    
        return current_hypothesis
        
    elif(answer == 'yes'):
    
        next_hypothesis = current_hypothesis
        
        for x in range(0, len(trainingEx)):
            if(next_hypothesis[x] == 'NULL'):
                next_hypothesis[x] = trainingEx[x]
            elif(next_hypothesis[x] != trainingEx[x]):
                next_hypothesis[x] = '?'
            #
        #
        
        return next_hypothesis
        
    #
    
def training_example_generator():
    
    """
    Generate random training example according to target concept
        <Sunny, Warm, ?, ?, ?, ?>.

    Returns:
        example : (list, str) : a tuple of the six attribute values and 
            the classification according to the target concept, 
            i.e., the return will be of form
            (
                [Sky, AirTemp, Humidity, Wind, Water, Forecast], 
                EnjoySport
            ) 
    """
    
    SkyVals = ['Sunny', 'Cloudy', 'Rainy']
    AirTempVals = ['Warm', 'Cold']
    humidityVals = ['Normal', 'High']
    windVals = ['Strong', 'Weak']
    waterVals = ['Warm', 'Cool']
    forecastVals = ['Same', 'Change']
    categories = [SkyVals, AirTempVals, humidityVals, windVals, waterVals, forecastVals]
    
    randNum = random.randint(0, 31)
    binaryNum = str(bin(randNum))[2:]
    for x in range(0, 5 - len(binaryNum)):
        binaryNum = '0' + binaryNum
    #
    randNum = random.randint(0, 2)
    binaryNum = str(randNum) + binaryNum
    
    indices = []
    for x in binaryNum:
        indices.append(int(x))
    #

    trainingEx = []
    for x in range(0, len(categories)):
        word = categories[x][indices[x]]
        trainingEx.append(word)
    #
    
    answer = 'no'
    
    if((trainingEx[0] == 'Sunny') & (trainingEx[1] == 'Warm')):
        answer = 'yes'
    #
    
    return (trainingEx, answer)

def examples_required_to_learn(target_concept):
    """
    Determine how many random training examples are required to learn a
        given target function using find-s algorithm.

    Arguments:
        target_concept : list : the target concept to learn

    Returns:
        num_examples: int : number of training examples required to 
            learn target concept
    """

    num_examples = 0

    while find_s_iteration(training_example_generator()) != target_concept:
        num_examples += 1

    return num_examples

def experimental_question(n=100):
    """
    Write the number of examples required to learn the target concept
        for n trials to a txt file.

    Arguments:
        n : int : number of trials to perform (should be >= 100)
    """

    target_concept = ['Sunny', 'Warm', '?', '?', '?', '?']

    number_of_required_examples = [
        examples_required_to_learn(target_concept) for i in range(n)
    ]

    with open('experimental_question.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(number_of_required_examples)

def main():

    experimental_question(1000)
    
if __name__ == "__main__":
    main()

