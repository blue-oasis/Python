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
        Lottoset = set([])
        while(len(Lottoset) < 6) :
            Lottoset.add(random.randint(1, 45))

        Lottolist = list(Lottoset)
        Lottolist.sort()
        self.v1.set(str(Lottolist[0]))
        self.v2.set(str(Lottolist[1]))
        self.v3.set(str(Lottolist[2]))
        self.v4.set(str(Lottolist[3]))
        self.v5.set(str(Lottolist[4]))
        self.v6.set(str(Lottolist[5]))


            

lootto()

        
