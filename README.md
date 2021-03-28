# Concept-Learner
Project 2 Concept Learner for CSC426-01: Machine Learning.

Instructions to use programs:

Task 1, Task 2: 
	In the command line, type
		> python3 find_s.py

	This will automatically use the training data contained in the file
	training_examples.csv. If desired, you can run the find-s algorithm
	and print the trace on any similarily formatted csv file by 
	supplying the name of the csv file as a command line argument.

Task 3, Experimental Question
	We have already provided the required historgram and data analysis, 
	so there is no need for the professor to do any of this. However, in
	the spirit of good documentation, we document this aspect of the 
	program as well. 
	
	To run this aspect of the program, in the command line type
		> python3 experiment.py

	This will automatically perform an experiment with 1000 trials, but 
	the number of trials can be controlled by specifying an integer as
	command line argument. This will output a csv file containing the 
	data collected from the experiment. To produce the histogram and 
	stats, in the command line type
		> python3 produce_plots.py

	The histogram relies on pandas, so make sure that is installed.

	


