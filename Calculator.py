#Nicholas Pomroy and Adam Fry

import tkinter as tk

root = tk.Tk()
root.title('Calculator')
root.geometry('600x600')
root.columnconfigure(1,weight=1)

message_var = tk.StringVar(root)
message_input = tk.Entry(root,textvariable=message_var)

def on_submit():
    message_var.set('')

def one():
    temp= message_var.get()
    temp +='1'
    message_var.set(temp)

def two():
    temp= message_var.get()
    temp +='2'
    message_var.set(temp)

def three():
    temp= message_var.get()
    temp +='3'
    message_var.set(temp)

def four():
    temp= message_var.get()
    temp +='4'
    message_var.set(temp)

def five():
    temp= message_var.get()
    temp +='5'
    message_var.set(temp)

def six():
    temp= message_var.get()
    temp +='6'
    message_var.set(temp)

def seven():
    temp= message_var.get()
    temp +='7'
    message_var.set(temp)

def eight():
    temp= message_var.get()
    temp +='8'
    message_var.set(temp)

def nine():
    temp= message_var.get()
    temp +='9'
    message_var.set(temp)

def zero():
    temp= message_var.get()
    temp +='0'
    message_var.set(temp)

def plus():
    temp= message_var.get()
    temp +='+'
    message_var.set(temp)

def minus():
    temp= message_var.get()
    temp +='-'
    message_var.set(temp)

def multiply():
    temp= message_var.get()
    temp +='*'
    message_var.set(temp)

def divide():
    temp= message_var.get()
    temp +='/'
    message_var.set(temp)

# first row
message_label = tk.Label(
    root,
    text='Please enter your calculation:',
    font=('Arial 16 bold'),
    bg='red',
    fg='#FF0'
)
message_var = tk.StringVar(root)
message_input = tk.Entry(root,textvariable=message_var)
message_label.grid(row=0,column=0,sticky=(tk.E),padx=25)
message_input.grid(row=0,column=1,sticky=(tk.N,tk.S,tk.E,tk.W))

# third row
one_btn = tk.Button(root,text='1')
one_btn.grid(row=2,column=0,sticky=(tk.E),padx=10,pady=10)
one_btn.configure(command=one)

two_btn = tk.Button(root,text='2')
two_btn.grid(row=2,column=1,sticky=(tk.E),padx=10,pady=10)
two_btn.configure(command=two)

three_btn = tk.Button(root,text='3')
three_btn.grid(row=2,column=2,sticky=(tk.E),padx=10,pady=10)
three_btn.configure(command=three)

four_btn = tk.Button(root,text='4')
four_btn.grid(row=3,column=0,sticky=(tk.E),padx=10,pady=10)
four_btn.configure(command=four)

five_btn = tk.Button(root,text='5')
five_btn.grid(row=3,column=1,sticky=(tk.E),padx=10,pady=10)
five_btn.configure(command=five)

six_btn = tk.Button(root,text='6')
six_btn.grid(row=3,column=2,sticky=(tk.E),padx=10,pady=10)
six_btn.configure(command=six)

seven_btn = tk.Button(root,text='7')
seven_btn.grid(row=4,column=0,sticky=(tk.E),padx=10,pady=10)
seven_btn.configure(command=seven)

eight_btn = tk.Button(root,text='8')
eight_btn.grid(row=4,column=1,sticky=(tk.E),padx=10,pady=10)
eight_btn.configure(command=eight)

nine_btn = tk.Button(root,text='9')
nine_btn.grid(row=4,column=2,sticky=(tk.E),padx=10,pady=10)
nine_btn.configure(command=nine)

zero_btn = tk.Button(root,text='0')
zero_btn.grid(row=5,column=0,sticky=(tk.E),padx=10,pady=10)
zero_btn.configure(command=zero)

multiply_btn = tk.Button(root,text='*')
multiply_btn.grid(row=5,column=1,sticky=(tk.E),padx=10,pady=10)
multiply_btn.configure(command=multiply)

divide_btn = tk.Button(root,text='/')
divide_btn.grid(row=5,column=2,sticky=(tk.E),padx=10,pady=10)
divide_btn.configure(command=divide)

plus_btn = tk.Button(root,text='+')
plus_btn.grid(row=6,column=0,sticky=(tk.E),padx=10,pady=10)
plus_btn.configure(command=plus)

minus_btn = tk.Button(root,text='-')
minus_btn.grid(row=6,column=1,sticky=(tk.E),padx=10,pady=10)
minus_btn.configure(command=minus)

calculate_btn = tk.Button(root,text='clear')
calculate_btn.grid(row=6,column=2,sticky=(tk.E),padx=10,pady=10)
calculate_btn.configure(command=on_submit)

root.mainloop()