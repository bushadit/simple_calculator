from tkinter import *

root = Tk()
root.title('Simple Calculator')

# Entry (calculus)

calc = Entry(root, width=40, borderwidth=5)
calc.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Defining button (numbers and operators)


def button_click(number):
    current = calc.get()
    calc.delete(0, END)
    calc.insert(0, str(current) + str(number))


def button_clear():
    calc.delete(0, END)


def button_addi():
    first_number = calc.get()
    global math
    global f_num
    math = 'addition'
    f_num = float(first_number)
    calc.delete(0, END)


def button_sub():
    first_number = calc.get()
    global math
    global f_num
    math = 'subtraction'
    f_num = float(first_number)
    calc.delete(0, END)


def button_mult():
    first_number = calc.get()
    global math
    global f_num
    math = 'multiplication'
    f_num = float(first_number)
    calc.delete(0, END)


def button_div():
    first_number = calc.get()
    global math
    global f_num
    math = 'division'
    f_num = float(first_number)
    calc.delete(0, END)


def button_equal():
    second_number = calc.get()
    calc.delete(0, END)

    if math == 'addition':
        calc.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        calc.insert(0, f_num - int(second_number))
    if math == 'multiplication':
        calc.insert(0, f_num * int(second_number))
    if math == 'division':
        calc.insert(0, f_num / int(second_number))


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
                      command=button_equal)
button_sub = Button(root, text='-', padx=40, pady=20,
                    command=button_sub)
button_mult = Button(root, text='*', padx=40, pady=20,
                     command=button_mult)
button_div = Button(root, text='/', padx=40, pady=20,
                    command=button_div)

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
button_sub.grid(row=6, column=0, sticky=EW)
button_mult.grid(row=6, column=1, sticky=EW)
button_div.grid(row=6, column=2, sticky=EW)

root.mainloop()
