from tkinter import *
#tkinter is the module used for creating windows programs using python

#Creating a class that represent our window
#Frame is a predefined class in tkinter
#Frame refers to the borders and the title bar of the whole window

class Window(Frame) :
    def __init__(self, master = None) :
        Frame.__init__(self, master)
        self.master = master

#Creating the root frame/window
#root is a frame of the type Tk() which defines the frames/windows
root = Tk()

#app is the variable that refers to the first frame/window of our GUI
#the root is a frame that is passed to our window class
app = Window(root)

#Call the mainloop of Tk.
root.mainloop()

'''One thing, the program works just fine even with \
the app and mainloop lines being commeted. Wonder what\
exactly is there use.'''
