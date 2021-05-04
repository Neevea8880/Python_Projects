#Calculator using tkinter.....

from tkinter import *


window = Tk()
window.title("CALCULATOR")
window.geometry("350x400")
window.resizable(0,0)


def button_click(num):
   global exp
   exp = exp + str(num)
   input_text.set(exp)

def text_clear():
   global exp
   exp=" "
   input_text.set("")

def equal_click():
   global exp
   res=str(eval(exp))
   input_text.set(res)
   exp=" "

exp=" "
input_text = StringVar()


entry=Entry(window, text=input_text, bd=5)
entry.grid(columnspan=4, ipadx=100, ipady=10)

frame = Frame(window, width = 310, height = 280, bg = "#9E9FA0")
frame.grid(columnspan=4, rowspan=5)

button1=Button(window, text="7", borderwidth=20, bg="#E1F9F5", command= lambda: button_click(7),)
button1.grid(row=1,column=0, padx = 5, pady = 5)
button2=Button(window, text="8", borderwidth=20, bg="#E1F9F5", command= lambda: button_click(8))
button2.grid(row=1,column=1)
button3=Button(window, text="9", borderwidth=20, bg="#E1F9F5", command= lambda: button_click(9))
button3.grid(row=1,column=2)
button10=Button(window, text="/", borderwidth=20, bg="#BCDEF0", command= lambda: button_click("/"))
button10.grid(row=1,column=3, padx = 8, pady = 5)
button4=Button(window, text="4", borderwidth=20, bg="#E1F9F5", command= lambda: button_click(4))
button4.grid(row=2,column=0, padx = 5, pady = 5)
button5=Button(window, text="5", borderwidth=20, bg="#E1F9F5", command= lambda: button_click(5))
button5.grid(row=2,column=1)
button6=Button(window, text="6", borderwidth=20, bg="#E1F9F5", command= lambda: button_click(6))
button6.grid(row=2,column=2)
button11=Button(window, text="*", borderwidth=20, bg="#BCDEF0", command= lambda: button_click("*"))
button11.grid(row=2,column=3)
button7=Button(window, text="1", borderwidth=20, bg="#E1F9F5", command= lambda: button_click(1))
button7.grid(row=3,column=0, padx = 5, pady = 5)
button8=Button(window, text="2", borderwidth=20, bg="#E1F9F5", command= lambda: button_click(2))
button8.grid(row=3,column=1)
button9=Button(window, text="3", borderwidth=20, bg="#E1F9F5", command= lambda: button_click(3))
button9.grid(row=3,column=2)
button12=Button(window, text="-", borderwidth=20, bg="#BCDEF0", command= lambda: button_click("-"))
button12.grid(row=3,column=3)
button13=Button(window, text=".", borderwidth=20, bg="#BCDEF0", command= lambda: button_click("."))
button13.grid(row=4,column=0, padx = 5, pady = 5)
button14=Button(window, text="0", borderwidth=20, bg="#E1F9F5", command= lambda: button_click(0))
button14.grid(row=4,column=1)
button15=Button(window, text="=", borderwidth=20, bg="#BCDEF0", command= lambda: equal_click())
button15.grid(row=4,column=2)
button16=Button(window, text="+", borderwidth=20,bg="#BCDEF0", command= lambda: button_click("+"))
button16.grid(row=4,column=3)

button17=Button(window, text="Clear" , bg="#BCDEF0",width=10, borderwidth=20, command= lambda: text_clear())
button17.grid( columnspan = 4, padx = 5, pady = 5)



window.mainloop()
