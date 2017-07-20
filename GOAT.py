from appJar import gui
import GOATquestions


"""
    Generalized Occupational Aptitude Test (G.O.A.T)
    ===============================================
    
    The G.O.A.T is a career-deciding quiz from the video game Fallout 3.
    This is a recreation of the quiz.
    
"""

# SKILL VARIABLES START ------------------------------
    
# Combat
unarmed = 0
melee = 0 
explosives = 0 
smallGuns = 0 
bigGuns = 0 
energyGuns = 0

# Other
sneak = 0 
lockpick = 0
medicine = 0
science = 0
repair = 0
speech = 0 
barter = 0

# SKILL VARIABLES END -----------------------------

# SET WINDOWS START  ----------------------------------------------------------

startWin = gui("Generalized Occupational Aptitude Test") 
question1 = gui("Generalized Occupational Aptitude Test")
question2 = gui("Generalized Occupational Aptitude Test")
question3 = gui("Generalized Occupational Aptitude Test")
question4 = gui("Generalized Occupational Aptitude Test")
question5 = gui("Generalized Occupational Aptitude Test")
question6 = gui("Generalized Occupational Aptitude Test")
question7 = gui("Generalized Occupational Aptitude Test")
question8 = gui("Generalized Occupational Aptitude Test")
question9 = gui("Generalized Occupational Aptitude Test")
question10 = gui("Generalized Occupational Aptitude Test")

startWin.setGeometry("fullscreen")
question1.setGeometry("fullscreen")
question2.setGeometry("fullscreen")
question3.setGeometry("fullscreen")
question4.setGeometry("fullscreen")
question5.setGeometry("fullscreen")
question6.setGeometry("fullscreen")
question7.setGeometry("fullscreen")
question8.setGeometry("fullscreen")
question9.setGeometry("fullscreen")
question10.setGeometry("fullscreen")



qCount = 0 # Used to display different question labels

# SET WINDOWS END -------------------------------------------------

# FUNCTIONS START  -----------------------------------------------


def setup(q):
    q.setBg("green")
    q.addLabel("qNum", "Question " + str(qCount))
    q.addLabel("Question", "")


def qRep(count, q):

        q.setLabel("qNum", "Question " + str(qCount))
        
        # Question One                                 
        if count == 1:
            q.setLabel("Question", GOATquestions.qOne)
                
            q.addRadioButton("ans", GOATquestions.qOneA)
            q.addRadioButton("ans", GOATquestions.qOneB)
            q.addRadioButton("ans", GOATquestions.qOneC)
            q.addRadioButton("ans", GOATquestions.qOneD)

        if count == 2:
            q.setLabel("Question", GOATquestions.qTwo)
            
            q.addRadioButton("ans", GOATquestions.qTwoA)
            q.addRadioButton("ans", GOATquestions.qTwoB)
            q.addRadioButton("ans", GOATquestions.qTwoC)
            q.addRadioButton("ans", GOATquestions.qTwoD)
 
          #  question.setRadioButtonChangeFunction("ans", function)   
        
        if count == 3:
            q.setLabel("Question", GOATquestions.qThree)  
            
            q.addRadioButton("ans", GOATquestions.qThreeA)
            q.addRadioButton("ans", GOATquestions.qThreeB)
            q.addRadioButton("ans", GOATquestions.qThreeC)
            q.addRadioButton("ans", GOATquestions.qThreeD)
                     
        if count == 4:
            q.setLabel("Question", GOATquestions.qFour)
            
            q.addRadioButton("ans", GOATquestions.qFourA)
            q.addRadioButton("ans", GOATquestions.qFourB)
            q.addRadioButton("ans", GOATquestions.qFourC)
            q.addRadioButton("ans", GOATquestions.qFourD)
            
        if count == 5:
            q.setLabel("Question", GOATquestions.qFive)
            
            q.addRadioButton("ans", GOATquestions.qFiveA)
            q.addRadioButton("ans", GOATquestions.qFiveB)
            q.addRadioButton("ans", GOATquestions.qFiveC)
            q.addRadioButton("ans", GOATquestions.qFiveD)
            
        if count == 6: 
            q.setLabel("Question", GOATquestions.qSix)
            
            q.addRadioButton("ans", GOATquestions.qSixA)
            q.addRadioButton("ans", GOATquestions.qSixB)
            q.addRadioButton("ans", GOATquestions.qSixC)
            q.addRadioButton("ans", GOATquestions.qSixD)
            
        if count == 7:
            q.setLabel("Question", GOATquestions.qSeven)
            
            q.addRadioButton("ans", GOATquestions.qSevenA)
            q.addRadioButton("ans", GOATquestions.qSevenB)
            q.addRadioButton("ans", GOATquestions.qSevenC)
            q.addRadioButton("ans", GOATquestions.qSevenD)
            
        if count == 8:
            q.setLabel("Question", GOATquestions.qEight)
            
            q.addRadioButton("ans", GOATquestions.qEightA)
            q.addRadioButton("ans", GOATquestions.qEightB)
            q.addRadioButton("ans", GOATquestions.qEightC)
            q.addRadioButton("ans", GOATquestions.qEightD)
            
        if count == 9:
            q.setLabel("Question", GOATquestions.qNine)
            
            q.addRadioButton("ans", GOATquestions.qNineA)
            q.addRadioButton("ans", GOATquestions.qNineB)
            q.addRadioButton("ans", GOATquestions.qNineC)
            q.addRadioButton("ans", GOATquestions.qNineD)
            
        if count == 10:
            q.setLabel("Question", GOATquestions.qTen)

            q.addRadioButton("ans", GOATquestions.qTenA)
            q.addRadioButton("ans", GOATquestions.qTenB)
            q.addRadioButton("ans", GOATquestions.qTenC)
            q.addRadioButton("ans", GOATquestions.qTenD)

