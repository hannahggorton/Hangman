import random
import turtle
import math
import time

wordList = ["abate", "benevolent", "candid", "decree", "eloquent", "facilitate", "galvanizing", "hostile", "ignominious", "lament", "malicious", "obsolete",\
    "paramount", "qualitative", "ramify", "savvy", "tactful", "ubiquitous", "validate", "warrant", "yield"]

secretWord = random.choice(wordList)
wrongLetters = []
correctLetters = []
MAX_GUESSES = 15
screenword = ""
wrongGuesses = 0
print(f"The secret word is {secretWord}")

turtle.colormode(255)
screen = turtle.getscreen()
sWidth=1000
sHeight=700
diag = int(math.sqrt((sWidth*sWidth) + (sHeight * sHeight)))
screen.setup(sWidth, sHeight)
screen.bgcolor(90, 3, 252)
#sets up turtle
t = turtle.getturtle()
t.shape("turtle")
t.color(252, 194, 35)
t.width(5)
t.speed(0)
t.penup ()
t.hideturtle()

topFont = 48
topScreenTurtle = turtle.Turtle()
topScreenTurtle.shape("turtle")
topScreenTurtle.color(25,167,198)
topScreenTurtle.width(5)
topScreenTurtle.speed(0)
topScreenTurtle
topScreenTurtle.penup()
topScreenTurtle.goto (-1*int(sWidth/2) + int(sWidth*0.1),-1* int(sHeight*0.40))
topScreenTurtle.hideturtle()

bottomScreenTurtle = turtle.Turtle()
bottomScreenTurtle.shape("turtle")
bottomScreenTurtle.color(107, 248, 97)
bottomScreenTurtle.width(5)
bottomScreenTurtle.speed(0)
bottomScreenTurtle
bottomScreenTurtle.penup()
bottomScreenTurtle.goto (-1*int(sWidth/2) + int(sWidth*0.1), -1*int(sHeight/2)+ int(sHeight*0.35))
step = (sWidth/10)
bottomScreenTurtle.hideturtle()
gameOn = True

def drawGallows():
    global topHead
    t.forward(int(sWidth*0.125))
    t.right(90)
    t.forward(int(sHeight * 0.25))
    t.left(90)
    #bottom line
    t.pendown()
    t.forward(int(sWidth*0.3))
    #go backward
    t.backward(int(sWidth *0.15))
    #draw up
    t.left(90)
    t.forward(int(sHeight* 0.6))
    t.left(90)
    t.forward(int(sWidth*0.125))
    t.left(90)
    t.forward(int(sHeight*0.1))
    topHead = t.position()

def drawHead():
    global endGallows
    t.right(90)
    t.circle(int(sHeight*0.06))
    endGallows = t.position()

def drawBody():
    global lowerBodP
    t.left(90)
    t.penup()
    t.forward(int(sHeight * 0.06) * 2)
    t.pendown()
    t.forward(int(sHeight * 0.08) * 2)
    lowerBodP = t.position()

def rightArm():
    global lowerBodP, rightArmLoc
    t.penup()
    t.goto(lowerBodP)
    t.setheading(90)
    t.forward(int(sHeight * 0.03))
    t.right(30)
    # length of arm
    t.pendown()
    t.forward(int(diag * 0.06))
    rightArmLoc = t.position()

def leftArm():
    global lowerBodP , leftArmLoc
    t.penup()
    t.goto(lowerBodP)
    t.setheading(90)
    t.forward(int(sHeight*0.03))
    t.left(30)
    t.pendown()
    #length of arm
    t.forward(int(diag * 0.06))
    leftArmLoc = t.position()

def leftLeg():
    #get down to where to start leg
    global lowerBodP, leftLegLoc
    t.penup()
    t.goto(lowerBodP)
    t.setheading(-90)
    t.right(20)
    t.pendown()
    t.forward(int(diag * 0.08))
    leftLegLoc = t.position()

def rightLeg():
    global lowerBodP, rightLegLoc
    t.penup()
    t.goto(lowerBodP)
    t.setheading(-90)
    t.left(20)
    t.pendown()
    t.forward(int(diag * 0.08))
    rightLegLoc = t.position()

def rightHand():
    global rightArmLoc
    t.penup()
    t.goto (rightArmLoc)
    t.left(-90)
    t.pendown()
    t.circle(10)

def leftHand():
   global leftArmLoc
   t.penup()
   t.goto(leftArmLoc)
   t.left(90)
   t.pendown()
   t.circle(10)

def rightFoot():
    global rightLegLoc
    t.penup()
    t.goto(rightLegLoc)
    t.right(-180)
    t.pendown()
    t.circle(15)

def leftFoot():
    global leftLegLoc
    t.penup()
    t.goto(leftLegLoc)
    t.left(180)
    t.pendown()
    t.circle(15)

def eyes():
    global topHead
    t.penup()
    t.goto(topHead)
    t.setheading(-90)
    t.forward(int(sHeight*0.035))
    t.right(70)
    t.forward(int(sHeight*0.025))
    t.pendown()
    t.circle(8)
    t.penup()
    t.goto(topHead)
    t.setheading(-90)
    t.forward(int(sHeight * 0.05))
    t.left(70)
    t.forward(int(sHeight * 0.029))
    t.pendown()
    t.circle(8)

def mouth():
    global topHead
    t.penup()
    t.goto(topHead)
    t.setheading(-90)
    t.forward(int(sHeight*0.09))
    t.pendown()
    t.setheading(180)
    t.forward(int(diag*0.02))
    t.right(180)
    t.forward(int(diag*0.04))

