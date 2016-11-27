print ("Hello, World!")

from tkinter import *

main = Tk()

#def leftKey(event):
#	print ("Unicorn!")
#def rightKey(event):
#	print ("left, no the other left!")
#def upKey(event):
#	print ("Upp")
#def downKey(event):
#	print ("Feces!")

w = Canvas(main, width=500, height=500)
w.pack()
#w.create_line(0, 0, 200, 100)
oval = w.create_oval(10, 125, 150, 75)
fishie = w.create_oval(410, 450, 450, 470)
fishie_tail = w.create_line (415, 455, 400, 445)
fishie_tail2 = w.create_line (415, 465, 400, 475)
fishie_tail3 = w.create_line (400, 445, 400, 475)
fishie_mouth = w.create_line (450, 462, 443, 462)
fishie_eye = w.create_oval (442, 457, 445, 455)

def move_right(event):
        w.move(oval, 20, 0)
        pass

def move_left(event):
    w.move(oval, -20, 0)
    pass

def move_up(event):
        w.move(oval, 0, -20)
        pass

def move_down(event):
    w.move(oval, 0, 20)
    pass


#frame = Frame(main, width=100, height=100)
main.bind('<Left>', move_left)
main.bind('<Right>', move_right)
main.bind('<Up>', move_up)
main.bind('<Down>',move_down)
#frame.pack()





#canvas = Canvas()
#canvas.create_oval(15, 15)
        
#canvas.pack(fill=BOTH, expand=1)

main.mainloop()


#while True:

#	print "I am hungry!"

#end


