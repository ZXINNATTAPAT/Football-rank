from tkinter import*

# ----------------------------หน้าต่างโปรแกรม-------------------------------------

football = Tk()
football.title("Program Football")
football.minsize(400,400)
#-------define------------------------------------------------------------


def bt_1():
    global name_team_1
    name_team_1 = team_1.get()
    lb_1 = Label(football,text="Team 1 : " + name_team_1)
    lb_1.grid(row=0,column=2)

def bt_2():
    global name_team_2
    name_team_2 = team_2.get()
    lb_2 = Label(football,text="Team 2 : " + name_team_2)
    lb_2.grid(row=1,column=2)

def bt_3():
    global name_team_3
    name_team_3 = team_3.get()
    lb_3 = Label(football,text="Team 3 : " + name_team_3)
    lb_3.grid(row=2,column=2)

def bt_4():
    global name_team_4
    name_team_4 = team_4.get()
    lb_4 = Label(football,text="Team 4 : " + name_team_4)
    lb_4.grid(row=3,column=2)

#-----------------def clear------------------
def bt_clear():
    team_1.delete(0,END)
    team_2.delete(0,END)
    team_3.delete(0,END)
    team_4.delete(0,END)

#-----------------------Entry input team------------------
team_1 = Entry(football,width=20 ,borderwidth=3)
team_2 = Entry(football,width=20,borderwidth=3)
team_3 = Entry(football,width=20,borderwidth=3)
team_4 = Entry(football,width=20,borderwidth=3)

#-----------grid Entry team---------------------
team_1.grid(row=0 , column=1 ,padx=10,pady=10 )
team_1.focus()
team_2.grid(row=1 , column=1 ,padx=10,pady=10 )
team_2.focus()
team_3.grid(row=2 , column=1 ,padx=10,pady=10 )
team_3.focus()
team_4.grid(row=3 , column=1 ,padx=10,pady=10 )
team_4.focus()



#--button team---------------------------------
bt_1 = Button(football,text="Team 1",command=bt_1,padx=20,pady=10)
bt_2 = Button(football,text="Team 2",command=bt_2,padx=20,pady=10)
bt_3 = Button(football,text="Team 3",command=bt_3,padx=20,pady=10)
bt_4 = Button(football,text="Team 4",command=bt_4,padx=20,pady=10)

#-----------grid Button team---------------------
bt_1.grid(row=0,column=0,padx=20,pady=10)
bt_2.grid(row=1,column=0,padx=20,pady=10)
bt_3.grid(row=2,column=0,padx=20,pady=10)
bt_4.grid(row=3,column=0,padx=20,pady=10)


#----button clear---------------------------
bt_clear = Button(football,text="CLEAR",command=bt_clear,padx=40,pady=20)
bt_clear.grid(row=4,column=1)


mainloop()