from tkinter import *
from PIL import Image, ImageTk    #Notice the capital letters in PIL, Image and ImageTk

#PIL: python imaging library
#also known as pillow.

class Window(Frame) :
    def __init__(self, master = None) :
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self) :
        self.master.title("Some Random Interesting Title")
        self.pack(fill = BOTH, expand = 1)

        new_menu = Menu(self.master)
        self.master.config(menu = new_menu)

        file_ = Menu(new_menu)
        file_.add_command(label = 'Save (Doesn\'t work)')
        file_.add_command(label = 'Exit (Works)', command=self.client_exit)
        new_menu.add_cascade(label = 'File', menu = file_)

        edit_ = Menu(new_menu)
        edit_.add_command(label = 'Show Image (Works)', command=self.showImg)
        '''
        Above we have added function call to the command attribute without parenthesis.
        This works because, when we call function like this, the function doesn't get \
        executed into the main thread but a new thread is created for the function \
        and the main program execution is continued. Basically the function is just made\
        callable and is not actually called at that moment. It only gets executed when \
        a user triggers it.
        For example, if we add parenthesis to the function calls, as soon as we run the\
        program, the window already contains the image and text without even clicking on \
        the Show Image (Works) command in the Edit command header.
        Similarly, if we call exit with parenthesis, the program will exit even before \
        executing, meaning it takes the main thread and the main program is stopped.
        '''

        edit_.add_command(label = 'Show Text (Works)', command=self.showTxt)
        edit_.add_command(label = 'Redo (Doesn\'t work)')
        edit_.add_command(label = 'Copy (Doesn\'t work)')
        edit_.add_command(label = 'Paste (Doesn\'t work)')
        new_menu.add_cascade(label = 'Edit', menu = edit_)
        
        help_ = Menu(new_menu)
        help_.add_command(label = '?')
        new_menu.add_cascade(label = 'Help', menu = help_)

    def client_exit(self) :
        exit()

    def showImg(self) :
        #Opening a image and storing it in a variable
        load = Image.open("WIN_20180613_11_18_39_Pro.jpg")

        #Rendering an image: Converting a digital discription of something into an \
        #screen displayable image.
        render = ImageTk.PhotoImage(load)
        '''
           A Tkinter-compatible photo image.  This can be used
           everywhere Tkinter expects an image object.  If the image is an RGBA
           image, pixels having alpha 0 are treated as transparent.
   
           The constructor takes either a PIL image, or a mode and a size.
           Alternatively, you can use the **file** or **data** options to initialize
           the photo image object.
        '''

        #Label is not a part of Image, ImageTk
        #Labels are used for pack-in images or texts
        #Label widget which can display text and bitmaps.
        img = Label(self, image=render)
        #selecting the rendered image
        img.image = render
        img.place(x=0, y=0)
        
    def showTxt(self) :
        text = Label(self, text='Hey there good lookin!')
        #pack() basically adds the text.
        '''
            1. Why is text automatically coming in the center of the window?
            2. Also everytime showTxt is called, the text is being displayed below \
               the previously displayed text rather then overlapping. Why? And if this\
               is how it works, how do we overlap text? 
        '''
        text.pack()
        
root = Tk()
root.geometry("400x500")
app = Window(root)
root.mainloop()

#help(ImageTk.PhotoImage)                   #Don't bother yourself with these
#help(Label)


