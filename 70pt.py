#########################################
#
#    70pt - Basic collision detection
#
#########################################

# When the player moves the ball into the rectangle, turn the rectangle red
# You will need to code the movement of the player and the collision detection.

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")



class MyApp:
	def __init__(self, parent):
       	    global drawpad
            global circle
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=1)

       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)

       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack()
	

	    # Remember to include your "enemies" with "global"
	    	
		
	def upClicked(self, event):   
	   global circle
	   global player

	   drawpad.move(player,0,-10)

           x1, y1, x2, y2 = drawpad.coords(player)
           if (targetx1 < x1 and targetx2 > x2) and (targety1 < y1 and targety2 > y2):
                drawpad.itemconfig(target, fill = "Red")
		
myapp = MyApp(root)

root.mainloop()


