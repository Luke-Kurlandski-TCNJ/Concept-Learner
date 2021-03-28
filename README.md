# Concept-Learner
Project 2 Concept Learner for CSC426-01: Machine Learning.

## Build Instructions for the HPC:

On OnDemand, go to your File Home Directory and upload the files in Concept-Learner. 

Before running any of the code, ensure that the correct version of Python 
is installed by typing in the command line:
	> module add python
	> python --version 
This should return that Python 3.6.0 is installed

Task 1, Task 2: 
	In the command line, type
		> python find_s.py

	This will automatically use the training data contained in the file
	training_examples.csv. If desired, you can run the find-s algorithm
	and print the trace on any similarly formatted csv file by 
	supplying the name of the csv file as a command line argument.

Task 3, Experimental Question
	We have already provided the required historgram and data analysis, 
	so there is no need for the professor to do any of this. However, in
	the spirit of good documentation, we document this aspect of the 
	program as well. 
	
	To run this aspect of the program, in the command line type:
		> python experiment.py

	This will automatically perform an experiment with 1000 trials, but 
	the number of trials can be controlled by specifying an integer as a
	command line argument. This will output a csv file containing the 
	data collected from the experiment. To produce the histogram and 
	stats, in the command line type:
		> python produce_plots.py

	The histogram relies on pandas, so make sure that is installed by typing:
		> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
		> python get-pip.py
		> pip install pandas

	