# Function to check user answers 
def function(a):
    print(question1.getRadioButton("ans"))
""" Note to self : set Changeradiobutton function to check which answer and add to variables accordingly"""

# Function to control buttons
def startPress(btn):
    
    if btn == "Begin": # Opens the questions window when start page button is pressed
         
        global qCount
        qCount += 1
        
        
        # Initialize window
        setup(question1)
    
# CHANGE QUESTIONS ---------------------------------------------

        qRep(qCount, question1)            
                                 
# CHANGE QUESTIONS END ---------------------------------------------

        question1.addButton("Continue", startPress)
        question1.go()
        
    if btn == "Quit":
        question1.stop()
        question2.stop()
        question3.stop()
        question4.stop()
        question5.stop()
        question6.stop()
        question7.stop()
        question8.stop()
        question9.stop()
        question10.stop()
        startWin.stop()
        
    if btn == "Continue":
        qCount += 1
        if qCount == 2:
            question1.stop()
            setup(question2)     
            qRep(qCount, question2) 
            question2.addButton("Continue", startPress)
            question2.go()
        if qCount == 3:
            question2.stop()
            setup(question3)     
            qRep(qCount, question3) 
            question3.addButton("Continue", startPress)
            question3.go()
        if qCount == 4:
            question3.stop()
            setup(question4)     
            qRep(qCount, question4) 
            question4.addButton("Continue", startPress)
            question4.go()
        if qCount == 5:
            question4.stop()
            setup(question5)     
            qRep(qCount, question5) 
            question5.addButton("Continue", startPress)
            question5.go()
        if qCount == 6:
            question5.stop()
            setup(question6)     
            qRep(qCount, question6) 
            question6.addButton("Continue", startPress)
            question6.go()
        if qCount == 7:
            question6.stop()
            setup(question7)     
            qRep(qCount, question7) 
            question7.addButton("Continue", startPress)
            question7.go()
        if qCount == 8:
            question7.stop()
            setup(question8)     
            qRep(qCount, question8) 
            question8.addButton("Continue", startPress)
            question8.go()
        if qCount == 9:
            question8.stop()
            setup(question9)     
            qRep(qCount, question9) 
            question9.addButton("Continue", startPress)
            question9.go()
        if qCount == 10:
            question9.stop()
            setup(question10)     
            qRep(qCount, question10) 
            question10.addButton("Continue", startPress)
            question10.go() 
        if qCount > 10:
            question10.stop()
            qCount = 0                 
            
        
# FUNCTIONS END ----------------------------------------------------
         
# Initialize start window


startWin.setBg("green")
startWin.addLabel("welcome", "Welcome to the G.O.A.T")
startWin.setLabelBg("welcome", "green")
startWin.addButtons(["Begin", "Quit"], startPress)
startWin.go() 
 
    
    
    
