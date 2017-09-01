from appJar import gui
import GOATquestions


"""
    Generalized Occupational Aptitude Test (G.O.A.T)
    ===============================================
    
    The G.O.A.T is a career-deciding quiz from the video game Fallout 3.
    This is a recreation of the quiz.
    
    1 A - science B - speech C - melee D - sneak
    2 A - melee B - speech C - medicine D - science 
    3 A - speech B - unarmed C - sneak D - barter 
    4 A - explosives B - bigGuns C - melee D - unarmed
    5 A - smallGuns B - barter C - bigGuns D - explosives
    6 A - lockpick B - explosives, barter C - energyWeps D - repair
    7 A  - smallGuns B - medicine C - barter D - energyweps
    8 A - barter B - smallGuns C - sneak D - medicine 
    9 A - repair B - explosives C - medicine D - lockpick
    
    Barter 5: 
    "They say the G.O.A.T never lies.\nAccording to this, you're slated to be the next vault ...\n\nChaplain.\nGod help us all.\n" 
    
    Big Guns 2 : 
    "Well according to this, you're in line to be trained as a laundry cannon operator.\nFirst time for everything indeed.\n"
    
    Energy Weps 2:
    "It's nice to know I can still be surprised.\n\n Pedicurist!\nI might have guessed Manicurist, or even Masseuse.\nBut apparently you're a foot person.\n"  
      
     Explosives 4:  
     "It says here you're perfectly suited for a career as a Waste Management Specialist.\n\nA specialist, mind you, not just a dabbler.\n Congratulations!\n"  
    
    Lockpick 2:
      "Huh.\n\nVault Loyalty Inspector...\nI thought that had been phased out decades ago.\nWell, sounds like a job right up your alley, hmm?\n"  
    
    Medicine 5:
     "Interesting.\n Clinical Test Subject...\n\n sounds like something you should excel at.\nI guess you and your dad will be working together.\n" 
     
    Melee 3:
        "Looks like the diner's going to get a new Fry Cook.\nI'll just say this once: hold the mustard, extra pickles.\nHa ha ha!\n"  
        
    Repair 2:
    "Thank goodness.\nWe're finally getting a new Jukebox Technician.\nThat thing hasn't worked right since old Joe Palmer passed!\n"  
    
    Science 2:
    "Well, well.\n\nPip-Boy Programmer, eh?\nStanley will finally have someone to talk shop with.\n"  
    
   small guns 3:
    "Huh...\nI wonder who will be brave enough to be your first customer as the vault's new Tattoo Artist?\nI promise it won't be me.\n"  
    
    sneak 3: 
     "Apparently you're management material.\n\nYou're going to be trained as a Shift Supervisor.\nCould I be talking to the next Overseer?\nStranger things have happened.\n"  
     
     speech 3: 
     "Wow.\n Wow.\n\nSays here you're going to be the vault's Marriage Counselor.\nAlmost makes me want to get married, just to be able to avail myself of your services.\n"  
     
     unarmed 2:
      "I always thought you'd have a career in professional sports.\nYou're the new vault Little League coach!\nCongratulations.\n"           
    
"""



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
resultWin = gui("Generalized Occupational Aptitude Test")

startWin.setGeometry("fullscreen")

qCount = 0 # Used to display different question labels

# SET WINDOWS END -------------------------------------------------

# FUNCTIONS START  -----------------------------------------------

# Set window defaults
def setup(q):
    q.setBg("green")
    q.addLabel("qNum", "Question " + str(qCount))
    q.addLabel("Question", "")
    q.setGeometry("fullscreen")
    
# Change questions accordingly
def winCycle(count, q):

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
              
               
# Functions to control buttons
        
        
def startPress(btn):
    
    if btn == "Begin": # Opens the questions window when start page button is pressed
         
        global qCount
        qCount += 1
        
        # Initialize window
        setup(question1)
  
        winCycle(qCount, question1)            

        question1.addButton("Continue", startPress)
        question1.go()
        
    if btn == "Quit":
        startWin.stop()
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
        
    if btn == "Continue":
        qCount += 1
        for x in range(0, 12):
            if qCount == 2:
                question1.stop()
                setup(question2)     
                winCycle(qCount, question2) 
                question2.addButton("Continue", startPress)
                question2.go()
            if qCount == 3:
                question2.stop()
                setup(question3)     
                winCycle(qCount, question3) 
                question3.addButton("Continue", startPress)
                question3.go()
            if qCount == 4:
                question3.stop()
                setup(question4)     
                winCycle(qCount, question4) 
                question4.addButton("Continue", startPress)
                question4.go()
            if qCount == 5:
                question4.stop()
                setup(question5)     
                winCycle(qCount, question5) 
                question5.addButton("Continue", startPress)
                question5.go()
            if qCount == 6:
                question5.stop()
                setup(question6)     
                winCycle(qCount, question6) 
                question6.addButton("Continue", startPress)
                question6.go()
            if qCount == 7:
                question6.stop()
                setup(question7)     
                winCycle(qCount, question7) 
                question7.addButton("Continue", startPress)
                question7.go()
            if qCount == 8:
                question7.stop()
                setup(question8)     
                winCycle(qCount, question8) 
                question8.addButton("Continue", startPress)
                question8.go()
            if qCount == 9:
                question8.stop()
                setup(question9)     
                winCycle(qCount, question9) 
                question9.addButton("Continue", startPress)
                question9.go()
            if qCount == 10:
                question9.stop()
                setup(question10)     
                winCycle(qCount, question10) 
                question10.addButton("Continue", startPress)
                question10.go() 
            if qCount > 10:
                question10.stop()  
                startWin.stop()  
                resultWin.go()


def endpress(btn):       
    if btn == "Quit":
        resultWin.stop()
    
# FUNCTIONS END ----------------------------------------------------

# Initialise results window
                
resultWin.setBg("green")
resultWin.addLabel("cong", "Congratulations!") 
resultWin.setLabelBg("cong", "green")
resultWin.addButtons(["Quit"], endpress)
         
# Initialize start window

startWin.setBg("green")
startWin.addLabel("welcome", "Welcome to the G.O.A.T")
startWin.setLabelBg("welcome", "green")
startWin.addButtons(["Begin", "Quit"], startPress)
startWin.go() 

    
    
