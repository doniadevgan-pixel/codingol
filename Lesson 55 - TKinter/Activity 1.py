from tkinter import *

window = Tk()
window.title("My Profile Card")
window.geometry('400x380')


# Part 2 - Add a title label at the top using grid

title = Label(window, text="My proile card", fg="white", bg="purple", width=40)
title.grid(row=0, column=0, columnspan=2, padx=15, pady=10)

# part 3 - 
window.mainloop()