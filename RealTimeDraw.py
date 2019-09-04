from pygameWindow import PYGAME_WINDOW
import random
x = 0 #where the black circle is located
y = 0 #where the black circle is located
instance = PYGAME_WINDOW()



while True:
    instance.Prepare()
    pass
    instance.Reveal()
    pass
    #instance.Draw_Black_Circle(x,y)
    instance.Draw_Black_Circle(0)
    pass
    def Perturb_Circle_Position():
        global x, y
        fourSidedDieRoll = random.randint(1,5)
        if fourSidedDieRoll == 1:
            x -= 1
        elif fourSidedDieRoll == 2:
            x += 1
        elif fourSidedDieRoll == 3:
            y -= 1
        else
            y += 1
        
