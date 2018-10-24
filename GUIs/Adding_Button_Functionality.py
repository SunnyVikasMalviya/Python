from tkinter import *

class Window(Frame) :
    def __init__(self, master = None) :
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self) :
        self.master.title("Some Random Interesting Title")
        self.pack(fill = BOTH, expand = 1)

        #The command parameter inside the Button function takes what \
        #a button should do in the event of a click
        btn_1 = Button(self, text = "The Button", command = self.btn_1_action)
        btn_1.place(x = 80, y = 25)

        btn_2 = Button(self, text = "Exit", command = self.btn_2_action)
        btn_2.place(x = 280, y = 25)

    #Function that defines the action of the first button
    def btn_1_action(self) :
        pass

    #Function that defines the action of the second button
    def btn_2_action(self) :
        exit()

    

root = Tk()
root.geometry("400x500")
app = Window(root)
root.mainloop()

