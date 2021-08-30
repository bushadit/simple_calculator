from tkinter import *

root = Tk()
root.title('Simple Calculator')

# Entry (calculus)

calc = Entry(root, width=40, borderwidth=5)
calc.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Defining buttons (numbers and operators)


def button_click(number):
    current = calc.get()
    calc.delete(0, END)
    calc.insert(0, str(current) + str(number))


def button_clear():
    calc.delete(0, END)


def button_addi():
    first_number = calc.get()
    global f_num
    f_num = int(first_number)
    calc.delete(0, END)


button_1 = Button(root, text='1', padx=40, pady=20,
                  command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20,
                  command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20,
                  command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20,
                  command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20,
                  command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20,
                  command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20,
                  command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20,
                  command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20,
                  command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20,
                  command=lambda: button_click(0))

button_clear = Button(root, text='Clear', padx=80,
                      pady=20, command=button_clear)
button_addi = Button(root, text='+', padx=40, pady=20,
                     command=button_addi)
button_equal = Button(root, text='=', padx=80, pady=20,
                      command=lambda: button_click())

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
button_equal.grid(row=5, column=1, columnspan=2, sticky=EW)

root.mainloop()
