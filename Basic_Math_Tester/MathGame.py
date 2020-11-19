#Basic Math Tester
#Author: Sriram Yadavalli
#File: MathGame.py
#Date: 10/21/20

import Internals as x
import sys

class MathGame:
    
    x.printWelcome()
    
    #lists to print to file
    listQuestion = []
    listUserAns = []
    listCompAns = []
    
    #ints to print to file
    correct = 0
    incorrect = 0
    total = 0

    #loops until user says no
    while True:
        #collecting return values from methods
        uiLower, uiUpper, uiOperator = x.userInput()
        num1, num2 = x.randomNum(uiUpper, uiLower)
        operator = uiOperator
        userAns, question = x.question(num1, num2, operator)
        
        #adding to lists
        listQuestion.append(question)
        listUserAns.append(str(userAns))
        
        compAns = x.answerCompute(num1, num2, operator)
        
        listCompAns.append(str(compAns))
        
        compared = x.compare(userAns, compAns)
        
        if(compared == True):
            print("\nCorrect!")
            #adding to correct and total
            correct = correct + 1
            total = total + 1
        else:
            print("\nIncorrect!")
            total = total + 1
        
        incorrect = total - correct
        
        playAgain = input("Do you want to play again (Y|N)? ")
        
        #check if user wants to play again
        if(playAgain == "y" or playAgain == "Y"):
            continue
        elif(playAgain == "n" or playAgain == "N"):
            fileName = x.printToFile(listQuestion, listUserAns, listCompAns, correct, incorrect, total)
            print("Your results are available in file " + fileName)
            sys.exit()