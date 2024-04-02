from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Football.program")

#Input name team
Tfb_1=StringVar()
Label(text="ทีมที่-1",padx=10,font=30).grid(row=0,column=1,sticky=W)
et1=Entry(font=30,textvariable=Tfb_1)
et1.grid(row=0,column=2)

Tfb_2=StringVar()
Label(text="ทีมที่-2",padx=10,font=30).grid(row=0,column=3,sticky=W)
et2=Entry(font=30,textvariable=Tfb_2)
et2.grid(row=0,column=4)

Tfb_3=StringVar()
Label(text="ทีมที่-3",padx=10,font=30).grid(row=1,column=1,sticky=W)
et3=Entry(font=30,textvariable=Tfb_3)
et3.grid(row=1,column=2)

Tfb_4=StringVar()
Label(text="ทีมที่-4",padx=10,font=30).grid(row=1,column=3,sticky=W)
et4=Entry(font=30,textvariable=Tfb_4)
et4.grid(row=1,column=4)

#1vs2
scr_Tfb_1_1=StringVar()
Label(text="ทีม-1",padx=10,font=30).grid(row=5,column=1,sticky=N)
et6=Entry(font=30,textvariable=scr_Tfb_1_1)
et6.grid(row=5,column=2)

scr_Tfb_2_1=StringVar()
Label(text="ทีม-2",padx=10,font=30).grid(row=5,column=3,sticky=N)
et7=Entry(font=30,textvariable=scr_Tfb_2_1)
et7.grid(row=5,column=4)

#output
Label(text="ผลการแข่งขัน")


def cal():
    point_1=[]
    point_2=[]

    score_good_1=[]
    score_bad_1=[]

    score_good_2=[]
    score_bad_2=[]

    #('home',Tfb_1,'Vs','visit',Tfb_2,'(1)')

    score_good_1.append(scr_Tfb_1_1)
    score_bad_1.append(scr_Tfb_2_1)

    score_good_2.append(scr_Tfb_2_1)
    score_bad_2.append(scr_Tfb_1_1)

    if scr_Tfb_1_1 == scr_Tfb_2_1 :
        print(Tfb_1,'peer',Tfb_2)
        point_1.append(1)
        point_2.append(1)

    elif scr_Tfb_1_1 > scr_Tfb_2_1 :
        print(Tfb_1,'Win')
        print(Tfb_2,'Lose')
        point_1.append(3)
        point_2.append(0)
    else:
        print(Tfb_1,'Lose')
        print(Tfb_2,'Win')
        point_1.append(0)
        point_2.append(3)
    

Button(text="คำนวณ",font=30,width=15,command=cal).grid(row=6,column=2,sticky=W)





root.mainloop()