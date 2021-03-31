"""
Vihan Patel, Suada Demirovic, Luke Kurlandski
March 2021

Answers the experimental question: how many training examples will Find-S require to learn 
the target concept: <Sunny, Warm, ?, ?, ?, ?>

Runs the experiment and produces a csv file which later can be used to conduct statistical 
analysis.

Structural Description:
    find_s_iteration() runs an iteration of the Find-S algorithm and returns the new hypothesis.
    training_example_generator() generates random instances and classifies them according to 
    the target concept. examples_required_to_learn() calculates the total number of examples
    needed to learn the target concept and experimental_question() writes this number to a 
    .csv file.

Run this program from the command line like

    > python3 experiment.py number_of_trials

    where number_of_trials is an integer that default to 100 if nothing is specified
    If number_of_trials < 100, then no experiment will be conducted.

"""

import csv
from os import path
import random
import sys

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
    
    skyVals = ['Sunny', 'Cloudy', 'Rainy']
    airTempVals = ['Warm', 'Cold']
    humidityVals = ['Normal', 'High']
    windVals = ['Strong', 'Weak']
    waterVals = ['Warm', 'Cool']
    forecastVals = ['Same', 'Change']
    categories = [skyVals, airTempVals, humidityVals, windVals, waterVals, forecastVals]
    
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
    
    if((trainingEx[0] == 'Sunny') and (trainingEx[1] == 'Warm')): 
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
    hyp = ['NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL']
    
    while(hyp != target_concept):
        a = training_example_generator()
        num_examples += 1
        hyp = find_s_iteration(hyp, a)
    #
    
    return num_examples

def experimental_question(n=100):
    """
    Write the number of examples required to learn the target concept
        for n trials to a csv file.

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
    """
    Acquire the number of trials from the user, or use 100 as default, and then run.
    If the number of trials that the user wants to run is < 100, then no experiment will be conducted.
    """

    n_trials = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    
    if(n_trials < 100):
        print('The experiment needs at least 100 trials')
        return
    #
    
    experimental_question(n_trials)
    
if __name__ == "__main__":
    main()
