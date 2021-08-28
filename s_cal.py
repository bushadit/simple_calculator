from tkinter import *

root = Tk()
root.title('Simple Calculator')

# Entry (calculus)

calc = Entry(root, width=40, borderwidth=5)
calc.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Defining buttons (numbers and operators)


def button_click():
    return


button_1 = Button(root, text='1', padx=40, pady=20, command=button_click)
button_2 = Button(root, text='2', padx=40, pady=20, command=button_click)
button_3 = Button(root, text='3', padx=40, pady=20, command=button_click)
button_4 = Button(root, text='4', padx=40, pady=20, command=button_click)
button_5 = Button(root, text='5', padx=40, pady=20, command=button_click)
button_6 = Button(root, text='6', padx=40, pady=20, command=button_click)
button_7 = Button(root, text='7', padx=40, pady=20, command=button_click)
button_8 = Button(root, text='8', padx=40, pady=20, command=button_click)
button_9 = Button(root, text='9', padx=40, pady=20, command=button_click)
button_0 = Button(root, text='0', padx=40, pady=20, command=button_click)

button_clear = Button(root, text='Clear', padx=80,
                      pady=20, command=button_click)
button_addi = Button(root, text='+', padx=40, pady=20, command=button_click)
button_minus = Button(root, text='-', padx=40, pady=20, command=button_click)
button_equal = Button(root, text='=', padx=40, pady=20, command=button_click)

# Putting the buttons on screen (grid)

button_1.grid(row=3, column=0, sticky=EW)
button_2.grid(row=3, column=1, sticky=EW)
button_3.grid(row=3, column=2, sticky=EW)

button_4.grid(row=2, column=0, sticky=EW)
button_5.grid(row=2, column=1, sticky=EW)
button_6.grid(row=2, column=2, sticky=EW)

button_7.grid(row=1, column=0, sticky=EW)
button_8.grid(row=1, column=1, sticky=EW)
button_9.grid(row=1, column=2, sticky=EW)

button_0.grid(row=4, column=0, sticky=EW)

button_clear.grid(row=4, column=1, columnspan=2, sticky=EW)
button_addi.grid(row=5, column=0, sticky=EW)
button_minus.grid(row=5, column=1, sticky=EW)
button_equal.grid(row=5, column=2, sticky=EW)

root.mainloop()
