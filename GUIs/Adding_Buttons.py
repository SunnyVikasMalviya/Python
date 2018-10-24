from tkinter import *

class Window(Frame) :
    def __init__(self, master = None) :
        Frame.__init__(self, master)
        self.master = master
        self.init_window()  #Creating the actual window in the frame by calling the function

    #Function that creates the window inside the frame
    def init_window(self) :
        #Window.title() assigns the title of the window written on the frames top panel
        self.master.title("Some Random Interesting Title")

        #Window.pack() refers to how much space of the frame the window should acquire
        self.pack(fill = BOTH, expand = 1)

        #Creating a button and giving it a title, Button() is an inbuilt function
        some_Button = Button(self, text = "Some Text On The Button")

        #Setting the position of the button on the screen, x and y are in pixels
        some_Button.place(x = 80, y = 25)

        #Creating one more button
        btn = Button(self, text = "Other Button")
        btn.place(x = 0, y = 0)
        #Breadth (or height) of the button is about 25 pixels
        

root = Tk()

#Assigning the size of the window at the time of the initialization
#The window is resizable though
root.geometry("400x500")
app = Window(root)

root.mainloop()

