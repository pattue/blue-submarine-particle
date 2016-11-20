print "Hello, World!"

from Tkinter import *

main = Tk()

def leftKey(event):
	print "Unicorn!"
def rightKey(event):
	print "left, no the other left!"
def upKey(event):
	print "Upp"
def downKey(event):
	print "Feasises!"


frame = Frame(main,width=100, height=100)
main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
main.bind('<Up>', upKey)
main.bind('<Down>',downKey)
frame.pack()
main.mainloop()


#while True:

#	print "I am hungry!"

#end


