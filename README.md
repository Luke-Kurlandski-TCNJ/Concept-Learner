# Concept-Learner
Project 2 Concept Learner for CSC426-01: Machine Learning.

# Authors: Vihan Patel, Luke Kurlandski, Suada Demirovic
# File Name: README.md
# Description: Describes the contents of the submission.

## Contents:
The deliverables include:

File needed for D1 & D2:
1. **training_examples.csv**: A formatted .csv file with a header describing the attributes and the target concept, and each following row describing a training example.

D1 & D2:
1. **find_s.py**: contains implementation of Find-S algorithm and prints the trace needed for Task 2
2. **experiment.py**: contains implementation of Task 3 and counts the # of training examples needed to learn a target concept for each trial in an experiment
3. **get_plot_and_stats.py**: produces statistics and frequency histogram for the experimental question

File needed for D3:
1. **experiment_results.csv**: this file serves as an output of experiment.py

D3: 
1. **statistics.csv**: The file where the calculated statistics (the number of times the experiment was run, min, max, mode, median, mean, and standard deviation) were written to, from get_plot_and_stats.py. 
2. **histogram.png**: The histogram produced from get_plot_and_stats.py
3. **experimental_question.pdf**: contains histogram from histogram.png and statistics from statistics.csv

D4:
1. **Reflection**: A writeup for D4.

## Build and Command-Line Execution Instructions for the HPC:

1) On OnDemand, go to your File Home Directory.
2) Upload Concept-Learner.tar.gz to your File Home Directory.
4) Type 'module add python' in the command line. Press the return key.
5) Type 'python --version' in the command line. Press the return key. You will get to know that Python 3.6.0 is installed.
6) Type 'tar -xzf ?' in the command line. The symbol, ?, represents the absolute path for Concept-Learner.tar.gz. Press the return key.
7) Figure out the absolute path for a folder called Concept-Learner.
8) Type 'cd ?' in the command line. The symbol, ?, represents the absolute path for a folder called Concept-Learner. Press the return key.

Task 1, Task 2: 
	
	In the command line, type 'python3 find_s.py'. Press the return key.

	This will automatically use the training data contained in the file
	training_examples.csv. If desired, you can run the find-s algorithm
	and print the trace on any similarly formatted csv file by 
	supplying the name of the csv file as a command line argument. Suppose
	you have a csv file called x.csv. Then you can type 'python3 find_s.py x.csv'
	and press the return key afterwards. Suppose you have a csv file with a
	name containing spaces in it (i.e. a - Sheet1.csv). Then you would type
	'python3 find_s.py "a - Sheet1.csv"'.

Task 3, Experimental Question:
	
	In the command line, type 'python3 experiment.py'. Press the return key.

	This will automatically perform an experiment with 100 trials, but 
	the number of trials can be controlled by specifying an integer as a
	command line argument. If the number specified is less than 100, 
	no experiment will be run. Say that you wanted to run 101 trials in an experiment.
	Then you would type 'python3 experiment.py 101'. If an experiment is performed, 
	a csv file containing experimental data will be outputted.
	
	To produce the histogram and stats, in the command line type 'python3 get_plot_and_stats.py'. Press the return key.

	The histogram relies on pandas, so make sure that is installed. Take the following steps below.
	1. Type 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py' in the command line. Press the return key.
	2. Type 'python get-pip.py' in the command line. Press the return key.
	3. Type 'pip install pandas' in the command line. Press the return key.
