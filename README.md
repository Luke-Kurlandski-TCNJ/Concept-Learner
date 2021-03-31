# Concept-Learner
Project 2 Concept Learner for CSC426-01: Machine Learning.

# Authors: Vihan Patel, Luke Kurlandski, Suada Demirovic
# File Name: README.md
# Description: Describes the contents of the submission.

## Contents:
The deliverables include:
1. **find_s.py**: The implementation of the Find-S algorithm and verification that produces the trace found in class. (Tasks 1 and 2)
	i. **training_examples.csv**: A formatted .csv file with a header describing the attributes and the target concept, and each following row describing a training example.
2. **experiment.py**: Determines the number of random training examples required to exactly learn the target concept. (Task 3)
	i. **experimental_question.csv**: The file where the calculated number of examples required to learn the target concept for each experiment was written to, from experiment.py. 
3. **produce_plots.py**: Produces a frequency histogram of the number of examples required. (Experimental Question)
	i. **experimental_details.csv**: The file where the calculated statistics (the number of times the experiment was run n, min, max, mode, median, mean, and standard deviation) were written to, from produce_plots.py. 
	ii. **experimental_question.png**: The histogram produced from produce_plots.py of the number of training examples needed to learn the target concept.
4. **experimental_question.pdf**: A pdf containing the histogram and statistics. (Experimental Question)
5. **Reflection**: A writeup reflecting on the assignment. 


## Build and Command-Line Execution Instructions for the HPC:

On OnDemand, go to your File Home Directory and upload the files in Concept-Learner. 

Before running any of the code, ensure that the correct version of Python 
is installed. Take the following steps.
1. Type 'module add python' in the command line.
2. Type 'python --version' in the command line.
You will get to know if Python 3.6.0 is installed.

Task 1, Task 2: 
	In the command line, type 'python find_s.py'.

	This will automatically use the training data contained in the file
	training_examples.csv. If desired, you can run the find-s algorithm
	and print the trace on any similarly formatted csv file by 
	supplying the name of the csv file as a command line argument. Suppose
	you have a csv file called x.csv. Then you can type 'python find_s.py x.csv'.

Task 3, Experimental Question:
	
	In the command line type 'python experiment.py'.

	This will automatically perform an experiment with 1000 trials, but 
	the number of trials can be controlled by specifying an integer as a
	command line argument. This will output a csv file containing the 
	data collected from the experiment. To produce the histogram and 
	stats, in the command line type 'python produce_plots.py'.

	The histogram relies on pandas, so make sure that is installed. Take the
	following steps below.
	1. Type 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py' in the command line.
	2. Type 'python get-pip.py' in the command line.
	3. Type 'pip install pandas' in the command line.
