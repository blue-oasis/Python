import tkinter

window=tkinter.Tk()
window.title("체크버튼")
window.geometry("640x480+100+100")
window.resizable(True, True)

def flash():
    checkbutton3.flash()

CheckVariety_1=tkinter.IntVar()
CheckVariety_2=tkinter.IntVar()
CheckVariety_3=tkinter.IntVar()

checkbutton1=tkinter.Checkbutton(window, text="O", variable=CheckVariety_1, activebackground="blue")
checkbutton2=tkinter.Checkbutton(window, text="△", variable=CheckVariety_2, command=checkbutton1.flash)
checkbutton3=tkinter.Checkbutton(window, text="X", variable=CheckVariety_3, command=flash, activebackground="red")

checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()

window.mainloop()