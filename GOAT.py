from appJar import gui
import GOATquestions

startWin = gui("Generalized Occupational Aptitude Test")
question = gui("Generalized Occupational Aptitude Test")

qCount = 0

def startPress(btn):
    
    if btn == "Begin":
         
        global qCount
        qCount += 1
    
        question.setBg("green")
     
        question.addLabel("Tit", "Question " + str(qCount))
        question.addLabel("Question", "")
            
        if qCount == 1:
            question.setLabel("Question", GOATquestions.qOne)
                
            question.addRadioButton("ans", GOATquestions.qOneA)
            question.addRadioButton("ans", GOATquestions.qOneB)
            question.addRadioButton("ans", GOATquestions.qOneC)
            question.addRadioButton("ans", GOATquestions.qOneD)
 
        question.addButton("Continue", startPress)
        
        question.go()
   
    if btn == "Quit":
        startWin.stop()
        print("Quit")
        
    if btn == "Continue":
        question.stop()    
        

startWin.setBg("green")
startWin.addLabel("welcome", "Welcome to the G.O.A.T")
startWin.setLabelBg("welcome", "green")
startWin.addButtons(["Begin", "Quit"], startPress)
startWin.go() 

"""
    Generalized Occupational Aptitude Test (G.O.A.T)
    ===============================================
    
    The G.O.A.T is a career-deciding quiz from the video game Fallout 3.
    This is a recreation of the quiz.
"""

# Skills
    
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
    
    
    
    
    
    
