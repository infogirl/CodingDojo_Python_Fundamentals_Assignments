#This is a file of select functions I wrote for Coding Dojo's Python Fundamentals Chapter and Assignments

#Assignment 1: Filter by Type
#Write a program that, given some value, tests that value for its type. Here's what you should do for each type:
#Integer
#If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"
def intergerTest(x):
    if isinstance(x, int):
        if x >= 100:
            print "That's a big number!"
        else:
            print "That's a small number"

#String
#If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."
def stringTest(x):
    if isinstance(x, str):
        if len(x) >= 50:
            print "Long Sentence"
        else:
            print "Short Sentence"

#List
#If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."
def listTest(x):
    if isinstance(x, list):
        if len(x) >= 10:
            print "Big list"
        else:
            print "Short list"

#Assignment 2: Type List
#Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
#Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum.
# At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

def typeTest(list1):
    i = 0
    sumValues = 0
    concateStrings = ""
    listCounter = 0
    stringCounter = 0
    integerCounter = 0
    while i < len(list1):
        if isinstance(list1[i], int):
            sumValues = sumValues + list1[i]
            integerCounter += 1
        elif isinstance (list1[i], str):
            concateStrings = concateStrings + list1[i]
            stringCounter += 1
        elif isinstance (list1[i], list):
            listCounter += 1
        i += 1
    print "Sum: " + str(sumValues)
    print "string: " + concateStrings
    if (stringCounter == 0) and (listCounter == 0):
        print "The list you entered is of integer type"
    elif (listCounter == 0) and (integerCounter  == 0):
        print "The list you entered is of string type"
    elif(integerCounter == 0) and (stringCounter == 0):
        print "The list you entered is of list type"
    else:
        print "The list you entered is of mixed type"

#Assignment 3:  Find Characters
#Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

def compare_list(word_list, char):
    outPutList = []
    i = 0
    while i < len(word_list):
        z = 0
        while z < len(word_list[i]):
            #print word_list[i][z]
            if word_list[i][z] == char:
                outPutList.append(word_list[i])
            z += 1
        i += 1
    print outPutList

#Assignment 4: Checkerboard
#Write a program that prints a 'checkerboard' pattern to the console.  Your program should require no input

def checkerboard():
    for x in range (0, 8):
        if x%2 == 0:
            print "* * *"
        else:
            print " * * *"

#Assignment 5: Fun with Functions
#Odd/Even: Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
def odd_even():
    for x in range (1, 2001):
        if x%2 == 0:
            print "Number is " + str(x) + ". This is an even number."
        else:
            print "Number is " + str(x) + ". This is an odd number."

#Multiply:Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
def multiply(a):
    b = []
    x = 0
    while x < len(a):
        b.append(a[x] * 5)
        x += 1
    return b

#Assignment 6: Scores and Grades
#Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score.
#Hint: Use the python random module to generate a random number
def grade():
    x = 0
    for x in range (0, 10):
        import random
        random_num = random.random()
        score = round(random_num * 100)
        scoreInt = int(score)
        if scoreInt < 70:
            print "Score: " + str(scoreInt) + "; Your grade is D"
        elif scoreInt < 80:
            print "Score: " + str(scoreInt) + "; Your grade is C"
        elif scoreInt < 90:
            print "Score: " + str(scoreInt) + "; Your grade is B"
        else:
            print "Score: " + str(scoreInt) + "; Your grade is A"

#Assignment 7: Coin Tosses
#Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears
def cointoss():
    x = 0
    headCounter = 0
    tailCounter = 0
    for x in range (0, 5001):
        import random
        random_num = random.random()
        rounded_num = round(random_num)
        if rounded_num == 1:
            headCounter += 1
            print "Attempt #" + str(x) + ": Throwing a coin... It's a head! ... Got " + str(headCounter) + " head(s) so far and " + str(tailCounter) + " tail(s) so far"
        elif rounded_num == 0:
            tailCounter += 1
            print "Attempt #" + str(x) + ": Throwing a coin... It's tails! ... Got " + str(headCounter) + " head(s) so far and " + str(tailCounter) + " tail(s) so far"

#Assignment 8: Stars
#Part I: Create a function called draw_stars() that takes a list of numbers and prints out *.
def draw_stars(myList):
    x = 0
    for x in range (0, len(myList)):
        print myList[x] * "* "

#Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function.
#When a string is passed, instead of displaying *, display the first letter of the string according to the example below.
#You may use the .lower() string method for this part.

def draw_stars(myList):
    x = 0
    for x in range (0, len(myList)):
        if isinstance(myList[x], int):
            print myList[x] * "* "
        else:
            firstLet = myList[x][0]
            firstLet = firstLet.lower()
            print firstLet * len( myList[x])

#Assignment 9: Dictionary in, tuples out
#Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value.
def convertTuple(my_dict):
    tupleList = []
    for data, key in my_dict.iteritems():
        #print data, key
        tupElement = (key, data)
        #print x
        tupleList.append(tupElement)
    return tupleList

#Assignment 10: Making Dictionaries
#Create a function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values. Assume the lists will be of equal length.
def make_dict(list1, list2):
  new_dict = {}
  combine = zip(list1, list2)
  new_dict = dict(combine)
  return new_dict