def hat():
    global topHead
    t.penup()
    t.goto(topHead)
    t.setheading(90)
    t.pendown()
    t.right(90)
    t.forward(int(sWidth*0.07))
    t.right(180)
    t.forward(int(sWidth*0.14))
    t.right(180)
    t.forward(int(sWidth*0.035))
    t.left(90)
    t.forward(int(sHeight*0.07))
    t.right(90)
    t.forward(int(sWidth*0.07))
    t.right(90)
    t.forward(int(sHeight*0.07))

def skirt():
    global lowerBodP
    t.penup()
    t.goto(lowerBodP)
    t.setheading(90)
    t.right(90)
    t.pendown()
    t.forward(int(sWidth*0.07))
    t.right(180)
    t.forward(int(sWidth*0.014))
    t.right(360)
    t.forward(int(sWidth*0.14))
    t.left(70)
    t.forward(int(diag*0.04))
    t.left(110)
    t.forward(int(sWidth*0.21))
    t.left(125)
    t.forward(int(diag*0.045))

def updateDrawing():
    if wrongGuesses == 0:
        drawGallows()
    if wrongGuesses == 1:
        drawHead()
    if wrongGuesses == 2:
        drawBody()
    if wrongGuesses == 3:
       leftLeg()
    if wrongGuesses == 4:
        rightLeg()
    if wrongGuesses == 5:
        leftLeg()
    if wrongGuesses == 6:
        rightArm()
    if wrongGuesses == 7:
        leftArm()
    if wrongGuesses == 8:
        rightHand()
    if wrongGuesses == 9:
        leftHand()
    if wrongGuesses == 10:
        rightFoot()
    if wrongGuesses == 11:
        leftFoot()
    if wrongGuesses == 12:
        eyes()
    if wrongGuesses == 13:
        mouth()
    if wrongGuesses == 14:
        hat()
    if wrongGuesses == 15:
        skirt()

def drawWrongLetters():
    topScreenTurtle.clear()
    letterString = "Wrong Letters: "
    for l in wrongLetters:
        letterString += l + ", "
    letterString = letterString[ : len(letterString)-2]
    topScreenTurtle.write(letterString,move=False, align="left", font=("Arial", topFont, "normal"))

def drawWord():
    global screenword
    #step one is to save the turtle information
    #currentLoc = t.position()
    #currentHead = t.heading()
    bottomScreenTurtle.clear()
    bottomScreenTurtle.penup()
    bottomScreenTurtle.goto (-1*int(sWidth/2) + int(sWidth*0.1), -1*int(sHeight/2)+int(sHeight*0.25))
    bottomScreenTurtle.setheading(0)

    screenword = ""
    for letter in secretWord:
        if letter in correctLetters:
            screenword +=letter+" "
        else:
            screenword += "_" +" "
    bottomScreenTurtle.write(screenword, move=False, align="left", font=("Arial", 56, "normal"))
    if "_" not in screenword:
        writeErrorMessage("You won, way to go!!!")
        gameOn = False
    #t.goto(currentLoc)
    #t.setheading(currentHead)

def getGuess():
    badLetterString = ""
    for letter in wrongLetters:
        badLetterString += letter + ", "
    boxTitle = "Letters Used:" + badLetterString
    theGuess = screen.textinput(boxTitle, "Enter a letter or type ** to guess the word")
    return theGuess

def writeErrorMessage(msg):
    topScreenTurtle.clear()
    topScreenTurtle.write(msg, move=False, align="left", font=("Arial", topFont, "normal"))
    time.sleep(2)
    topScreenTurtle.clear()

def printWinorLose(win):

    topScreenTurtle.clear()
    if win:
        screenword = secretWord
        drawWord()

        topScreenTurtle.write("You Win!!!", move=False, align = "left",font=("Arial",topFont, "normal"))

    else:
        topScreenTurtle.write("You Did not Win :(:(:(", move=False, align="left", font=("Arial", topFont, "normal"))

def getWordGuess():
    playerWordGuess = screen.textinput("Guess the word","Enter your guess of the word")
    print(playerWordGuess)
    print(secretWord)
    if (playerWordGuess.lower() == secretWord.lower()):
        #celebrate the win!!
        printWinorLose(True)
        time.sleep(1)
        writeErrorMessage("The secret word is:" + secretWord)
        return False #false means that the game is./ over (when you guess the word you get it rigth or wrong but the game is over either way)
    else:
        #celebrate fail
        printWinorLose(False)
        return False
updateDrawing()
while gameOn:
    drawWord()
    guess = getGuess()
    if guess == "**":
        gameOn = getWordGuess()
    elif len(guess) != 1:
        writeErrorMessage("I need one letter. Try again.")
    elif guess.lower() not in "abcdefghijklmnopqrstuvwxyz":
        writeErrorMessage("Sorry, I need a letter not a character. \nGuess again")
        drawWrongLetters()
    elif guess.lower() in wrongLetters:
        writeErrorMessage("You already guessed " + guess.upper() + ". Guess again.")
    elif guess.lower() in correctLetters:
        writeErrorMessage(guess.upper() + " is in the word. Please guess again.")
    else:
        if guess.lower() in secretWord.lower():
            correctLetters.append(guess.lower())
            drawWord()
        else:
            wrongLetters.append(guess.lower())
            drawWrongLetters()
            wrongGuesses += 1
            updateDrawing()
        if(wrongGuesses>= MAX_GUESSES):
            writeErrorMessage("You are out of guesses. Game over")
            gameOn == False
            writeErrorMessage("The secret word is:" + secretWord)



turtle.mainloop()

