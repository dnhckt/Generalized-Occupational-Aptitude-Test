from appJar import gui

def press(btn):
    print(btn)

app = gui()

app.setBg("green")

app.addLabel("welcome", "Welcome to the G.O.A.T")
app.setLabelBg("welcome", "green")

app.addButton("Begin", press)
app.setButtonBg("Begin", "black")

app.go() 

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
    
    
    
    
    
    
