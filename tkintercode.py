from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='First number')
        self.lbl2=Label(win, text='Second number')
        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Subtract')
        self.btn3=Button(win, text='Multiply')
        self.btn4=Button(win, text='Divide')
        self.btn5=Button(win, text='Mod')
        self.btn6 = Button(win, text='x^y')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1=Button(win, text='Add')
        self.b1.bind('<Button-1>', self.add)
        self.b2=Button(win, text='Subtract')
        self.b2.bind('<Button-1>', self.sub)
        self.b3=Button(win, text='Multiply')
        self.b3.bind('<Button-1>', self.mul)
        self.b4=Button(win, text='Divide')
        self.b4.bind('<Button-1>', self.div)
        self.b5=Button(win, text='Mod')
        self.b5.bind('<Button-1>', self.mod)
        self.b6=Button(win, text='x^y')
        self.b6.bind('<Button-1>', self.xraisey)
        self.b1.place(x=30, y=150)
        self.b2.place(x=100, y=150)
        self.b3.place(x=200, y=150)
        self.b4.place(x=300, y=150)
        self.b5.place(x=400, y=150)
        self.b6.place(x=500, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
    def add(self,event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))
    def mul(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1*num2
        self.t3.insert(END, str(result))
    def div(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1/num2
        self.t3.insert(END, str(result))
    def mod(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1%num2
        self.t3.insert(END, str(result))
    def xraisey(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1**num2
        self.t3.insert(END, str(result))

window=Tk()
mywin=MyWindow(window)
window.title('Tkinter Calculator')
window.geometry("400x300+10+10")
window.mainloop()
