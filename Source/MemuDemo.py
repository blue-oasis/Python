from tkinter import *

class MenuDemo:
    def __init__(self):
        window = Tk()
        window.title("메뉴 데모")

        menubar = Menu(window)
        window.config(menu = menubar)

        operationMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "연산", menu = operationMenu)
        operationMenu.add_command(label = "더하기", command = self.add)
        operationMenu.add_command(label = "빼기", command = self.subtract)
        operationMenu.add_command(label = "곱하기", command = self.multiply)
        operationMenu.add_command(label = "나누기", command = self.divide)

        exitmenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "나가기", menu = exitmenu)
        exitmenu.add_command(label = "종료", command = window.quit)

        frame0 = Frame(window)
        frame0.grid(row = 1, column = 1, sticky = W)

        plusImage = PhotoImage(file = "../image/plus.gif")
        minusImage = PhotoImage(file = "../image/minus.gif")
        timesImage = PhotoImage(file = "../image/times.gif")
        divideImage = PhotoImage(file = "../image/divide.gif")


        Button(frame0, image = plusImage, command = self.add).grid(row = 1, column = 1, sticky = W)
        Button(frame0, image = minusImage, command = self.subtract).grid(row = 1, column = 2)
        Button(frame0, image = timesImage, command = self.multiply).grid(row = 1, column = 3)
        Button(frame0, image = divideImage, command = self.divide).grid(row = 1, column = 4)

        frame1 = Frame(window)
        frame1.grid(row = 2, column = 1, pady = 10)
        Label(frame1, text = "숫자 1:").pack(side = LEFT)
        self.v1 = StringVar()
        Entry(frame1, width = 5, textvariable = self.v1, justify = RIGHT).pack(side = LEFT)
        Label(frame1, text = "숫자 2:").pack(side = LEFT)
        self.v2 = StringVar()
        Entry(frame1, width = 5, textvariable = self.v2, justify = RIGHT).pack(side = LEFT)
        Label(frame1, text = "결과").pack(side = LEFT)
        self.v3 = StringVar()
        Entry(frame1, width = 5, textvariable = self.v3, justify = RIGHT).pack(side = LEFT)
        
        
        frame2 = Frame(window)
        frame2.grid(row = 3, column = 1, pady = 10, sticky = E)
        Button(frame2, text = "더하기", command = self.add).pack(side = LEFT)
        Button(frame2, text = "빼기", command = self.subtract).pack(side = LEFT)
        Button(frame2, text = "곱하기", command = self.multiply).pack(side = LEFT)
        Button(frame2, text = "나누기", command = self.divide).pack(side = LEFT)

        mainloop()
                                 
    def add(self):
        self.v3.set(eval(self.v1.get()) + eval(self.v2.get()))
    def subtract(self):
        self.v3.set(eval(self.v1.get()) - eval(self.v2.get()))
    def multiply(self):
        self.v3.set(eval(self.v1.get()) * eval(self.v2.get()))
    def divide(self):
        self.v3.set(eval(self.v1.get()) / eval(self.v2.get()))
        

MenuDemo()
       

        
        
        
