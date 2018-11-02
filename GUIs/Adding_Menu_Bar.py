from tkinter import *

class Window(Frame) :
    def __init__(self, master = None) :
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self) :
        self.master.title("Some Random Interesting Title")
        self.pack(fill = BOTH, expand = 1)

        #Menu is a built in function in the tkinter library
        #It takes the frame as the argument in which we want to insert the menu.
        #Menu is attached to the frame and not the window.
        #new_menu is the name of the object of the type menu.
        new_menu = Menu(self.master)
        #We have created the menu but haven't attached it yet to the frame. \
        #The next statement does that.
        #config() is  a function in the frame class that is used to configure \
        #the frame object that we create.
        self.master.config(menu = new_menu)

        #Now we create the Command header in the menu we created. Command \
        #header is the name of the header given to a group of commands.
        #Example the File is the command header for the command for commands \
        #like New, Open, Save, Save As, etc.
        #We pass the newly created menu object to the Menu class and it gives \
        #Us a place for our command header in the menu. Here this place is \
        #named as file_.
        #Then we add commands to the command header file_.
        #The commands are added to the command header in sequential order.
        #add_command has an argument that takes the action of the command \
        #button. This is similar to that of the command argument in the \
        #Button() class.
        file_ = Menu(new_menu)
        file_.add_command(label = 'Leave', command=self.client_exit)
        file_.add_command(label = 'Quit', command=self.client_exit)
        file_.add_command(label = 'Exit', command=self.client_exit)

        #Now we have created a File command header with few commands but we \
        #haven't added them to the menu that we created. The next statement \
        #does that.
        #The label is the name of the command header. menu is the command \
        #header variable that you want to add the created menu object.
        new_menu.add_cascade(label = 'File', menu = file_)

        #self.com(file_)                #Don't bother yourself with this.

        #Similarly we create an Edit,a Help and an Extra command header with \
        #several commands in it.
        #Notice we didn't add any command argument to the add_command(). These\
        #commands will not do anything for now.
        edit_ = Menu(new_menu)
        edit_.add_command(label = 'Undo')
        edit_.add_command(label = 'Redo')
        edit_.add_command(label = 'Copy')
        edit_.add_command(label = 'Paste')
        new_menu.add_cascade(label = 'Edit', menu = edit_)

        
        help_ = Menu(new_menu)
        help_.add_command(label = '?')
        new_menu.add_cascade(label = 'Help', menu = help_)

        extra_ = Menu(new_menu)
        new_menu.add_cascade(label = 'Extra', menu =extra_)

    def client_exit(self) :
        exit()

    #def com(self, file_) :               #Don't bother yourself with this.
    #    print(type(file_))     

root = Tk()
root.geometry("400x500")
app = Window(root)
root.mainloop()


