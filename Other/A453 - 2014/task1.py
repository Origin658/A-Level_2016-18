#Joseph Young
import random # imports random
opts = ("+", "*", "-")# for random math methods
score = 0#sets score counter to 0
i = 10#puts the counter on ten
question = 0 



print ("-------------------------Primary School quiz------------------------------------\n--------------------------------------------------------------------------------\n\n")
print ("Instrucations.\n You will be asked ten questions testing your arithmetic skills\n")#prints instructions
username = str(input("Please Enter Your full name to begin\n-"))# askes the user for there name
date = str(input("Please enter the date in this formate - DD-MM-YY\n-"))#askes the user to import the date
print ("Hello", username, "you are in class you now will be asked ten questions")

while i != 0:#while loop will end once run ten times for ten questons 
    i = i - 1 # takes away one from counter so it only loops ten times
    number1 = random.randint(1,10)#generates the random number for the question
    number2 = random.randint(1,10)
    sign = random.choice (opts)# generates the random math option + - *
    try: #stops error if user enters something other than a number.
        question = int(input("What is {0}{1}{2} =".format(number1,sign,number2))) #askes the user the question
    except ValueError: 
        print()
        
    if sign == "+": #tests which method was randomly generated.
        answer = (number1 + number2) # if method is plus it adds the numbers
    elif sign == "*":
        answer = (number1 * number2)
    else:
        answer = (number1 - number2)
        
    if question == answer: #checks if the user entered the correct answer.
        print ("Your answer was correct\n")
        score = score + 1 # if user gets anser correct it adds one to the score counter
    else:
        print("Your answer was Wrong the correct answer was",answer, "\n")#tells the user that they got the anser wrong and it gives them the correct answer
print (username, "you Got",score, "out of 10")# tells the user what they got out of ten
