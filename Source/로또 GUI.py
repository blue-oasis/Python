from tkinter import *
import random
class lootto:
    def __init__(self):
        window = Tk()
        window.title("로또 번호 예상 프로그램")

        frame1 = Frame(window)
        frame1.grid(row = 1, column = 1, pady = 10)
        Label(frame1, text = "숫자 1").pack(side = LEFT)
        Label(frame1, text = "숫자 2").pack(side = LEFT)
        Label(frame1, text = "숫자 3").pack(side = LEFT)
        Label(frame1, text = "숫자 4").pack(side = LEFT)
        Label(frame1, text = "숫자 5").pack(side = LEFT)
        Label(frame1, text = "숫자 6").pack(side = LEFT)

        frame2 = Frame(window)
        frame2.grid(row = 2, column = 1)
        self.v1 = StringVar()
        Entry(frame2, width = 5, textvariable = self.v1, justify = RIGHT).pack(side = LEFT)
        self.v2 = StringVar()
        Entry(frame2, width = 5, textvariable = self.v2, justify = RIGHT).pack(side = LEFT)
        self.v3 = StringVar()
        Entry(frame2, width = 5, textvariable = self.v3, justify = RIGHT).pack(side = LEFT)
        self.v4 = StringVar()
        Entry(frame2, width = 5, textvariable = self.v4, justify = RIGHT).pack(side = LEFT)
        self.v5 = StringVar()
        Entry(frame2, width = 5, textvariable = self.v5, justify = RIGHT).pack(side = LEFT)
        self.v6 = StringVar()
        Entry(frame2, width = 5, textvariable = self.v6, justify = RIGHT).pack(side = LEFT)

        frame3 = Frame(window)
        frame3.grid(row = 3, column = 1, pady = 10, sticky = E)
        Button(frame3, text = "시작", command = self.start).pack(side = LEFT)

        window.mainloop()

    def start(self):

        self.v1.set(str(random.randint(1, 45)))
        self.v2.set(str(random.randint(1, 45)))
        self.v3.set(str(random.randint(1, 45)))
        self.v4.set(str(random.randint(1, 45)))
        self.v5.set(str(random.randint(1, 45)))
        self.v6.set(str(random.randint(1, 45)))
        if self.v1 == self.v2 or self.v3 or self.v4 or self.v5 or self.v6 :
            self.v1.set(str(random.randint(1, 45)))
        if self.v2 == self.v3 or self.v4 or self.v5 or  self.v6 :
            self.v2.set(str(random.randint(1, 45)))
        if self.v3 == self.v4 or self.v5 or self.v6  :
            self.v3.set(str(random.randint(1, 45)))
        if self.v4 == self.v5 or self.v6 :
            self.v4.set(str(random.randint(1, 45)))
        if self.v5 == self.v6 :
            self.v5.set(str(random.randint(1, 45)))

            

lootto()

        
