#Basic Math tester internal functions
#Author: Sriram Yadavalli
#File: Internals.py
#Date: 10/21/20

import random
import math
from datetime import datetime

#welcome prints
def printWelcome():
        print("\nWelcome to Basic Math Tester")
        print("This program tests your ability to perform " + "basic math operations")
        print("\nRandom integers will be picked between lower and upper bounds (inclusive) " 
              + "that you choose")
#collects user input for lower and upper bound and operator        
def userInput():
        while True:
            #looks for invalid inputs
            try:
                uiLower = int(input("Enter an integer for Lower/Upper Bound: "))
                uiUpper = int(input("Enter the other integer for Lower/Upper Bound: "))
            except ValueError:
                print("Invalid Input")
                continue
            else:
                break
        
        operator = ["+", "-", "*", "/"]
        
        uiOperator = input("Choose Operator (+, -, *, /): ")
        
        #looks for invalid inputs
        while(uiOperator not in operator):
            uiOperator = input("Choose Operator (+, -, *, /): ")
            if(uiOperator in operator):
                break
            
        if(uiLower < uiUpper or uiLower == uiUpper):
            return int(uiLower), int(uiUpper), str(uiOperator)
        else:
            return int(uiUpper), int(uiLower), str(uiOperator)

#truncates to two decimal places
def truncate(number, decimals = 0):
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor

#random number generator        
def randomNum(uiLower, uiUpper): 
    num1 = random.randrange(uiUpper, uiLower + 1)
    num2 = random.randrange(uiUpper, uiLower + 1)
    
    return num1, num2

#computer calculated answer
def answerCompute(num1, num2, operator):
    compAns = 0
    
    if(operator == "+"):
        compAns = num1 + num2
        return compAns
    
    if(operator == "-"):
        compAns = num1 - num2
        return compAns
    
    if(operator == "*"):
        compAns = num1 * num2
        return compAns
    
    if(operator == "/"):
        #divide by 0 handling
        if(num2 == 0):
            compAns = "undef"
            return compAns
        #truncating and whole number cases
        else:
            compAns = num1 / num2
            compAns = truncate(compAns, 2)
            if(num1 % num2 == 0):
                return str(compAns).replace(".0","")
            else:
                return compAns

#presents question to user
def question(num1, num2, operator):
    userAns = input("Solve (Note: For answers with decimal numbers truncate to max two digits): \n" 
                + str(num1) + " " + operator + " " + str(num2) + " = ")
    question = str(num1) + " " + operator + " " + str(num2) + " = " + "?\n"
    
    return userAns, question

#compares user provided answer with computer
def compare(userAns, compAns):
    userAns = str(userAns)
    compAns = str(compAns)
    
    if(userAns == compAns):
        return True
    else:
        return False

#print results to file    
def printToFile(listQuestion, listUserAns, listCompAns, correct, incorrect, total): 
    now = datetime.now()
    fileName = "results" + now.strftime("%m-%d-%Y" + "_" + "%H.%M.%S" + ".txt")
    
    with open(fileName, "w") as file:
        file.write("Basic Math Tester Results\n")
        file.write("Date and Time: " + str(now.strftime("%m-%d-%Y" + " " + "%H:%M:%S")) + "\n\n")
        for i in range(0, len(listQuestion)):
            file.write("Question " + "#" + str(i + 1) + "\n" + listQuestion[i])
            file.write("Your Answer: " + listUserAns[i] + "\n")
            file.write("Computer's Answer: " + listCompAns[i] + "\n")
            
            if(listUserAns[i] == listCompAns[i]):
                file.write("Your answer was correct\n\n")
            else:
                file.write("Your answer was incorrect\n\n")
                
        file.write("Total Correct: " + str(correct) + "\n")
        file.write("Total Incorrect: " + str(incorrect) + "\n")
        file.write("Total Score: " + str(correct) + "/" + str(total))
    
    return fileName