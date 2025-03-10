from tkinter import Tk,Button,Entry,Label
import modules

############################################################################
root = Tk()
root.geometry("600x600+0+0")
root.resizable(False,False)
root.config(bg="#ff8")

###########################################################################
create_button = Button(root,text="Create CSV",command= lambda:modules.creation_window(root,Entry,150,10,Button,Label))
create_button.config(font=["Arial",20,"bold",],fg="red")
create_button.pack()
read_button = Button(root,text="Read CSV",command="")
read_button.config(font=["Arial",20,"bold",],fg="red")
read_button.pack()





############################################################################
root.mainloop()
