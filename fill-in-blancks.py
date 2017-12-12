#!/usr/bin/python
# -*- coding: utf-8 -*-
difficulty_level = 0
stop = False
score = 0
max_score = 4
level_one = ['City of Eiffel Tower is: ', 'City of Leaning Tower is: ',
             'City of Great Pyramids is: ', 'City of Acropolis is: ']
level_one_answers = ['paris', 'pisa', 'giza', 'athens']

level_two = ['Santorini is islands in: ', 'Bora Bora is islands in: ',
             'Bali is islands in: ', 'Koh Tao is islands in: ']
level_two_answers = ['greece', 'france', 'indonesian', 'thailand']

level_three = ['Everest is Mount in: ', 'Fuji is Mount in: ',
               'Kilimanjaro is Mount in: ', 'Olympus is Mount in: ']
level_three_answers = ['nepali', 'japan', 'tanzania', 'greece']


def getListOfQuestion():
    ''' return list of Questions '''

    if difficulty_level == 1:
        return level_one
    if difficulty_level == 2:
        return level_two
    if difficulty_level == 3:
        return level_three


def getListOfAnswers():
    ''' return list of Answers '''

    if difficulty_level == 1:
        return level_one_answers
    if difficulty_level == 2:
        return level_two_answers
    if difficulty_level == 3:
        return level_three_answers

def printBlanck(question_number):
    ''' print the full Answer '''
    print "Correct..!, "getListOfQuestion()[question_number] + getListOfAnswers()[question_number]


def check(question_number, answer):
    ''' get number of Question and answer as string and check of true or false and return it  '''

    if getListOfAnswers()[question_number] == answer.lower():
        printBlanck(question_number)
        return True
    else:
        return False


def getAnswer(question_number):
    ''' get number of Question and show it to the user and get an answer and send it to check method then return the boolean result '''

    answer = raw_input(getListOfQuestion()[question_number] + "\n")
    return check(question_number, answer)


def againChoice():
    ''' check if user pass or not and give him the option to try again them reset the score and level of difficulty '''

    global score
    global difficulty_level
    if score == max_score:
        print 'Congratulation..!'
    again = raw_input('play again? y for yes : ')
    if again.lower() != 'y':
        stop = True
    score = 0
    difficulty_level = 0

def chooseDifficulty():
    ''' choose level of difficulty '''

    global difficulty_level
    while difficulty_level == 0:
        choice = raw_input('choose difficulty: hard, medium, easy: ')
        if choice.lower() == 'hard':
            difficulty_level = 3
        elif choice.lower() == 'medium':

            difficulty_level = 2
        elif choice.lower() == 'easy':

            difficulty_level = 1


def sartQuiz():
    ''' start quiz loop '''
    for index in range(max_score):
        if getAnswer(index) == False:
		print "Try Again.."
		if getAnswer(index) == False:
            		againChoice()
            		break
        score = index + 1

    if score == max_score:
        againChoice()


while stop == False:
    chooseDifficulty()
    sartQuiz()
			
