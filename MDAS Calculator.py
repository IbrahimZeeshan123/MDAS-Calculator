from tkinter import*

root = Tk()
root.geometry("1350x650+0+0")
root.title("MDAS Calculator")
root.configure(background='black')

Tops =Frame(root, width=1350, height =50, bd=16 , relief="raise")
Tops.pack(side=TOP)
Botto =Frame(root, width=1350, height =700, bd=16 , relief="raise")
Botto.pack(side=BOTTOM)

LbLInfo= Label(Tops, font=('Helvetica', 50, 'bold'), text ="MDAS Calculator", bd=16) .grid(row=0, column=0)
inBotto1=Frame(Botto, width=650, height=300, relief="raise")
inBotto1.pack(side=BOTTOM)

inBotto2=Frame(Botto, width=650, height=400,bd=16, relief="raise")
inBotto2.pack(side=BOTTOM)

LF=Frame(inBotto2, width=1350, height=400,bd=16, relief="raise")
LF.pack(side=LEFT)
RF=Frame(inBotto2, width=1350, height=400,bd=16, relief="raise")
RF.pack(side=RIGHT)

Buttons=Frame(inBotto1, width=1350, height=100,bd=16, relief="raise")
Buttons.pack(side=BOTTOM)
AnsBotto2=Frame(inBotto1, width=1350, height=200,bd=16, relief="raise")
AnsBotto2.pack(side=BOTTOM)

def Sum():
    if var.get() == 1:
        Qty1 = float(firstnum.get())
        Qty2 = float(firstnum.get())
        Sumup= Qty1 + Qty2
        Total.set(Sumup)
    elif var.get() == 2:
        Qty1 = float(firstnum.get())
        Qty2 = float(firstnum.get())
        Sumup= Qty1 - Qty2
        Total.set(Sumup)
    elif var.get() == 3:
        Qty1 = float(firstnum.get())
        Qty2 = float(firstnum.get())
        Sumup = Qty1 * Qty2
        Total.set(Sumup)
    elif var.get() == 4:
        Qty1 = float(firstnum.get())
        Qty2 = float(firstnum.get())
        Sumup = Qty1 / Qty2
        Total.set(Sumup)
    elif var.get() == 5:
        Qty1 = float(firstnum.get())
        Qty2 = float(firstnum.get())
        Sumup = Qty1 % Qty2
        Total.set(Sumup)
    elif var.get() == 6:
        Qty1 = float(firstnum.get())
        Qty2 = float(firstnum.get())
        Sumup = Qty1 ** Qty2
        Total.set(Sumup)
    else:
        Qty1 = float(firstnum.get())
        Qty2 = float(firstnum.get())
        Sumup = Qty1 // Qty2
        Total.set(Sumup)


def Exit():
    qExit = messagebox.askyesno("MDAS System", "Do you want to exit the system?")
    if qExit > 0:
        root.destroy()
        return

def Reset():
    firstnum.set("")
    secondnum.set("")
    Total.set("")

var = IntVar()
firstnum= IntVar()
secondnum = IntVar()
Total = IntVar()


firstnum.set("")
secondnum.set("")
Total.set("")

Addition = Radiobutton(LF, text="Addition                                 ", variable=var, value=1,
                       font=('Helvetica',12, 'bold')).grid(row=0, sticky=W)

Subtraction = Radiobutton(LF, text="Subtraction                           ", variable=var, value=2,
                       font=('Helvetica',12, 'bold')).grid(row=1, sticky=W)

Multiplication = Radiobutton(LF, text="Multiplication                     ", variable=var, value=3,
                       font=('Helvetica',12, 'bold')).grid(row=2, sticky=W)

Division = Radiobutton(LF, text="Division                                 ", variable=var, value=4,
                       font=('Helvetica',12, 'bold')).grid(row=3, sticky=W)

Modulus = Radiobutton(RF, text="Modulus                                   ", variable=var, value=5,
                       font=('Helvetica',12, 'bold')).grid(row=4, sticky=W)

Exponent = Radiobutton(RF, text="Exponent                                 ", variable=var, value=6,
                       font=('Helvetica',12, 'bold')).grid(row=5, sticky=W)

Floor_Division = Radiobutton(RF, text="Floor Division                      ", variable=var, value=7,
                       font=('Helvetica',12, 'bold')).grid(row=6, sticky=W)

Space = Radiobutton(LF, text="                                       ",
                        indicatoron=0,variable=var, value=8,
                       font=('Helvetica',12, 'bold')).grid(row=7, sticky=W)

LbLfirst= Label(AnsBotto2,font=('Helvetica' , 13,'bold'), text="Enter First Number",
            fg="black", bd=16).grid(row=0,column=0, sticky=W)
txtfirst = Entry(AnsBotto2,font=('Helvetica' , 13,'bold'), bd=4, width=34,bg="white",
             textvariable=firstnum ).grid(row=0,column=1)
LbLsecond= Label(AnsBotto2,font=('Helvetica' , 13,'bold'), text="Enter Second Number",
            fg="black", bd=16).grid(row=1,column=0, sticky=W)
txtsecond = Entry(AnsBotto2,font=('Helvetica' , 13,'bold'), bd=4, width=34,bg="white",
             textvariable=secondnum ).grid(row=1,column=1)

LblTotal = Label(AnsBotto2, font=('Helvetica', 13,'bold'),text="Answer is  ",fg="black", bd=16,justify = "left")
LblTotal.grid(row=2,column=0, sticky=W)

LAnswer  = Label(AnsBotto2,font=('Helvetica' , 13,'bold'), bd=4, width=34,bg="white",
                 textvariable=Total, relief='sunken').grid(row=2,column=1, sticky=W)

sumUp=Button(Buttons,pady=8, bd=8, fg="black",font=('Helvetica', 16,'bold'), width=12,  command=Sum,
             text="Sum Up", bg="white").grid(row=0, column=0)
Reset=Button(Buttons,pady=8, bd=8, fg="black",font=('Helvetica', 16,'bold'), width=12,  command=Reset,
             text="Reset", bg="white").grid(row=0, column=1)
Exit=Button(Buttons,pady=8, bd=8, fg="black",font=('Helvetica', 16,'bold'), command=Exit,     width=12,
             text="Exit", bg="white").grid(row=0, column=2)

root.mainloop()