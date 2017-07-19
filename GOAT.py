from appJar import gui
import GOATquestions


"""
    Generalized Occupational Aptitude Test (G.O.A.T)
    ===============================================
    
    The G.O.A.T is a career-deciding quiz from the video game Fallout 3.
    This is a recreation of the quiz.
    
"""

# SKILL VARIABLES ------------------------------
    
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

startWin = gui("Generalized Occupational Aptitude Test") # Initial window
question = gui("Generalized Occupational Aptitude Test") # Question winow
qCount = 0 # Used to display different question labels

# FUNCTIONS START  -----------------------------------------------

# Function to check user answers 
def function(a):
    print(question.getRadioButton("ans"))
""" Note to self : set Changeradiobutton function to check which answer and add to variables accordingly"""

# Function to control buttons
def startPress(btn):
    
    if btn == "Begin": # Opens the questions window when start page button is pressed
         
        global qCount
        qCount += 1
        
        # Initialize window
        
        question.setBg("green")
        question.addLabel("Title", "Question " + str(qCount))
        question.addLabel("Question", "")
        
# CHANGE QUESTIONS ---------------------------------------------

        # Question One                 
                   
        if qCount == 1:
            question.setLabel("Question", GOATquestions.qOne)
                
            question.addRadioButton("ans", GOATquestions.qOneA)
            question.addRadioButton("ans", GOATquestions.qOneB)
            question.addRadioButton("ans", GOATquestions.qOneC)
            question.addRadioButton("ans", GOATquestions.qOneD)
 
            question.setRadioButtonChangeFunction("ans", function)
            
# CHANGE QUESTIONS END ---------------------------------------------
 
        question.addButton("Continue", startPress)
        question.go()
   
    if btn == "Quit":
        question.stop()
        startWin.stop()
        
    if btn == "Continue":
        question.stop()   
        
# FUNCTIONS END ----------------------------------------------------
         
# Initialize start window

startWin.setBg("green")
startWin.addLabel("welcome", "Welcome to the G.O.A.T")
startWin.setLabelBg("welcome", "green")
startWin.addButtons(["Begin", "Quit"], startPress)
startWin.go() 
 
    
    
    
