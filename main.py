
from tkinter import *

root_bg = "#808080" #gray
root = Tk(className="Calculator")
root['background'] = root_bg
err = '#FF0000'  #red

def add():
    num1, num2 = e1.get(), e2.get()
    if num1 == '1/0' or num2 == '1/0' :
        label.config(text='Cannot Add with infinity', font='bold', fg=err)
    else:
        num1, num2 = int(num1), int(num2)
        sum1 = num1 + num2
        s = f"{num1} + {num2} = {sum1}"
        label.config(text=s)

def sub():
    num1, num2 = e1.get(), e2.get()
    if num1 == '1/0' and num2 == '1/0':
        label.config(text = 'Indeterminate Form', font='bold', fg=err)
    elif num1 == '1/0' or num2 == '1/0':
        label.config(text='Cannot Subtract with infinity', font='bold', fg=err)
    else:
        num1, num2 = int(num1), int(num2)
        minus = num1 - num2
        s = f"{num1} - {num2} = {minus}"
        label.config(text = s)

def product():
    num1, num2 = e1.get() , e2.get()
    if (num1 == '0' and num2 == '1/0') and (num1 == '1/0' or num2 == '0'):
        label.config(text = 'Inderterminate Form', font='bold', fg=err)
    if num2 == '1/0':
        label.config(text = 'Cannot Multiply with infinity', font='bold', fg=err)
    else:
        num1, num2 = int(num1), int(num2)
        mult = num1 * num2
        s = f"{num1} x {num2} = {mult}"
        label.config(text = s)

def quotient():
    num1 , num2 = e1.get(), e2.get()
    if (num1 == '1/0' and num2 == '1/0') or (num1 == '0' and num2 == '0'):
        label.config(text='Indeterminate Form', font = 'bold', fg=err)
    elif num1 == '1/0':
        label.config(text='Cannot divide Infinity', font='bold', fg=err)
    elif num2 == '0':
        label.config(text = 'Cannot Divide by Zero', font='bold', fg=err)
    elif num2 == '1/0' :
        label.config(text = 'Cannot Divide by Infinity', font='bold', fg=err)
    else:
        num1, num2 = int(num1), int(num2)
        div = num1 / num2
        s = f"{num1} / {num2} = {div}"
        label.config(text = s)

def remainder():
    num1 , num2 = e1.get(), e2.get()
    if (num1 == '1/0' and num2 == '1/0') or (num1 == '0' and num2 == '0'):
        label.config(text='Indeterminate Form', font = 'bold', fg=err)
    elif num1 == '1/0':
        label.config(text='Cannot divide Infinity', font='bold', fg=err)
    elif num2 == '0':
        label.config(text = 'Cannot Divide by Zero', font='bold', fg=err)
    elif num2 == '1/0' :
        label.config(text = 'Cannot Divide by Infinity', font='bold', fg=err)
    else:
        num1, num2 = int(num1), int(num2)
        rem = num1 % num2
        s = f"{num1} % {num2} = {rem}"
        label.config(text = s)


w = Label(root, text = "CALCULATOR", font='arial 25', bg= root_bg, fg='#191970') #midnightblue
w.pack()

bc = '#FFFFF0'  #Ivory
hc = '#F5F5DC'  #Biege
fg = '#000000'
Label(root, text = "Number1", font = 'bold', bg=root_bg, fg=fg).pack() #grid(row = 1, column = 0)
e1 = Entry(root, bg=bc, highlightcolor=hc)
e1.pack() #grid(row = 1, column = 1)
Label(root, text = "Number2", font='bold', bg=root_bg, fg=fg).pack() #grid(row = 2, column = 0)
e2 = Entry(root, bg=bc, highlightcolor=hc)
e2.pack() #grid(row = 2, column = 1)

y = 160
w = 2
h = 1
act = '#5F9EA0'  #cadetblue
back = '#708090'  #slategrey
f = 'bold'
Button(root, text = "+", command = add, width=w, height=h, activebackground=act, bg=back, font=f, padx=2, pady=2).place(x=530, y=y)
Button(root, text = "-", command=sub, width=w, height=h, activebackground=act, bg=back, font=f, padx=2, pady=2).place(x=578, y=y)
Button(root, text = "x", command=product, width=w, height=h, activebackground=act, bg=back, font=f, padx=2, pady=2).place(x=628, y=y)
Button(root, text = "/", command=quotient, width=w, height=h, activebackground=act, bg=back, font=f, padx=2, pady=2).place(x=678, y=y)
Button(root, text = "%", command=remainder, width=w, height=h, activebackground=act, bg=back, font=f, padx=2, pady=2).place(x=728, y=y)

Label(root, text = "Result", font=f+' 25', bg=root_bg).place(x=600, y=240)
label = Label(root, width=25, height=2, font='bold', background=bc)
label.place(x=500, y=300)

root.mainloop()
#THE END
