import csv
from os import name
from tkinter import*
from tkinter import ttk

#--------------file path------------------


# ----------------------------หน้าต่างโปรแกรม-------------------------------------

football = Tk()
football.title("Program Football")


#-------------------tabs-------------------------------------------------

my_notebook = ttk.Notebook(football)
my_notebook.pack(pady=15)


#------------Frame ------------------------------------

my_frame1 = Frame(football,width=100,height=300)
my_frame2 = Frame(football,width=100,height=300)
my_frame3 = Frame(football,width=100,height=300)
my_frame4 = Frame(football,width=100,height=300)
my_frame5 = Frame(football,width=100,height=300)


#------------Frame grid------------------------------------

my_frame1.pack(fill="both",expand=1)
my_frame2.pack(fill="both",expand=1)
my_frame3.pack(fill="both",expand=1)
my_frame4.pack(fill="both",expand=1)
my_frame5.pack(fill="both",expand=1)
my_notebook.add(my_frame1,text="Name Team")
my_notebook.add(my_frame2,text="first round")
my_notebook.add(my_frame3,text="second round")
my_notebook.add(my_frame4,text="Third round")
my_notebook.add(my_frame5,text="round four")







#_------------------------- My Frame 1-----------------------------------------------------------


#------------- define---------

def submit():
    global name_team_1
    global name_team_2
    global name_team_3
    global name_team_4
    name_team_1 = name_t1.get()
    name_team_2 = name_t2.get()
    name_team_3 = name_t3.get()
    name_team_4 = name_t4.get()
    title_lb = Label(my_frame1,text="TEAM NAME",font="Helevic 14 bold italic ",bg="Blue",fg="white")
    lb_1 = Label(my_frame1,text="Team 1 : " + name_team_1,font="Tohama 11  ")
    lb_2 = Label(my_frame1,text="Team 2 : " + name_team_2,font="Tohama 11  ")
    lb_3 = Label(my_frame1,text="Team 3 : " + name_team_3,font="Tohama 11  ")
    lb_4 = Label(my_frame1,text="Team 4 : " + name_team_4,font="Tohama 11  ")
    title_lb.grid(row=6,column=1,columnspan=3,pady=15)
    lb_1.grid(row=7,column=1,pady=15,padx=20,sticky=W,columnspan=2)
    lb_2.grid(row=8,column=1,pady=15,padx=20,sticky=W,columnspan=2)
    lb_3.grid(row=9,column=1,pady=15,padx=20,sticky=W,columnspan=2)
    lb_4.grid(row=10,column=1,pady=15,padx=20,sticky=W,columnspan=2)


#------------------------My frame2-----------------------------
    #--------------Label VS---------------------------------------------

    vs_1 = Label(my_frame2,text="VS")
    name_t_1_12 = Label(my_frame2,text=name_team_1)
    name_t_1_21 = Label(my_frame2,text=name_team_2)
    name_t_1_12.grid(row=2,column=1)
    name_t_1_21.grid(row=2,column=5)
    vs_1.grid(row=2,column=3)

    vs_2 = Label(my_frame2,text="VS")
    name_t_1_13 = Label(my_frame2,text=name_team_1)
    name_t_1_31 = Label(my_frame2,text=name_team_3)
    name_t_1_13.grid(row=3,column=1)
    name_t_1_31.grid(row=3,column=5)
    vs_2.grid(row=3,column=3)


    vs_3 = Label(my_frame2,text="VS")
    name_t_1_14 = Label(my_frame2,text=name_team_1)
    name_t_1_41 = Label(my_frame2,text=name_team_4)
    name_t_1_14.grid(row=4,column=1)
    name_t_1_41.grid(row=4,column=5)
    vs_3.grid(row=4,column=3)
 



    #-------------------Entry VS firs -----------------------------

    name_te12 = Entry(my_frame2,width=5)
    name_te21 = Entry(my_frame2,width=5)
    name_te12.grid(row=2,column=2)
    name_te21.grid(row=2,column=4)

    name_te13 = Entry(my_frame2,width=5)
    name_te31 = Entry(my_frame2,width=5)
    name_te13.grid(row=3,column=2)
    name_te31.grid(row=3,column=4)

    name_te14 = Entry(my_frame2,width=5)
    name_te41 = Entry(my_frame2,width=5)
    name_te14.grid(row=4,column=2)
    name_te41.grid(row=4,column=4)




def clear():
    name_t1.delete(0,END)
    name_t2.delete(0,END)
    name_t3.delete(0,END)
    name_t4.delete(0,END)








 
    

#-------------------Entry input name team--------------------
name_t1 = Entry(my_frame1,width=30,borderwidth=1)
name_t2 = Entry(my_frame1,width=30,borderwidth=1)
name_t3 = Entry(my_frame1,width=30,borderwidth=1)
name_t4 = Entry(my_frame1,width=30,borderwidth=1)
name_t1.grid(row = 1 , column = 2,padx=10,pady=10)
name_t1.focus()
name_t2.grid(row = 2 , column = 2,padx=20,pady=10)
name_t3.grid(row = 3 , column = 2,padx=20,pady=10)
name_t4.grid(row = 4 , column = 2,padx=20,pady=10)

#--------------------- Label name team------------------
name_t1_lb = Label(my_frame1,text="Team 1 ",font="Tohama 11  ")
name_t2_lb = Label(my_frame1,text="Team 2 ",font="Tohama 11  ")
name_t3_lb = Label(my_frame1,text="Team 3 ",font="Tohama 11  ")
name_t4_lb = Label(my_frame1,text="Team 4 ",font="Tohama 11 ")
name_t1_lb.grid(row=1 ,column=1,padx=10)
name_t2_lb.grid(row=2 ,column=1,padx=10)
name_t3_lb.grid(row=3 ,column=1,padx=10)
name_t4_lb.grid(row=4 ,column=1,padx=10)

#------------------button name team--------------------
submit_bt=Button(my_frame1,text="Submit",command=submit,font="Verdana 10 ",padx=50,pady=5)
clear_bt=Button(my_frame1,text="Clear",command=clear,font="Verdana 10 ",padx=60,pady=5)
submit_bt.grid(row=5,column=1,padx=10)
clear_bt.grid(row=5,column=2,sticky=E,padx=10)


#_-------------------------  End My Frame 1-----------------------------------------------------------


















mainloop()