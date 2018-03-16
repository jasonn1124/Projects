# Files - Quiz Maker (WIP)

"""
PROGRAM OBJECTIVES
1) Program randomly takes questions from a file.
2) Presents as a quiz.
3) User answers the quiz.
4) Program returns a grade.
"""

"""
ADDITIONAL NOTES
This program requires a file named "QuizMakerData.txt" in an accompanying folder named "ProjectData".
The filename and foldername can be changed in line 32.
The format of the file contents is as follows:
	- Start with a questions
	- Next line is an answer for the previous questions
	- Repeat ad infinitum
	- Last line should be an empty line
"""
# Imports
import subprocess
import os
from random import randint

# Function - Clear screen
def cls():
	subprocess.call("cls", shell = True)
	
# File retrieval and adding everything to respective lists.
fileDir = os.path.dirname(os.path.realpath('__file__'))
fileName = os.path.join(fileDir, "ProjectData/QuizMakerData.txt")
with open(fileName) as fileHolder:
	isQuestion = True
	isAnswer = False
	questionsList = []
	answersList = []
	for line in fileHolder:
		# Removes the \n character
		line = line[0:len(line)-1]
		if isQuestion == True:
			questionsList.append(line)
			isQuestion = False
			isAnswer = True
		elif isAnswer == True:
			answersList.append(line)
			isQuestion = True
			isAnswer = False

# Adds 3 random questions to the quiz, along with corresponding answer keys
quizQnList = []
quizAnsList = []
counter = 3
while counter != 0:
	randNo = randint(0,len(questionsList)-1)
	# Debug - print "\nRandom integer is {0}.\nquestionsList is {1} elements long.".format(randNo, len(questionsList))
	quizQnList.append(questionsList.pop(randNo))
	quizAnsList.append(answersList.pop(randNo))
	counter -= 1
	
# Presents quiz to user and records responses.
cls()
print "Quiz maker - Quiz"
userAnsList = []
for i in range(0,len(quizQnList)):
	userInput = raw_input("\nQuestion {0}: {1}\nAnswer: ".format(i+1, quizQnList[i]))
	userAnsList.append(userInput.lower())

# Compares user answers vs answer list
cls()
print "Quiz maker - grader"
userScore = 0
for i in range(0,len(quizAnsList)):
	if userAnsList[i] != quizAnsList[i]:
		print "\nQuestion {0} was wrong.\nYour answer was '{1}'.\nCorrect answer was '{2}'.".format(i+1, userAnsList[i], quizAnsList[i])
	elif userAnsList[i] == quizAnsList[i]:
		print "\nQuestion {0} was correct.".format(i+1)
		userScore += 1

print "\nYou got {0} out of 3 questions correct.".format(userScore)

raw_input()
