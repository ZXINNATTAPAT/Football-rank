from os import read, write
from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv


#import mysql.connector

root = Tk()
root.title("FOOTBALL MATCH")
#root.iconbitmap("C:/Users/sarif/Desktop/project.compro/GUI/icon.ico")


wrapper1 = LabelFrame(root,text="NAME TEAM",font="Roboto 11",fg="#570D90")
wrapper2 = LabelFrame(root,text="MATCH SCORE",font="Roboto 11",fg="#570D90")
wrapper3 = LabelFrame(root,text="TABLE SCORE",font="Roboto 11",fg="#570D90")

wrapper1.pack(fill="both", expand="yes",padx=20,pady=20)
wrapper2.pack(fill="both", expand="yes",padx=20,pady=20)
wrapper3.pack(fill="both", expand="yes",padx=20,pady=20)
# file path

filepath = 'myfile.csv'

root.configure(background="#ADFAB6")
wrapper1.configure(background="#EFDB43")
wrapper2.configure(background="#EFDB43")
wrapper3.configure(background="#EFDB43")
#wraooer 1 ---------------------------------------------

# list ชื่อทีมฟุตบอล
listteam = []
def sb():
    global mycombo_1
    global mycombo_2
    listteam.append(input_name_team.get())
    mycombo_1 = ttk.Combobox(wrapper2,value=listteam)
    mycombo_2 = ttk.Combobox(wrapper2,value=listteam)
    mycombo_1.bind("<<ComboboxSelected>>",submit)
    mycombo_2.bind("<<ComboboxSelected>>",submit)
    mycombo_1.grid(row=2,column=1)
    mycombo_2.grid(row=2,column=5)
    input_name_team.delete(0,END)

#my combo


#text 
Enter_name_team = Label(wrapper1,text="Enter Name Team : ",font="Roboto 12 bold  ",fg="#6F126F",bg="#EFDB43")
Enter_name_team.grid(row=1,column=1,pady=20,padx=10,sticky=E)



#input name team
input_name_team = Entry(wrapper1,width=20,font="Roboto 12  bold ",fg="#4A0606",bg="#FAC7C7",borderwidth=3)
input_name_team.grid(row=1,column=2,columnspan=3,pady=20,padx=10)

# bt
btsubmit = Button(wrapper1,text="Add Name Team",command=sb,font="Roboto 11 bold  ",fg="#FFFFFF",bg="#054B0D")
btsubmit.grid(row=2,column=1,columnspan=5,ipadx=50,padx=10,pady=10)


#-----------------------wraper 2-------------------------
#funtion def\
t_1 =[]
t_2 =[]
t_3 =[]
t_4 =[]
t_5 =[]
t_6 =[]
t_7 =[]
t_8 =[]
t_9 =[]
t_10 =[]
class football:
    def __init__(self,team_1,score_1,point_1,team_2,score_2,point_2,GD1,GB1,GD2,GB2):
        self.team_1 = team_1
        self.score_1 = score_1
        self.point_1 = point_1
        self.GD1 = GD1 #ประตูที่ได้
        self.GB1 = GB1 #ประตูที่เสีย
        
        
        self.team_2 = team_2
        self.score_2 = score_2
        self.point_2 = point_2
        self.GD2 = GD2 #ประตูที่ได้
        self.GB2 = GB2 #ประตูที่เสีย

        
        #x = len(listteam)
        
        # 1vs2 
        if self.team_1 == listteam[0] and self.team_2 == listteam[1]:
            try:
                t_1.append(self.team_1 ) #nameteam
                t_1.append(int(self.score_1))        #score  
                t_1.append(int(self.point_1))        #point
                t_1.append(int(self.GD1))           #ประตูที่ได้ 
                t_1.append(int(self.GB1))   #ประตูที่เสีย
                t_1.append(1)
                t_2.append(self.team_2)   #nameteam
                t_2.append(int(self.score_2))        #score  
                t_2.append(int(self.point_2))        #point
                t_2.append(int(self.GD2))           #ประตูที่ได้ 
                t_2.append(int(self.GB2))   #ประตูที่เสีย
                t_2.append(1)

                print(t_1)
                print(t_2)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)

            # 1 vs3
        elif self.team_1 == listteam[0] and self.team_2 == listteam[2]:
            try:
                t_1.append(self.team_1 ) #nameteam
                t_1.append(int(self.score_1))        #score  
                t_1.append(int(self.point_1))        #point
                t_1.append(int(self.GD1))           #ประตูที่ได้ 
                t_1.append(int(self.GB1))   #ประตูที่เสีย
                t_1.append(1)
                t_3.append(self.team_2)   #nameteam
                t_3.append(int(self.score_2))        #score  
                t_3.append(int(self.point_2))        #point
                t_3.append(int(self.GD2))           #ประตูที่ได้ 
                t_3.append(int(self.GB2))   #ประตูที่เสีย
                t_3.append(1)

                print(t_1)
                print(t_3)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
            
            # 1 vs4
        elif self.team_1 == listteam[0] and self.team_2 == listteam[3]:
            try:
                t_1.append(self.team_1 ) #nameteam
                t_1.append(int(self.score_1))        #score  
                t_1.append(int(self.point_1))        #point
                t_1.append(int(self.GD1))           #ประตูที่ได้ 
                t_1.append(int(self.GB1))   #ประตูที่เสีย
                t_1.append(1)
                t_4.append(self.team_2)   #nameteam
                t_4.append(int(self.score_2))        #score  
                t_4.append(int(self.point_2))        #point
                t_4.append(int(self.GD2))           #ประตูที่ได้ 
                t_4.append(int(self.GB2))   #ประตูที่เสีย
                t_4.append(1)

                print(t_1)
                print(t_4)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
            
            # 1 vs5
        elif self.team_1 == listteam[0] and self.team_2 == listteam[4]:
            try:
                t_1.append(self.team_1 ) #nameteam
                t_1.append(int(self.score_1))        #score  
                t_1.append(int(self.point_1))        #point
                t_1.append(int(self.GD1))           #ประตูที่ได้ 
                t_1.append(int(self.GB1))   #ประตูที่เสีย
                t_1.append(1)
                t_5.append(self.team_2)   #nameteam
                t_5.append(int(self.score_2))        #score  
                t_5.append(int(self.point_2))        #point
                t_5.append(int(self.GD2))           #ประตูที่ได้ 
                t_5.append(int(self.GB2))   #ประตูที่เสีย
                t_5.append(1)

                print(t_1)
                print(t_5)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
            
            # 1 vs6
        elif self.team_1 == listteam[0] and self.team_2 == listteam[5]:
            try:
                t_1.append(self.team_1 ) #nameteam
                t_1.append(int(self.score_1))        #score  
                t_1.append(int(self.point_1))        #point
                t_1.append(int(self.GD1))           #ประตูที่ได้ 
                t_1.append(int(self.GB1))   #ประตูที่เสีย
                t_1.append(1)
                t_6.append(self.team_2)   #nameteam
                t_6.append(int(self.score_2))        #score  
                t_6.append(int(self.point_2))        #point
                t_6.append(int(self.GD2))           #ประตูที่ได้ 
                t_6.append(int(self.GB2))   #ประตูที่เสีย
                t_6.append(1)

                print(t_1)
                print(t_6)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
            
            # 1 vs7
        elif self.team_1 == listteam[0] and self.team_2 == listteam[6]:
            try:
                t_1.append(self.team_1 ) #nameteam
                t_1.append(int(self.score_1))        #score  
                t_1.append(int(self.point_1))        #point
                t_1.append(int(self.GD1))           #ประตูที่ได้ 
                t_1.append(int(self.GB1))   #ประตูที่เสีย
                t_1.append(1)
                t_7.append(self.team_2)   #nameteam
                t_7.append(int(self.score_2))        #score  
                t_7.append(int(self.point_2))        #point
                t_7.append(int(self.GD2))           #ประตูที่ได้ 
                t_7.append(int(self.GB2))   #ประตูที่เสีย
                t_7.append(1)

                print(t_1)
                print(t_7)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
            
            # 1 vs8
        elif self.team_1 == listteam[0] and self.team_2 == listteam[7]:
            try:
                t_1.append(self.team_1 ) #nameteam
                t_1.append(int(self.score_1))        #score  
                t_1.append(int(self.point_1))        #point
                t_1.append(int(self.GD1))           #ประตูที่ได้ 
                t_1.append(int(self.GB1))   #ประตูที่เสีย
                t_1.append(1)
                t_8.append(self.team_2)   #nameteam
                t_8.append(int(self.score_2))        #score  
                t_8.append(int(self.point_2))        #point
                t_8.append(int(self.GD2))           #ประตูที่ได้ 
                t_8.append(int(self.GB2))   #ประตูที่เสีย
                t_8.append(1)

                print(t_1)
                print(t_8)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
            
            # 1 vs9
        elif self.team_1 == listteam[0] and self.team_2 == listteam[8]:
            try:
                t_1.append(self.team_1 ) #nameteam
                t_1.append(int(self.score_1))        #score  
                t_1.append(int(self.point_1))        #point
                t_1.append(int(self.GD1))           #ประตูที่ได้ 
                t_1.append(int(self.GB1))   #ประตูที่เสีย
                t_1.append(1)
                t_9.append(self.team_2)   #nameteam
                t_9.append(int(self.score_2))        #score  
                t_9.append(int(self.point_2))        #point
                t_9.append(int(self.GD2))           #ประตูที่ได้ 
                t_9.append(int(self.GB2))   #ประตูที่เสีย
                t_9.append(1)

                print(t_1)
                print(t_9)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
            
            # 1vs 10
        elif self.team_1 == listteam[0] and self.team_2 == listteam[9]:
            try:
                t_1.append(self.team_1 ) #nameteam
                t_1.append(int(self.score_1))        #score  
                t_1.append(int(self.point_1))        #point
                t_1.append(int(self.GD1))           #ประตูที่ได้ 
                t_1.append(int(self.GB1))   #ประตูที่เสีย
                t_1.append(1)
                t_10.append(self.team_2)   #nameteam
                t_10.append(int(self.score_2))        #score  
                t_10.append(int(self.point_2))        #point
                t_10.append(int(self.GD2))           #ประตูที่ได้ 
                t_10.append(int(self.GB2))   #ประตูที่เสีย
                t_10.append(1)

                print(t_1)
                print(t_10)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
            #2vs1
        elif self.team_1 == listteam[1] and self.team_2 == listteam[0]:
            try:
                t_2.append(self.team_1 ) #nameteam
                t_2.append(int(self.score_1))        #score  
                t_2.append(int(self.point_1))        #point
                t_2.append(int(self.GD1))           #ประตูที่ได้ 
                t_2.append(int(self.GB1))   #ประตูที่เสีย
                t_2.append(1)
                t_1.append(self.team_2)   #nameteam
                t_1.append(int(self.score_2))        #score  
                t_1.append(int(self.point_2))        #point
                t_1.append(int(self.GD2))           #ประตูที่ได้ 
                t_1.append(int(self.GB2))   #ประตูที่เสีย
                t_1.append(1)

                print(t_2)
                print(t_1)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[1] and self.team_2 == listteam[2]:
            try:
                t_2.append(self.team_1 ) #nameteam
                t_2.append(int(self.score_1))        #score  
                t_2.append(int(self.point_1))        #point
                t_2.append(int(self.GD1))           #ประตูที่ได้ 
                t_2.append(int(self.GB1))   #ประตูที่เสีย
                t_2.append(1)
                t_3.append(self.team_2)   #nameteam
                t_3.append(int(self.score_2))        #score  
                t_3.append(int(self.point_2))        #point
                t_3.append(int(self.GD2))           #ประตูที่ได้ 
                t_3.append(int(self.GB2))   #ประตูที่เสีย
                t_3.append(1)

                print(t_2)
                print(t_3)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[1] and self.team_2 == listteam[3]:
            try:
                t_2.append(self.team_1 ) #nameteam
                t_2.append(int(self.score_1))        #score  
                t_2.append(int(self.point_1))        #point
                t_2.append(int(self.GD1))           #ประตูที่ได้ 
                t_2.append(int(self.GB1))   #ประตูที่เสีย
                t_2.append(1)
                t_4.append(self.team_2)   #nameteam
                t_4.append(int(self.score_2))        #score  
                t_4.append(int(self.point_2))        #point
                t_4.append(int(self.GD2))           #ประตูที่ได้ 
                t_4.append(int(self.GB2))   #ประตูที่เสีย
                t_4.append(1)

                print(t_2)
                print(t_4)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[1] and self.team_2 == listteam[4]:
            try:
                t_2.append(self.team_1 ) #nameteam
                t_2.append(int(self.score_1))        #score  
                t_2.append(int(self.point_1))        #point
                t_2.append(int(self.GD1))           #ประตูที่ได้ 
                t_2.append(int(self.GB1))   #ประตูที่เสีย
                t_2.append(1)
                t_5.append(self.team_2)   #nameteam
                t_5.append(int(self.score_2))        #score  
                t_5.append(int(self.point_2))        #point
                t_5.append(int(self.GD2))           #ประตูที่ได้ 
                t_5.append(int(self.GB2))   #ประตูที่เสีย
                t_5.append(1)

                print(t_2)
                print(t_5)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[1] and self.team_2 == listteam[5]:
            try:
                t_2.append(self.team_1 ) #nameteam
                t_2.append(int(self.score_1))        #score  
                t_2.append(int(self.point_1))        #point
                t_2.append(int(self.GD1))           #ประตูที่ได้ 
                t_2.append(int(self.GB1))   #ประตูที่เสีย
                t_2.append(1)
                t_6.append(self.team_2)   #nameteam
                t_6.append(int(self.score_2))        #score  
                t_6.append(int(self.point_2))        #point
                t_6.append(int(self.GD2))           #ประตูที่ได้ 
                t_6.append(int(self.GB2))   #ประตูที่เสีย
                t_6.append(1)

                print(t_2)
                print(t_6)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[1] and self.team_2 == listteam[6]:
            try:
                t_2.append(self.team_1 ) #nameteam
                t_2.append(int(self.score_1))        #score  
                t_2.append(int(self.point_1))        #point
                t_2.append(int(self.GD1))           #ประตูที่ได้ 
                t_2.append(int(self.GB1))   #ประตูที่เสีย
                t_2.append(1)
                t_7.append(self.team_2)   #nameteam
                t_7.append(int(self.score_2))        #score  
                t_7.append(int(self.point_2))        #point
                t_7.append(int(self.GD2))           #ประตูที่ได้ 
                t_7.append(int(self.GB2))   #ประตูที่เสีย
                t_7.append(1)

                print(t_2)
                print(t_7)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[1] and self.team_2 == listteam[7]:
            try:
                t_2.append(self.team_1 ) #nameteam
                t_2.append(int(self.score_1))        #score  
                t_2.append(int(self.point_1))        #point
                t_2.append(int(self.GD1))           #ประตูที่ได้ 
                t_2.append(int(self.GB1))   #ประตูที่เสีย
                t_2.append(1)
                t_8.append(self.team_2)   #nameteam
                t_8.append(int(self.score_2))        #score  
                t_8.append(int(self.point_2))        #point
                t_8.append(int(self.GD2))           #ประตูที่ได้ 
                t_8.append(int(self.GB2))   #ประตูที่เสีย
                t_8.append(1)

                print(t_2)
                print(t_8)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[1] and self.team_2 == listteam[8]:
            try:
                t_2.append(self.team_1 ) #nameteam
                t_2.append(int(self.score_1))        #score  
                t_2.append(int(self.point_1))        #point
                t_2.append(int(self.GD1))           #ประตูที่ได้ 
                t_2.append(int(self.GB1))   #ประตูที่เสีย
                t_2.append(1)
                t_9.append(self.team_2)   #nameteam
                t_9.append(int(self.score_2))        #score  
                t_9.append(int(self.point_2))        #point
                t_9.append(int(self.GD2))           #ประตูที่ได้ 
                t_9.append(int(self.GB2))   #ประตูที่เสีย
                t_9.append(1)

                print(t_2)
                print(t_9)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[1] and self.team_2 == listteam[9]:
            try:
                t_2.append(self.team_1 ) #nameteam
                t_2.append(int(self.score_1))        #score  
                t_2.append(int(self.point_1))        #point
                t_2.append(int(self.GD1))           #ประตูที่ได้ 
                t_2.append(int(self.GB1))   #ประตูที่เสีย
                t_2.append(1)
                t_10.append(self.team_2)   #nameteam
                t_10.append(int(self.score_2))        #score  
                t_10.append(int(self.point_2))        #point
                t_10.append(int(self.GD2))           #ประตูที่ได้ 
                t_10.append(int(self.GB2))   #ประตูที่เสีย
                t_10.append(1)

                print(t_2)
                print(t_10)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[2] and self.team_2 == listteam[0]:
            try:
                t_3.append(self.team_1 ) #nameteam
                t_3.append(int(self.score_1))        #score  
                t_3.append(int(self.point_1))        #point
                t_3.append(int(self.GD1))           #ประตูที่ได้ 
                t_3.append(int(self.GB1))   #ประตูที่เสีย
                t_3.append(1)
                t_1.append(self.team_2)   #nameteam
                t_1.append(int(self.score_2))        #score  
                t_1.append(int(self.point_2))        #point
                t_1.append(int(self.GD2))           #ประตูที่ได้ 
                t_1.append(int(self.GB2))   #ประตูที่เสีย
                t_1.append(1)

                print(t_3)
                print(t_1)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[2] and self.team_2 == listteam[1]:
            try:
                t_3.append(self.team_1 ) #nameteam
                t_3.append(int(self.score_1))        #score  
                t_3.append(int(self.point_1))        #point
                t_3.append(int(self.GD1))           #ประตูที่ได้ 
                t_3.append(int(self.GB1))   #ประตูที่เสีย
                t_3.append(1)
                t_2.append(self.team_2)   #nameteam
                t_2.append(int(self.score_2))        #score  
                t_2.append(int(self.point_2))        #point
                t_2.append(int(self.GD2))           #ประตูที่ได้ 
                t_2.append(int(self.GB2))   #ประตูที่เสีย
                t_2.append(1)

                print(t_3)
                print(t_2)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[2] and self.team_2 == listteam[3]:
            try:
                t_3.append(self.team_1 ) #nameteam
                t_3.append(int(self.score_1))        #score  
                t_3.append(int(self.point_1))        #point
                t_3.append(int(self.GD1))           #ประตูที่ได้ 
                t_3.append(int(self.GB1))   #ประตูที่เสีย
                t_3.append(1)
                t_4.append(self.team_2)   #nameteam
                t_4.append(int(self.score_2))        #score  
                t_4.append(int(self.point_2))        #point
                t_4.append(int(self.GD2))           #ประตูที่ได้ 
                t_4.append(int(self.GB2))   #ประตูที่เสีย
                t_4.append(1)

                print(t_3)
                print(t_4)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[2] and self.team_2 == listteam[4]:
            try:
                t_3.append(self.team_1 ) #nameteam
                t_3.append(int(self.score_1))        #score  
                t_3.append(int(self.point_1))        #point
                t_3.append(int(self.GD1))           #ประตูที่ได้ 
                t_3.append(int(self.GB1))   #ประตูที่เสีย
                t_3.append(1)
                t_5.append(self.team_2)   #nameteam
                t_5.append(int(self.score_2))        #score  
                t_5.append(int(self.point_2))        #point
                t_5.append(int(self.GD2))           #ประตูที่ได้ 
                t_5.append(int(self.GB2))   #ประตูที่เสีย
                t_5.append(1)

                print(t_3)
                print(t_5)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[2] and self.team_2 == listteam[5]:
            try:
                t_3.append(self.team_1 ) #nameteam
                t_3.append(int(self.score_1))        #score  
                t_3.append(int(self.point_1))        #point
                t_3.append(int(self.GD1))           #ประตูที่ได้ 
                t_3.append(int(self.GB1))   #ประตูที่เสีย
                t_3.append(1)
                t_6.append(self.team_2)   #nameteam
                t_6.append(int(self.score_2))        #score  
                t_6.append(int(self.point_2))        #point
                t_6.append(int(self.GD2))           #ประตูที่ได้ 
                t_6.append(int(self.GB2))   #ประตูที่เสีย
                t_6.append(1)

                print(t_3)
                print(t_6)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[2] and self.team_2 == listteam[6]:
            try:
                t_3.append(self.team_1 ) #nameteam
                t_3.append(int(self.score_1))        #score  
                t_3.append(int(self.point_1))        #point
                t_3.append(int(self.GD1))           #ประตูที่ได้ 
                t_3.append(int(self.GB1))   #ประตูที่เสีย
                t_3.append(1)
                t_7.append(self.team_2)   #nameteam
                t_7.append(int(self.score_2))        #score  
                t_7.append(int(self.point_2))        #point
                t_7.append(int(self.GD2))           #ประตูที่ได้ 
                t_7.append(int(self.GB2))   #ประตูที่เสีย
                t_7.append(1)

                print(t_3)
                print(t_7)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[2] and self.team_2 == listteam[7]:
            try:
                t_3.append(self.team_1 ) #nameteam
                t_3.append(int(self.score_1))        #score  
                t_3.append(int(self.point_1))        #point
                t_3.append(int(self.GD1))           #ประตูที่ได้ 
                t_3.append(int(self.GB1))   #ประตูที่เสีย
                t_3.append(1)
                t_8.append(self.team_2)   #nameteam
                t_8.append(int(self.score_2))        #score  
                t_8.append(int(self.point_2))        #point
                t_8.append(int(self.GD2))           #ประตูที่ได้ 
                t_8.append(int(self.GB2))   #ประตูที่เสีย
                t_8.append(1)

                print(t_3)
                print(t_8)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[2] and self.team_2 == listteam[8]:
            try:
                t_3.append(self.team_1 ) #nameteam
                t_3.append(int(self.score_1))        #score  
                t_3.append(int(self.point_1))        #point
                t_3.append(int(self.GD1))           #ประตูที่ได้ 
                t_3.append(int(self.GB1))   #ประตูที่เสีย
                t_3.append(1)
                t_9.append(self.team_2)   #nameteam
                t_9.append(int(self.score_2))        #score  
                t_9.append(int(self.point_2))        #point
                t_9.append(int(self.GD2))           #ประตูที่ได้ 
                t_9.append(int(self.GB2))   #ประตูที่เสีย
                t_9.append(1)

                print(t_3)
                print(t_9)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[2] and self.team_2 == listteam[9]:
            try:
                t_3.append(self.team_1 ) #nameteam
                t_3.append(int(self.score_1))        #score  
                t_3.append(int(self.point_1))        #point
                t_3.append(int(self.GD1))           #ประตูที่ได้ 
                t_3.append(int(self.GB1))   #ประตูที่เสีย
                t_3.append(1)
                t_10.append(self.team_2)   #nameteam
                t_10.append(int(self.score_2))        #score  
                t_10.append(int(self.point_2))        #point
                t_10.append(int(self.GD2))           #ประตูที่ได้ 
                t_10.append(int(self.GB2))   #ประตูที่เสีย
                t_10.append(1)

                print(t_3)
                print(t_10)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[3] and self.team_2 == listteam[0]:
            try:
                t_4.append(self.team_1 ) #nameteam
                t_4.append(int(self.score_1))        #score  
                t_4.append(int(self.point_1))        #point
                t_4.append(int(self.GD1))           #ประตูที่ได้ 
                t_4.append(int(self.GB1))   #ประตูที่เสีย
                t_4.append(1)
                t_1.append(self.team_2)   #nameteam
                t_1.append(int(self.score_2))        #score  
                t_1.append(int(self.point_2))        #point
                t_1.append(int(self.GD2))           #ประตูที่ได้ 
                t_1.append(int(self.GB2))   #ประตูที่เสีย
                t_1.append(1)

                print(t_4)
                print(t_1)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[3] and self.team_2 == listteam[1]:
            try:
                t_4.append(self.team_1 ) #nameteam
                t_4.append(int(self.score_1))        #score  
                t_4.append(int(self.point_1))        #point
                t_4.append(int(self.GD1))           #ประตูที่ได้ 
                t_4.append(int(self.GB1))   #ประตูที่เสีย
                t_4.append(1)
                t_2.append(self.team_2)   #nameteam
                t_2.append(int(self.score_2))        #score  
                t_2.append(int(self.point_2))        #point
                t_2.append(int(self.GD2))           #ประตูที่ได้ 
                t_2.append(int(self.GB2))   #ประตูที่เสีย
                t_2.append(1)

                print(t_4)
                print(t_2)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[3] and self.team_2 == listteam[2]:
            try:
                t_4.append(self.team_1 ) #nameteam
                t_4.append(int(self.score_1))        #score  
                t_4.append(int(self.point_1))        #point
                t_4.append(int(self.GD1))           #ประตูที่ได้ 
                t_4.append(int(self.GB1))   #ประตูที่เสีย
                t_4.append(1)
                t_3.append(self.team_2)   #nameteam
                t_3.append(int(self.score_2))        #score  
                t_3.append(int(self.point_2))        #point
                t_3.append(int(self.GD2))           #ประตูที่ได้ 
                t_3.append(int(self.GB2))   #ประตูที่เสีย
                t_3.append(1)

                print(t_4)
                print(t_3)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[3] and self.team_2 == listteam[4]:
            try:
                t_4.append(self.team_1 ) #nameteam
                t_4.append(int(self.score_1))        #score  
                t_4.append(int(self.point_1))        #point
                t_4.append(int(self.GD1))           #ประตูที่ได้ 
                t_4.append(int(self.GB1))   #ประตูที่เสีย
                t_4.append(1)
                t_5.append(self.team_2)   #nameteam
                t_5.append(int(self.score_2))        #score  
                t_5.append(int(self.point_2))        #point
                t_5.append(int(self.GD2))           #ประตูที่ได้ 
                t_5.append(int(self.GB2))   #ประตูที่เสีย
                t_5.append(1)

                print(t_4)
                print(t_5)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[3] and self.team_2 == listteam[5]:
            try:
                t_4.append(self.team_1 ) #nameteam
                t_4.append(int(self.score_1))        #score  
                t_4.append(int(self.point_1))        #point
                t_4.append(int(self.GD1))           #ประตูที่ได้ 
                t_4.append(int(self.GB1))   #ประตูที่เสีย
                t_4.append(1)
                t_6.append(self.team_2)   #nameteam
                t_6.append(int(self.score_2))        #score  
                t_6.append(int(self.point_2))        #point
                t_6.append(int(self.GD2))           #ประตูที่ได้ 
                t_6.append(int(self.GB2))   #ประตูที่เสีย
                t_6.append(1)

                print(t_4)
                print(t_6)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[3] and self.team_2 == listteam[6]:
            try:
                t_4.append(self.team_1 ) #nameteam
                t_4.append(int(self.score_1))        #score  
                t_4.append(int(self.point_1))        #point
                t_4.append(int(self.GD1))           #ประตูที่ได้ 
                t_4.append(int(self.GB1))   #ประตูที่เสีย
                t_4.append(1)
                t_7.append(self.team_2)   #nameteam
                t_7.append(int(self.score_2))        #score  
                t_7.append(int(self.point_2))        #point
                t_7.append(int(self.GD2))           #ประตูที่ได้ 
                t_7.append(int(self.GB2))   #ประตูที่เสีย
                t_7.append(1)

                print(t_4)
                print(t_7)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[3] and self.team_2 == listteam[7]:
            try:
                t_4.append(self.team_1 ) #nameteam
                t_4.append(int(self.score_1))        #score  
                t_4.append(int(self.point_1))        #point
                t_4.append(int(self.GD1))           #ประตูที่ได้ 
                t_4.append(int(self.GB1))   #ประตูที่เสีย
                t_4.append(1)
                t_8.append(self.team_2)   #nameteam
                t_8.append(int(self.score_2))        #score  
                t_8.append(int(self.point_2))        #point
                t_8.append(int(self.GD2))           #ประตูที่ได้ 
                t_8.append(int(self.GB2))   #ประตูที่เสีย
                t_8.append(1)

                print(t_4)
                print(t_8)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[3] and self.team_2 == listteam[8]:
            try:
                t_4.append(self.team_1 ) #nameteam
                t_4.append(int(self.score_1))        #score  
                t_4.append(int(self.point_1))        #point
                t_4.append(int(self.GD1))           #ประตูที่ได้ 
                t_4.append(int(self.GB1))   #ประตูที่เสีย
                t_4.append(1)
                t_9.append(self.team_2)   #nameteam
                t_9.append(int(self.score_2))        #score  
                t_9.append(int(self.point_2))        #point
                t_9.append(int(self.GD2))           #ประตูที่ได้ 
                t_9.append(int(self.GB2))   #ประตูที่เสีย
                t_9.append(1)

                print(t_4)
                print(t_9)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[3] and self.team_2 == listteam[9]:
            try:
                t_4.append(self.team_1 ) #nameteam
                t_4.append(int(self.score_1))        #score  
                t_4.append(int(self.point_1))        #point
                t_4.append(int(self.GD1))           #ประตูที่ได้ 
                t_4.append(int(self.GB1))   #ประตูที่เสีย
                t_4.append(1)
                t_10.append(self.team_2)   #nameteam
                t_10.append(int(self.score_2))        #score  
                t_10.append(int(self.point_2))        #point
                t_10.append(int(self.GD2))           #ประตูที่ได้ 
                t_10.append(int(self.GB2))   #ประตูที่เสีย
                t_10.append(1)

                print(t_4)
                print(t_10)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[4] and self.team_2 == listteam[0]:
            try:
                t_5.append(self.team_1 ) #nameteam
                t_5.append(int(self.score_1))        #score  
                t_5.append(int(self.point_1))        #point
                t_5.append(int(self.GD1))           #ประตูที่ได้ 
                t_5.append(int(self.GB1))   #ประตูที่เสีย
                t_5.append(1)
                t_1.append(self.team_2)   #nameteam
                t_1.append(int(self.score_2))        #score  
                t_1.append(int(self.point_2))        #point
                t_1.append(int(self.GD2))           #ประตูที่ได้ 
                t_1.append(int(self.GB2))   #ประตูที่เสีย
                t_1.append(1)

                print(t_5)
                print(t_1)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[4] and self.team_2 == listteam[1]:
            try:
                t_5.append(self.team_1 ) #nameteam
                t_5.append(int(self.score_1))        #score  
                t_5.append(int(self.point_1))        #point
                t_5.append(int(self.GD1))           #ประตูที่ได้ 
                t_5.append(int(self.GB1))   #ประตูที่เสีย
                t_5.append(1)
                t_2.append(self.team_2)   #nameteam
                t_2.append(int(self.score_2))        #score  
                t_2.append(int(self.point_2))        #point
                t_2.append(int(self.GD2))           #ประตูที่ได้ 
                t_2.append(int(self.GB2))   #ประตูที่เสีย
                t_2.append(1)

                print(t_5)
                print(t_2)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[4] and self.team_2 == listteam[2]:
            try:
                t_5.append(self.team_1 ) #nameteam
                t_5.append(int(self.score_1))        #score  
                t_5.append(int(self.point_1))        #point
                t_5.append(int(self.GD1))           #ประตูที่ได้ 
                t_5.append(int(self.GB1))   #ประตูที่เสีย
                t_5.append(1)
                t_3.append(self.team_2)   #nameteam
                t_3.append(int(self.score_2))        #score  
                t_3.append(int(self.point_2))        #point
                t_3.append(int(self.GD2))           #ประตูที่ได้ 
                t_3.append(int(self.GB2))   #ประตูที่เสีย
                t_3.append(1)

                print(t_5)
                print(t_3)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[4] and self.team_2 == listteam[3]:
            try:
                t_5.append(self.team_1 ) #nameteam
                t_5.append(int(self.score_1))        #score  
                t_5.append(int(self.point_1))        #point
                t_5.append(int(self.GD1))           #ประตูที่ได้ 
                t_5.append(int(self.GB1))   #ประตูที่เสีย
                t_5.append(1)
                t_4.append(self.team_2)   #nameteam
                t_4.append(int(self.score_2))        #score  
                t_4.append(int(self.point_2))        #point
                t_4.append(int(self.GD2))           #ประตูที่ได้ 
                t_4.append(int(self.GB2))   #ประตูที่เสีย
                t_4.append(1)

                print(t_5)
                print(t_4)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[4] and self.team_2 == listteam[5]:
            try:
                t_5.append(self.team_1 ) #nameteam
                t_5.append(int(self.score_1))        #score  
                t_5.append(int(self.point_1))        #point
                t_5.append(int(self.GD1))           #ประตูที่ได้ 
                t_5.append(int(self.GB1))   #ประตูที่เสีย
                t_5.append(1)
                t_6.append(self.team_2)   #nameteam
                t_6.append(int(self.score_2))        #score  
                t_6.append(int(self.point_2))        #point
                t_6.append(int(self.GD2))           #ประตูที่ได้ 
                t_6.append(int(self.GB2))   #ประตูที่เสีย
                t_6.append(1)

                print(t_5)
                print(t_6)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[4] and self.team_2 == listteam[6]:
            try:
                t_5.append(self.team_1 ) #nameteam
                t_5.append(int(self.score_1))        #score  
                t_5.append(int(self.point_1))        #point
                t_5.append(int(self.GD1))           #ประตูที่ได้ 
                t_5.append(int(self.GB1))   #ประตูที่เสีย
                t_5.append(1)
                t_7.append(self.team_2)   #nameteam
                t_7.append(int(self.score_2))        #score  
                t_7.append(int(self.point_2))        #point
                t_7.append(int(self.GD2))           #ประตูที่ได้ 
                t_7.append(int(self.GB2))   #ประตูที่เสีย
                t_7.append(1)

                print(t_5)
                print(t_7)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[4] and self.team_2 == listteam[7]:
            try:
                t_5.append(self.team_1 ) #nameteam
                t_5.append(int(self.score_1))        #score  
                t_5.append(int(self.point_1))        #point
                t_5.append(int(self.GD1))           #ประตูที่ได้ 
                t_5.append(int(self.GB1))   #ประตูที่เสีย
                t_5.append(1)
                t_8.append(self.team_2)   #nameteam
                t_8.append(int(self.score_2))        #score  
                t_8.append(int(self.point_2))        #point
                t_8.append(int(self.GD2))           #ประตูที่ได้ 
                t_8.append(int(self.GB2))   #ประตูที่เสีย
                t_8.append(1)

                print(t_5)
                print(t_8)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[4] and self.team_2 == listteam[8]:
            try:
                t_5.append(self.team_1 ) #nameteam
                t_5.append(int(self.score_1))        #score  
                t_5.append(int(self.point_1))        #point
                t_5.append(int(self.GD1))           #ประตูที่ได้ 
                t_5.append(int(self.GB1))   #ประตูที่เสีย
                t_5.append(1)
                t_9.append(self.team_2)   #nameteam
                t_9.append(int(self.score_2))        #score  
                t_9.append(int(self.point_2))        #point
                t_9.append(int(self.GD2))           #ประตูที่ได้ 
                t_9.append(int(self.GB2))   #ประตูที่เสีย
                t_9.append(1)

                print(t_5)
                print(t_9)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[4] and self.team_2 == listteam[9]:
            try:
                t_5.append(self.team_1 ) #nameteam
                t_5.append(int(self.score_1))        #score  
                t_5.append(int(self.point_1))        #point
                t_5.append(int(self.GD1))           #ประตูที่ได้ 
                t_5.append(int(self.GB1))   #ประตูที่เสีย
                t_5.append(1)
                t_10.append(self.team_2)   #nameteam
                t_10.append(int(self.score_2))        #score  
                t_10.append(int(self.point_2))        #point
                t_10.append(int(self.GD2))           #ประตูที่ได้ 
                t_10.append(int(self.GB2))   #ประตูที่เสีย
                t_10.append(1)

                print(t_5)
                print(t_10)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[5] and self.team_2 == listteam[0]:
            try:
                t_6.append(self.team_1 ) #nameteam
                t_6.append(int(self.score_1))        #score  
                t_6.append(int(self.point_1))        #point
                t_6.append(int(self.GD1))           #ประตูที่ได้ 
                t_6.append(int(self.GB1))   #ประตูที่เสีย
                t_6.append(1)
                t_1.append(self.team_2)   #nameteam
                t_1.append(int(self.score_2))        #score  
                t_1.append(int(self.point_2))        #point
                t_1.append(int(self.GD2))           #ประตูที่ได้ 
                t_1.append(int(self.GB2))   #ประตูที่เสีย
                t_1.append(1)

                print(t_6)
                print(t_1)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[5] and self.team_2 == listteam[1]:
            try:
                t_6.append(self.team_1 ) #nameteam
                t_6.append(int(self.score_1))        #score  
                t_6.append(int(self.point_1))        #point
                t_6.append(int(self.GD1))           #ประตูที่ได้ 
                t_6.append(int(self.GB1))   #ประตูที่เสีย
                t_6.append(1)
                t_2.append(self.team_2)   #nameteam
                t_2.append(int(self.score_2))        #score  
                t_2.append(int(self.point_2))        #point
                t_2.append(int(self.GD2))           #ประตูที่ได้ 
                t_2.append(int(self.GB2))   #ประตูที่เสีย
                t_2.append(1)

                print(t_6)
                print(t_2)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[5] and self.team_2 == listteam[2]:
            try:
                t_6.append(self.team_1 ) #nameteam
                t_6.append(int(self.score_1))        #score  
                t_6.append(int(self.point_1))        #point
                t_6.append(int(self.GD1))           #ประตูที่ได้ 
                t_6.append(int(self.GB1))   #ประตูที่เสีย
                t_6.append(1)
                t_3.append(self.team_2)   #nameteam
                t_3.append(int(self.score_2))        #score  
                t_3.append(int(self.point_2))        #point
                t_3.append(int(self.GD2))           #ประตูที่ได้ 
                t_3.append(int(self.GB2))   #ประตูที่เสีย
                t_3.append(1)

                print(t_6)
                print(t_3)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[5] and self.team_2 == listteam[3]:
            try:
                t_6.append(self.team_1 ) #nameteam
                t_6.append(int(self.score_1))        #score  
                t_6.append(int(self.point_1))        #point
                t_6.append(int(self.GD1))           #ประตูที่ได้ 
                t_6.append(int(self.GB1))   #ประตูที่เสีย
                t_6.append(1)
                t_4.append(self.team_2)   #nameteam
                t_4.append(int(self.score_2))        #score  
                t_4.append(int(self.point_2))        #point
                t_4.append(int(self.GD2))           #ประตูที่ได้ 
                t_4.append(int(self.GB2))   #ประตูที่เสีย
                t_4.append(1)

                print(t_6)
                print(t_4)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[5] and self.team_2 == listteam[4]:
            try:
                t_6.append(self.team_1 ) #nameteam
                t_6.append(int(self.score_1))        #score  
                t_6.append(int(self.point_1))        #point
                t_6.append(int(self.GD1))           #ประตูที่ได้ 
                t_6.append(int(self.GB1))   #ประตูที่เสีย
                t_6.append(1)
                t_5.append(self.team_2)   #nameteam
                t_5.append(int(self.score_2))        #score  
                t_5.append(int(self.point_2))        #point
                t_5.append(int(self.GD2))           #ประตูที่ได้ 
                t_5.append(int(self.GB2))   #ประตูที่เสีย
                t_5.append(1)

                print(t_6)
                print(t_5)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[5] and self.team_2 == listteam[6]:
            try:
                t_6.append(self.team_1 ) #nameteam
                t_6.append(int(self.score_1))        #score  
                t_6.append(int(self.point_1))        #point
                t_6.append(int(self.GD1))           #ประตูที่ได้ 
                t_6.append(int(self.GB1))   #ประตูที่เสีย
                t_6.append(1)
                t_7.append(self.team_2)   #nameteam
                t_7.append(int(self.score_2))        #score  
                t_7.append(int(self.point_2))        #point
                t_7.append(int(self.GD2))           #ประตูที่ได้ 
                t_7.append(int(self.GB2))   #ประตูที่เสีย
                t_7.append(1)

                print(t_6)
                print(t_7)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[5] and self.team_2 == listteam[7]:
            try:
                t_6.append(self.team_1 ) #nameteam
                t_6.append(int(self.score_1))        #score  
                t_6.append(int(self.point_1))        #point
                t_6.append(int(self.GD1))           #ประตูที่ได้ 
                t_6.append(int(self.GB1))   #ประตูที่เสีย
                t_6.append(1)
                t_8.append(self.team_2)   #nameteam
                t_8.append(int(self.score_2))        #score  
                t_8.append(int(self.point_2))        #point
                t_8.append(int(self.GD2))           #ประตูที่ได้ 
                t_8.append(int(self.GB2))   #ประตูที่เสีย
                t_8.append(1)

                print(t_6)
                print(t_8)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[5] and self.team_2 == listteam[8]:
            try:
                t_6.append(self.team_1 ) #nameteam
                t_6.append(int(self.score_1))        #score  
                t_6.append(int(self.point_1))        #point
                t_6.append(int(self.GD1))           #ประตูที่ได้ 
                t_6.append(int(self.GB1))   #ประตูที่เสีย
                t_6.append(1)
                t_9.append(self.team_2)   #nameteam
                t_9.append(int(self.score_2))        #score  
                t_9.append(int(self.point_2))        #point
                t_9.append(int(self.GD2))           #ประตูที่ได้ 
                t_9.append(int(self.GB2))   #ประตูที่เสีย
                t_9.append(1)

                print(t_6)
                print(t_9)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[5] and self.team_2 == listteam[9]:
            try:
                t_6.append(self.team_1 ) #nameteam
                t_6.append(int(self.score_1))        #score  
                t_6.append(int(self.point_1))        #point
                t_6.append(int(self.GD1))           #ประตูที่ได้ 
                t_6.append(int(self.GB1))   #ประตูที่เสีย
                t_6.append(1)
                t_10.append(self.team_2)   #nameteam
                t_10.append(int(self.score_2))        #score  
                t_10.append(int(self.point_2))        #point
                t_10.append(int(self.GD2))           #ประตูที่ได้ 
                t_10.append(int(self.GB2))   #ประตูที่เสีย
                t_10.append(1)

                print(t_6)
                print(t_10)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[6] and self.team_2 == listteam[0]:
            try:
                t_7.append(self.team_1 ) #nameteam
                t_7.append(int(self.score_1))        #score  
                t_7.append(int(self.point_1))        #point
                t_7.append(int(self.GD1))           #ประตูที่ได้ 
                t_7.append(int(self.GB1))   #ประตูที่เสีย
                t_7.append(1)
                t_1.append(self.team_2)   #nameteam
                t_1.append(int(self.score_2))        #score  
                t_1.append(int(self.point_2))        #point
                t_1.append(int(self.GD2))           #ประตูที่ได้ 
                t_1.append(int(self.GB2))   #ประตูที่เสีย
                t_1.append(1)

                print(t_7)
                print(t_1)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[6] and self.team_2 == listteam[1]:
            try:
                t_7.append(self.team_1 ) #nameteam
                t_7.append(int(self.score_1))        #score  
                t_7.append(int(self.point_1))        #point
                t_7.append(int(self.GD1))           #ประตูที่ได้ 
                t_7.append(int(self.GB1))   #ประตูที่เสีย
                t_7.append(1)
                t_2.append(self.team_2)   #nameteam
                t_2.append(int(self.score_2))        #score  
                t_2.append(int(self.point_2))        #point
                t_2.append(int(self.GD2))           #ประตูที่ได้ 
                t_2.append(int(self.GB2))   #ประตูที่เสีย
                t_2.append(1)

                print(t_7)
                print(t_2)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[6] and self.team_2 == listteam[2]:
            try:
                t_7.append(self.team_1 ) #nameteam
                t_7.append(int(self.score_1))        #score  
                t_7.append(int(self.point_1))        #point
                t_7.append(int(self.GD1))           #ประตูที่ได้ 
                t_7.append(int(self.GB1))   #ประตูที่เสีย
                t_7.append(1)
                t_3.append(self.team_2)   #nameteam
                t_3.append(int(self.score_2))        #score  
                t_3.append(int(self.point_2))        #point
                t_3.append(int(self.GD2))           #ประตูที่ได้ 
                t_3.append(int(self.GB2))   #ประตูที่เสีย
                t_3.append(1)

                print(t_7)
                print(t_3)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[6] and self.team_2 == listteam[3]:
            try:
                t_7.append(self.team_1 ) #nameteam
                t_7.append(int(self.score_1))        #score  
                t_7.append(int(self.point_1))        #point
                t_7.append(int(self.GD1))           #ประตูที่ได้ 
                t_7.append(int(self.GB1))   #ประตูที่เสีย
                t_7.append(1)
                t_4.append(self.team_2)   #nameteam
                t_4.append(int(self.score_2))        #score  
                t_4.append(int(self.point_2))        #point
                t_4.append(int(self.GD2))           #ประตูที่ได้ 
                t_4.append(int(self.GB2))   #ประตูที่เสีย
                t_4.append(1)

                print(t_7)
                print(t_4)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[6] and self.team_2 == listteam[4]:
            try:
                t_7.append(self.team_1 ) #nameteam
                t_7.append(int(self.score_1))        #score  
                t_7.append(int(self.point_1))        #point
                t_7.append(int(self.GD1))           #ประตูที่ได้ 
                t_7.append(int(self.GB1))   #ประตูที่เสีย
                t_7.append(1)
                t_5.append(self.team_2)   #nameteam
                t_5.append(int(self.score_2))        #score  
                t_5.append(int(self.point_2))        #point
                t_5.append(int(self.GD2))           #ประตูที่ได้ 
                t_5.append(int(self.GB2))   #ประตูที่เสีย
                t_5.append(1)

                print(t_7)
                print(t_5)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[6] and self.team_2 == listteam[5]:
            try:
                t_7.append(self.team_1 ) #nameteam
                t_7.append(int(self.score_1))        #score  
                t_7.append(int(self.point_1))        #point
                t_7.append(int(self.GD1))           #ประตูที่ได้ 
                t_7.append(int(self.GB1))   #ประตูที่เสีย
                t_7.append(1)
                t_6.append(self.team_2)   #nameteam
                t_6.append(int(self.score_2))        #score  
                t_6.append(int(self.point_2))        #point
                t_6.append(int(self.GD2))           #ประตูที่ได้ 
                t_6.append(int(self.GB2))   #ประตูที่เสีย
                t_6.append(1)

                print(t_7)
                print(t_6)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[6] and self.team_2 == listteam[7]:
            try:
                t_7.append(self.team_1 ) #nameteam
                t_7.append(int(self.score_1))        #score  
                t_7.append(int(self.point_1))        #point
                t_7.append(int(self.GD1))           #ประตูที่ได้ 
                t_7.append(int(self.GB1))   #ประตูที่เสีย
                t_7.append(1)
                t_8.append(self.team_2)   #nameteam
                t_8.append(int(self.score_2))        #score  
                t_8.append(int(self.point_2))        #point
                t_8.append(int(self.GD2))           #ประตูที่ได้ 
                t_8.append(int(self.GB2))   #ประตูที่เสีย
                t_8.append(1)

                print(t_7)
                print(t_8)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[6] and self.team_2 == listteam[8]:
            try:
                t_7.append(self.team_1 ) #nameteam
                t_7.append(int(self.score_1))        #score  
                t_7.append(int(self.point_1))        #point
                t_7.append(int(self.GD1))           #ประตูที่ได้ 
                t_7.append(int(self.GB1))   #ประตูที่เสีย
                t_7.append(1)
                t_1.append(self.team_2)   #nameteam
                t_9.append(int(self.score_2))        #score  
                t_9.append(int(self.point_2))        #point
                t_9.append(int(self.GD2))           #ประตูที่ได้ 
                t_9.append(int(self.GB2))   #ประตูที่เสีย
                t_9.append(1)

                print(t_7)
                print(t_9)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[6] and self.team_2 == listteam[9]:
            try:
                t_7.append(self.team_1 ) #nameteam
                t_7.append(int(self.score_1))        #score  
                t_7.append(int(self.point_1))        #point
                t_7.append(int(self.GD1))           #ประตูที่ได้ 
                t_7.append(int(self.GB1))   #ประตูที่เสีย
                t_7.append(1)
                t_10.append(self.team_2)   #nameteam
                t_10.append(int(self.score_2))        #score  
                t_10.append(int(self.point_2))        #point
                t_10.append(int(self.GD2))           #ประตูที่ได้ 
                t_10.append(int(self.GB2))   #ประตูที่เสีย
                t_10.append(1)

                print(t_7)
                print(t_10)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[7] and self.team_2 == listteam[0]:
            try:
                t_8.append(self.team_1 ) #nameteam
                t_8.append(int(self.score_1))        #score  
                t_8.append(int(self.point_1))        #point
                t_8.append(int(self.GD1))           #ประตูที่ได้ 
                t_8.append(int(self.GB1))   #ประตูที่เสีย
                t_8.append(1)
                t_1.append(self.team_2)   #nameteam
                t_1.append(int(self.score_2))        #score  
                t_1.append(int(self.point_2))        #point
                t_1.append(int(self.GD2))           #ประตูที่ได้ 
                t_1.append(int(self.GB2))   #ประตูที่เสีย
                t_1.append(1)

                print(t_8)
                print(t_1)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[7] and self.team_2 == listteam[1]:
            try:
                t_8.append(self.team_1 ) #nameteam
                t_8.append(int(self.score_1))        #score  
                t_8.append(int(self.point_1))        #point
                t_8.append(int(self.GD1))           #ประตูที่ได้ 
                t_8.append(int(self.GB1))   #ประตูที่เสีย
                t_8.append(1)
                t_2.append(self.team_2)   #nameteam
                t_2.append(int(self.score_2))        #score  
                t_2.append(int(self.point_2))        #point
                t_2.append(int(self.GD2))           #ประตูที่ได้ 
                t_2.append(int(self.GB2))   #ประตูที่เสีย
                t_2.append(1)

                print(t_8)
                print(t_2)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[7] and self.team_2 == listteam[2]:
            try:
                t_8.append(self.team_1 ) #nameteam
                t_8.append(int(self.score_1))        #score  
                t_8.append(int(self.point_1))        #point
                t_8.append(int(self.GD1))           #ประตูที่ได้ 
                t_8.append(int(self.GB1))   #ประตูที่เสีย
                t_8.append(1)
                t_3.append(self.team_2)   #nameteam
                t_3.append(int(self.score_2))        #score  
                t_3.append(int(self.point_2))        #point
                t_3.append(int(self.GD2))           #ประตูที่ได้ 
                t_3.append(int(self.GB2))   #ประตูที่เสีย
                t_3.append(1)

                print(t_8)
                print(t_3)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[7] and self.team_2 == listteam[3]:
            try:
                t_8.append(self.team_1 ) #nameteam
                t_8.append(int(self.score_1))        #score  
                t_8.append(int(self.point_1))        #point
                t_8.append(int(self.GD1))           #ประตูที่ได้ 
                t_8.append(int(self.GB1))   #ประตูที่เสีย
                t_8.append(1)
                t_4.append(self.team_2)   #nameteam
                t_4.append(int(self.score_2))        #score  
                t_4.append(int(self.point_2))        #point
                t_4.append(int(self.GD2))           #ประตูที่ได้ 
                t_4.append(int(self.GB2))   #ประตูที่เสีย
                t_4.append(1)

                print(t_8)
                print(t_4)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[7] and self.team_2 == listteam[4]:
            try:
                t_8.append(self.team_1 ) #nameteam
                t_8.append(int(self.score_1))        #score  
                t_8.append(int(self.point_1))        #point
                t_8.append(int(self.GD1))           #ประตูที่ได้ 
                t_8.append(int(self.GB1))   #ประตูที่เสีย
                t_8.append(1)
                t_5.append(self.team_2)   #nameteam
                t_5.append(int(self.score_2))        #score  
                t_5.append(int(self.point_2))        #point
                t_5.append(int(self.GD2))           #ประตูที่ได้ 
                t_5.append(int(self.GB2))   #ประตูที่เสีย
                t_5.append(1)

                print(t_8)
                print(t_5)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[7] and self.team_2 == listteam[5]:
            try:
                t_8.append(self.team_1 ) #nameteam
                t_8.append(int(self.score_1))        #score  
                t_8.append(int(self.point_1))        #point
                t_8.append(int(self.GD1))           #ประตูที่ได้ 
                t_8.append(int(self.GB1))   #ประตูที่เสีย
                t_8.append(1)
                t_6.append(self.team_2)   #nameteam
                t_6.append(int(self.score_2))        #score  
                t_6.append(int(self.point_2))        #point
                t_6.append(int(self.GD2))           #ประตูที่ได้ 
                t_6.append(int(self.GB2))   #ประตูที่เสีย
                t_6.append(1)

                print(t_8)
                print(t_6)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[7] and self.team_2 == listteam[6]:
            try:
                t_8.append(self.team_1 ) #nameteam
                t_8.append(int(self.score_1))        #score  
                t_8.append(int(self.point_1))        #point
                t_8.append(int(self.GD1))           #ประตูที่ได้ 
                t_8.append(int(self.GB1))   #ประตูที่เสีย
                t_8.append(1)
                t_7.append(self.team_2)   #nameteam
                t_7.append(int(self.score_2))        #score  
                t_7.append(int(self.point_2))        #point
                t_7.append(int(self.GD2))           #ประตูที่ได้ 
                t_7.append(int(self.GB2))   #ประตูที่เสีย
                t_7.append(1)

                print(t_8)
                print(t_7)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[7] and self.team_2 == listteam[8]:
            try:
                t_8.append(self.team_1 ) #nameteam
                t_8.append(int(self.score_1))        #score  
                t_8.append(int(self.point_1))        #point
                t_8.append(int(self.GD1))           #ประตูที่ได้ 
                t_8.append(int(self.GB1))   #ประตูที่เสีย
                t_8.append(1)
                t_9.append(self.team_2)   #nameteam
                t_9.append(int(self.score_2))        #score  
                t_9.append(int(self.point_2))        #point
                t_9.append(int(self.GD2))           #ประตูที่ได้ 
                t_9.append(int(self.GB2))   #ประตูที่เสีย
                t_9.append(1)

                print(t_8)
                print(t_9)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[7] and self.team_2 == listteam[9]:
            try:
                t_8.append(self.team_1 ) #nameteam
                t_8.append(int(self.score_1))        #score  
                t_8.append(int(self.point_1))        #point
                t_8.append(int(self.GD1))           #ประตูที่ได้ 
                t_8.append(int(self.GB1))   #ประตูที่เสีย
                t_8.append(1)
                t_10.append(self.team_2)   #nameteam
                t_10.append(int(self.score_2))        #score  
                t_10.append(int(self.point_2))        #point
                t_10.append(int(self.GD2))           #ประตูที่ได้ 
                t_10.append(int(self.GB2))   #ประตูที่เสีย
                t_10.append(1)

                print(t_8)
                print(t_10)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[8] and self.team_2 == listteam[0]:
            try:
                t_9.append(self.team_1 ) #nameteam
                t_9.append(int(self.score_1))        #score  
                t_9.append(int(self.point_1))        #point
                t_9.append(int(self.GD1))           #ประตูที่ได้ 
                t_9.append(int(self.GB1))   #ประตูที่เสีย
                t_9.append(1)
                t_1.append(self.team_2)   #nameteam
                t_1.append(int(self.score_2))        #score  
                t_1.append(int(self.point_2))        #point
                t_1.append(int(self.GD2))           #ประตูที่ได้ 
                t_1.append(int(self.GB2))   #ประตูที่เสีย
                t_1.append(1)

                print(t_9)
                print(t_1)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[8] and self.team_2 == listteam[1]:
            try:
                t_9.append(self.team_1 ) #nameteam
                t_9.append(int(self.score_1))        #score  
                t_9.append(int(self.point_1))        #point
                t_9.append(int(self.GD1))           #ประตูที่ได้ 
                t_9.append(int(self.GB1))   #ประตูที่เสีย
                t_9.append(1)
                t_2.append(self.team_2)   #nameteam
                t_2.append(int(self.score_2))        #score  
                t_2.append(int(self.point_2))        #point
                t_2.append(int(self.GD2))           #ประตูที่ได้ 
                t_2.append(int(self.GB2))   #ประตูที่เสีย
                t_2.append(1)

                print(t_9)
                print(t_2)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[8] and self.team_2 == listteam[2]:
            try:
                t_9.append(self.team_1 ) #nameteam
                t_9.append(int(self.score_1))        #score  
                t_9.append(int(self.point_1))        #point
                t_9.append(int(self.GD1))           #ประตูที่ได้ 
                t_9.append(int(self.GB1))   #ประตูที่เสีย
                t_9.append(1)
                t_3.append(self.team_2)   #nameteam
                t_3.append(int(self.score_2))        #score  
                t_3.append(int(self.point_2))        #point
                t_3.append(int(self.GD2))           #ประตูที่ได้ 
                t_3.append(int(self.GB2))   #ประตูที่เสีย
                t_3.append(1)

                print(t_9)
                print(t_3)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[8] and self.team_2 == listteam[3]:
            try:
                t_9.append(self.team_1 ) #nameteam
                t_9.append(int(self.score_1))        #score  
                t_9.append(int(self.point_1))        #point
                t_9.append(int(self.GD1))           #ประตูที่ได้ 
                t_9.append(int(self.GB1))   #ประตูที่เสีย
                t_9.append(1)
                t_4.append(self.team_2)   #nameteam
                t_4.append(int(self.score_2))        #score  
                t_4.append(int(self.point_2))        #point
                t_4.append(int(self.GD2))           #ประตูที่ได้ 
                t_4.append(int(self.GB2))   #ประตูที่เสีย
                t_4.append(1)

                print(t_9)
                print(t_4)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[8] and self.team_2 == listteam[4]:
            try:
                t_9.append(self.team_1 ) #nameteam
                t_9.append(int(self.score_1))        #score  
                t_9.append(int(self.point_1))        #point
                t_9.append(int(self.GD1))           #ประตูที่ได้ 
                t_9.append(int(self.GB1))   #ประตูที่เสีย
                t_9.append(1)
                t_5.append(self.team_2)   #nameteam
                t_5.append(int(self.score_2))        #score  
                t_5.append(int(self.point_2))        #point
                t_5.append(int(self.GD2))           #ประตูที่ได้ 
                t_5.append(int(self.GB2))   #ประตูที่เสีย
                t_5.append(1)

                print(t_9)
                print(t_5)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[8] and self.team_2 == listteam[5]:
            try:
                t_9.append(self.team_1 ) #nameteam
                t_9.append(int(self.score_1))        #score  
                t_9.append(int(self.point_1))        #point
                t_9.append(int(self.GD1))           #ประตูที่ได้ 
                t_9.append(int(self.GB1))   #ประตูที่เสีย
                t_9.append(1)
                t_6.append(self.team_2)   #nameteam
                t_6.append(int(self.score_2))        #score  
                t_6.append(int(self.point_2))        #point
                t_6.append(int(self.GD2))           #ประตูที่ได้ 
                t_6.append(int(self.GB2))   #ประตูที่เสีย
                t_6.append(1)

                print(t_9)
                print(t_6)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[8] and self.team_2 == listteam[6]:
            try:
                t_9.append(self.team_1 ) #nameteam
                t_9.append(int(self.score_1))        #score  
                t_9.append(int(self.point_1))        #point
                t_9.append(int(self.GD1))           #ประตูที่ได้ 
                t_9.append(int(self.GB1))   #ประตูที่เสีย
                t_9.append(1)
                t_7.append(self.team_2)   #nameteam
                t_7.append(int(self.score_2))        #score  
                t_7.append(int(self.point_2))        #point
                t_7.append(int(self.GD2))           #ประตูที่ได้ 
                t_7.append(int(self.GB2))   #ประตูที่เสีย
                t_7.append(1)

                print(t_9)
                print(t_7)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[8] and self.team_2 == listteam[7]:
            try:
                t_9.append(self.team_1 ) #nameteam
                t_9.append(int(self.score_1))        #score  
                t_9.append(int(self.point_1))        #point
                t_9.append(int(self.GD1))           #ประตูที่ได้ 
                t_9.append(int(self.GB1))   #ประตูที่เสีย
                t_9.append(1)
                t_8.append(self.team_2)   #nameteam
                t_8.append(int(self.score_2))        #score  
                t_8.append(int(self.point_2))        #point
                t_8.append(int(self.GD2))           #ประตูที่ได้ 
                t_8.append(int(self.GB2))   #ประตูที่เสีย
                t_8.append(1)

                print(t_9)
                print(t_8)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[8] and self.team_2 == listteam[9]:
            try:
                t_9.append(self.team_1 ) #nameteam
                t_9.append(int(self.score_1))        #score  
                t_9.append(int(self.point_1))        #point
                t_9.append(int(self.GD1))           #ประตูที่ได้ 
                t_9.append(int(self.GB1))   #ประตูที่เสีย
                t_9.append(1)
                t_10.append(self.team_2)   #nameteam
                t_10.append(int(self.score_2))        #score  
                t_10.append(int(self.point_2))        #point
                t_10.append(int(self.GD2))           #ประตูที่ได้ 
                t_10.append(int(self.GB2))   #ประตูที่เสีย
                t_10.append(1)

                print(t_9)
                print(t_10)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[9] and self.team_2 == listteam[0]:
            try:
                t_10.append(self.team_1 ) #nameteam
                t_10.append(int(self.score_1))        #score  
                t_10.append(int(self.point_1))        #point
                t_10.append(int(self.GD1))           #ประตูที่ได้ 
                t_10.append(int(self.GB1))   #ประตูที่เสีย
                t_10.append(1)
                t_1.append(self.team_2)   #nameteam
                t_1.append(int(self.score_2))        #score  
                t_1.append(int(self.point_2))        #point
                t_1.append(int(self.GD2))           #ประตูที่ได้ 
                t_1.append(int(self.GB2))   #ประตูที่เสีย
                t_1.append(1)

                print(t_10)
                print(t_1)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[9] and self.team_2 == listteam[1]:
            try:
                t_10.append(self.team_1 ) #nameteam
                t_10.append(int(self.score_1))        #score  
                t_10.append(int(self.point_1))        #point
                t_10.append(int(self.GD1))           #ประตูที่ได้ 
                t_10.append(int(self.GB1))   #ประตูที่เสีย
                t_10.append(1)
                t_2.append(self.team_2)   #nameteam
                t_2.append(int(self.score_2))        #score  
                t_2.append(int(self.point_2))        #point
                t_2.append(int(self.GD2))           #ประตูที่ได้ 
                t_2.append(int(self.GB2))   #ประตูที่เสีย
                t_2.append(1)

                print(t_10)
                print(t_2)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[9] and self.team_2 == listteam[2]:
            try:
                t_10.append(self.team_1 ) #nameteam
                t_10.append(int(self.score_1))        #score  
                t_10.append(int(self.point_1))        #point
                t_10.append(int(self.GD1))           #ประตูที่ได้ 
                t_10.append(int(self.GB1))   #ประตูที่เสีย
                t_10.append(1)
                t_3.append(self.team_2)   #nameteam
                t_3.append(int(self.score_2))        #score  
                t_3.append(int(self.point_2))        #point
                t_3.append(int(self.GD2))           #ประตูที่ได้ 
                t_3.append(int(self.GB2))   #ประตูที่เสีย
                t_3.append(1)

                print(t_10)
                print(t_3)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[9] and self.team_2 == listteam[3]:
            try:
                t_10.append(self.team_1 ) #nameteam
                t_10.append(int(self.score_1))        #score  
                t_10.append(int(self.point_1))        #point
                t_10.append(int(self.GD1))           #ประตูที่ได้ 
                t_10.append(int(self.GB1))   #ประตูที่เสีย
                t_10.append(1)
                t_4.append(self.team_2)   #nameteam
                t_4.append(int(self.score_2))        #score  
                t_4.append(int(self.point_2))        #point
                t_4.append(int(self.GD2))           #ประตูที่ได้ 
                t_4.append(int(self.GB2))   #ประตูที่เสีย
                t_4.append(1)

                print(t_10)
                print(t_4)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[9] and self.team_2 == listteam[4]:
            try:
                t_10.append(self.team_1 ) #nameteam
                t_10.append(int(self.score_1))        #score  
                t_10.append(int(self.point_1))        #point
                t_10.append(int(self.GD1))           #ประตูที่ได้ 
                t_10.append(int(self.GB1))   #ประตูที่เสีย
                t_10.append(1)
                t_5.append(self.team_2)   #nameteam
                t_5.append(int(self.score_2))        #score  
                t_5.append(int(self.point_2))        #point
                t_5.append(int(self.GD2))           #ประตูที่ได้ 
                t_5.append(int(self.GB2))   #ประตูที่เสีย
                t_5.append(1)

                print(t_10)
                print(t_5)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[9] and self.team_2 == listteam[5]:
            try:
                t_10.append(self.team_1 ) #nameteam
                t_10.append(int(self.score_1))        #score  
                t_10.append(int(self.point_1))        #point
                t_10.append(int(self.GD1))           #ประตูที่ได้ 
                t_10.append(int(self.GB1))   #ประตูที่เสีย
                t_10.append(1)
                t_6.append(self.team_2)   #nameteam
                t_6.append(int(self.score_2))        #score  
                t_6.append(int(self.point_2))        #point
                t_6.append(int(self.GD2))           #ประตูที่ได้ 
                t_6.append(int(self.GB2))   #ประตูที่เสีย
                t_6.append(1)

                print(t_10)
                print(t_6)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[9] and self.team_2 == listteam[6]:
            try:
                t_10.append(self.team_1 ) #nameteam
                t_10.append(int(self.score_1))        #score  
                t_10.append(int(self.point_1))        #point
                t_10.append(int(self.GD1))           #ประตูที่ได้ 
                t_10.append(int(self.GB1))   #ประตูที่เสีย
                t_10.append(1)
                t_7.append(self.team_2)   #nameteam
                t_7.append(int(self.score_2))        #score  
                t_7.append(int(self.point_2))        #point
                t_7.append(int(self.GD2))           #ประตูที่ได้ 
                t_7.append(int(self.GB2))   #ประตูที่เสีย
                t_7.append(1)

                print(t_10)
                print(t_7)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[9] and self.team_2 == listteam[7]:
            try:
                t_10.append(self.team_1 ) #nameteam
                t_10.append(int(self.score_1))        #score  
                t_10.append(int(self.point_1))        #point
                t_10.append(int(self.GD1))           #ประตูที่ได้ 
                t_10.append(int(self.GB1))   #ประตูที่เสีย
                t_10.append(1)
                t_8.append(self.team_2)   #nameteam
                t_8.append(int(self.score_2))        #score  
                t_8.append(int(self.point_2))        #point
                t_8.append(int(self.GD2))           #ประตูที่ได้ 
                t_8.append(int(self.GB2))   #ประตูที่เสีย
                t_8.append(1)

                print(t_10)
                print(t_8)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        elif self.team_1 == listteam[9] and self.team_2 == listteam[8]:
            try:
                t_10.append(self.team_1 ) #nameteam
                t_10.append(int(self.score_1))        #score  
                t_10.append(int(self.point_1))        #point
                t_10.append(int(self.GD1))           #ประตูที่ได้ 
                t_10.append(int(self.GB1))   #ประตูที่เสีย
                t_10.append(1)
                t_9.append(self.team_2)   #nameteam
                t_9.append(int(self.score_2))        #score  
                t_9.append(int(self.point_2))        #point
                t_9.append(int(self.GD2))           #ประตูที่ได้ 
                t_9.append(int(self.GB2))   #ประตูที่เสีย
                t_9.append(1)

                print(t_10)
                print(t_9)
            except Exception as e:
                notify = Label(wrapper2,text="Please enter a number",font="Tohama 11 ",fg="red")
                notify.grid(row=3,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
        with open(filepath,"w",encoding='utf-8') as f1:
            writer = csv.writer(f1)
            writer.writerow(t_1)
            writer.writerow(t_2)
            writer.writerow(t_3)
            writer.writerow(t_4)
            writer.writerow(t_5)
            writer.writerow(t_6)
            writer.writerow(t_7)
            writer.writerow(t_8)
            writer.writerow(t_9)
            writer.writerow(t_10)    


def submit():
    global se1
    nameteam_1 = mycombo_1.get()
    nameteam_2 = mycombo_2.get()
    score_1= GD1 = GB2 = Escore1.get() 
    score_2 = GD2 = GB1 = Escore2.get()
    
    if score_1 > score_2:
        point_1 = 3
        point_2 = 0
    elif score_1 < score_2:
        point_1 = 0
        point_2 = 3
    elif score_1 == score_2:
        point_1 = 1
        point_2 = 1

    se1 = football(nameteam_1,score_1,point_1,nameteam_2,score_2,point_2,GD1,GD2,GB1,GB2)


      

#def clear():
    
    #Escore1.delete(0,END)
    #Escore2.delete(0,END)

#Text
team_host = Label(wrapper2,text="Team Host",font="Roboto 12 bold  ",fg="#A20E0E",bg="#EFDB43")
team_guest = Label(wrapper2,text="Team Guest",font="Roboto 12 bold  ",fg="#A20E0E",bg="#EFDB43")
team_score_1 = Label(wrapper2,text="Score",font="Roboto 12 bold  ",fg="#A20E0E",bg="#EFDB43")
team_score_2 = Label(wrapper2,text="Score",font="Roboto 12 bold  ",fg="#A20E0E",bg="#EFDB43")
team_host.grid(row=1,column=1,pady=10,sticky=S)
team_guest.grid(row=1,column=5,pady=10)
team_score_1.grid(row=1,column=2)
team_score_2.grid(row=1,column=4)
# Input Name Team

# Input score Team
Escore1 = Entry(wrapper2,width=10,font="Roboto 12 bold  ",fg="#4A0606",bg="#F8B4B4",borderwidth=2)
Escore2 = Entry(wrapper2,width=10,font="Roboto 12 bold  ",fg="#4A0606",bg="#F8B4B4",borderwidth=2)
Escore1.grid(row=2,column=2,padx=10)
Escore2.grid(row=2,column=4,padx=10)

vs = Label(wrapper2,text="VS",font="Roboto 14 bold  ",fg="#6F346F",bg="#EFDB43")
vs.grid(row=2,column=3)


# button

bt_submit = Button(wrapper2,text="Add Score Team",command=submit,font="Roboto 11 bold  ",fg="#FFFFFF",bg="#054B0D")
#bt_clear = Button(wrapper2,text="CLEAR!!!!!",command=clear)
bt_submit.grid(row=4,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
#bt_clear.grid(row=5,column=1,columnspan=5,ipadx=100,padx=10)



#-----------------------wraper 3-------------------------
#bt ranking

def rangking():
    try:
    #team 1
        if 1>0:
            for i in range(1,t_1.count(t_1[0])):
                p1 = 7
                sc = 6
                sc = i+(sc*i) -(i-1)
                p1 = i+(p1*i) -(i-1)
                gd1 = 8
                gb1 = 9
                py1 = 10
                gd1 = i + (gd1*i) - (i-1)
                gb1 = i + (gb1*i) - (i-1)
                py1 = i + (py1*i) - (i-1)
                t_1[1] = t_1[1] + t_1[sc]
                t_1[2] = t_1[2] + t_1[p1]
                t_1[3] = t_1[3] + t_1[gd1]
                t_1[4] = t_1[4] + t_1[gb1]
                t_1[5] = t_1[5] + t_1[py1]

            x1 = ('Team : {}   Totalscore : {}  Totalpoint : {}  GD : {}  GB: {}  Played: {}'.format(t_1[0],t_1[1],t_1[2],t_1[3],t_1[4],t_1[5]))
            print(x1)
            t1 = Label(wrapper3,text=x1,font="Roboto 12 bold",bg="#EFDB43",fg="#760A0A")
            t1.grid(row=2,column=1,columnspan=3,sticky=W)

        #team 2
        if 1>0:
            for i in range(1,t_2.count(t_2[0])):
                p2 = 7
                sc2 = 6
                sc2 = i+(sc2*i) -(i-1)
                p2 = i+(p2*i) -(i-1)
                gd2 = 8
                gb2 = 9
                py2 = 10
                gd2 = i + (gd2*i) - (i-1)
                gb2 = i + (gb2*i) - (i-1)
                py2 = i + (py2*i) - (i-1)
                t_2[1] = t_2[1] + t_2[sc2]
                t_2[2] = t_2[2] + t_2[p2]
                t_2[3] = t_2[3] + t_2[gd2]
                t_2[4] = t_2[4] + t_2[gb2]
                t_2[5] = t_2[5] + t_2[py2]

            x2 = ('Team : {}   Totalscore : {}  Totalpoint : {}  GD : {}  GB: {}  Played: {}'.format(t_2[0],t_2[1],t_2[2],t_2[3],t_2[4],t_2[5]))
            print(x2)
            t2 = Label(wrapper3,text=x2,font="Roboto 12 bold",bg="#EFDB43",fg="#760A0A")
            t2.grid(row=3,column=1,columnspan=3,sticky=W)

        #team 3
        if 1>0:
            for i in range(1,t_3.count(t_3[0])):
                p3 = 7
                sc3 = 6
                sc3 = i+(sc3*i) -(i-1)
                p3 = i+(p3*i) -(i-1)
                gd3 = 8
                gb3 = 9
                py3 = 10
                gd3 = i + (gd3*i) - (i-1)
                gb3 = i + (gb3*i) - (i-1)
                py3 = i + (py3*i) - (i-1)
                t_3[1] = t_3[1] + t_3[sc3]
                t_3[2] = t_3[2] + t_3[p3]
                t_3[3] = t_3[3] + t_3[gd3]
                t_3[4] = t_3[4] + t_3[gb3]
                t_3[5] = t_3[5] + t_3[py3]
            x3 = ('Team : {}   Totalscore : {}  Totalpoint : {}  GD : {}  GB: {}  Played: {}'.format(t_3[0],t_3[1],t_3[2],t_3[3],t_3[4],t_3[5]))
            print(x3)
            t3 = Label(wrapper3,text=x3,font="Roboto 12 bold",bg="#EFDB43",fg="#760A0A")
            t3.grid(row=4,column=1,columnspan=3,sticky=W)

        #team 4
        if 1>0:
            for i in range(1,t_4.count(t_4[0])):
                p4 = 7
                sc4 = 6
                sc4 = i+(sc4*i) -(i-1)
                p4 = i+(p4*i) -(i-1)
                gd4 = 8
                gb4 = 9
                py4 = 10
                gd4 = i + (gd4*i) - (i-1)
                gb4 = i + (gb4*i) - (i-1)
                py4 = i + (py4*i) - (i-1)
                t_4[1] = t_4[1] + t_4[sc4]
                t_4[2] = t_4[2] + t_4[p4]
                t_4[3] = t_4[3] + t_4[gd4]
                t_4[4] = t_4[4] + t_4[gb4]
                t_4[5] = t_4[5] + t_4[py4]

            x4 = ('Team : {}   Totalscore : {}  Totalpoint : {}  GD : {}  GB: {}  Played: {}'.format(t_4[0],t_4[1],t_4[2],t_4[3],t_4[4],t_4[5]))
            print(x4)
            t4 = Label(wrapper3,text=x4,font="Roboto 12 bold",bg="#EFDB43",fg="#760A0A")
            t4.grid(row=5,column=1,columnspan=3,sticky=W)

        #team 5
        if 1>0:
            for i in range(1,t_5.count(t_5[0])):
                p5 = 7
                sc5= 6
                sc5 = i+(sc5*i) -(i-1)
                p5 = i+(p5*i) -(i-1)
                gd5 = 8
                gb5 = 9
                py5 = 10
                gd5 = i + (gd5*i) - (i-1)
                gb5 = i + (gb5*i) - (i-1)
                py5 = i + (py5*i) - (i-1)
                t_5[1] = t_5[1] + t_5[sc5]
                t_5[2] = t_5[2] + t_5[p5]
                t_5[3] = t_5[3] + t_5[gd5]
                t_5[4] = t_5[4] + t_5[gb5]
                t_5[5] = t_5[5] + t_5[py5]

            x5 = ('Team : {}   Totalscore : {}  Totalpoint : {}  GD : {}  GB: {}  Played: {}'.format(t_5[0],t_5[1],t_5[2],t_5[3],t_5[4],t_5[5]))
            print(x5)
            t5 = Label(wrapper3,text=x5,font="Roboto 12 bold",bg="#EFDB43",fg="#760A0A")
            t5.grid(row=6,column=1,columnspan=3,sticky=W)

        #team 6
        if 1>0:
            for i in range(1,t_6.count(t_6[0])):
                p6 = 7
                sc6 = 6
                sc6 = i+(sc6*i) -(i-1)
                p6 = i+(p6*i) -(i-1)
                gd6 = 8
                gb6 = 9
                py6 = 10
                gd6 = i + (gd6*i) - (i-1)
                gb6 = i + (gb6*i) - (i-1)
                py6 = i + (py6*i) - (i-1)
                t_6[1] = t_6[1] + t_6[sc6]
                t_6[2] = t_6[2] + t_6[p6]
                t_6[3] = t_6[3] + t_6[gd6]
                t_6[4] = t_6[4] + t_6[gb6]
                t_6[5] = t_6[5] + t_6[py6]

            x6 = ('Team : {}   Totalscore : {}  Totalpoint : {}  GD : {}  GB: {}  Played: {}'.format(t_6[0],t_6[1],t_6[2],t_6[3],t_6[4],t_6[5]))
            print(x6)
            t6 = Label(wrapper3,text=x6,font="Roboto 12 bold",bg="#EFDB43",fg="#760A0A")
            t6.grid(row=7,column=1,columnspan=3,sticky=W)

        #team 7
        if 1>0:
            for i in range(1,t_7.count(t_7[0])):
                p7 = 7
                sc7 = 6
                sc7 = i+(sc7*i) -(i-1)
                p7 = i+(p7*i) -(i-1)
                gd7 = 8
                gb7 = 9
                py7 = 10
                gd7 = i + (gd7*i) - (i-1)
                gb7 = i + (gb7*i) - (i-1)
                py7 = i + (py7*i) - (i-1)
                t_7[1] = t_1[1] + t_7[sc7]
                t_7[2] = t_1[2] + t_7[p7]
                t_7[3] = t_1[3] + t_7[gd7]
                t_7[4] = t_1[4] + t_7[gb7]
                t_7[5] = t_1[5] + t_7[py7]

            x7 = ('Team : {}   Totalscore : {}  Totalpoint : {}  GD : {}  GB: {}  Played: {}'.format(t_7[0],t_7[1],t_7[2],t_7[3],t_7[4],t_7[5]))
            print(x7)
            t7 = Label(wrapper3,text=x7,font="Tohama 12")
            t7.grid(row=8,column=1,columnspan=3)

        #team 8
        if 1>0:
            for i in range(1,t_8.count(t_8[0])):
                p8 = 7
                sc8 = 6
                sc8 = i+(sc8*i) -(i-1)
                p8 = i+(p8*i) -(i-1)
                gd8 = 8
                gb8 = 9
                py8 = 10
                gd8 = i + (gd8*i) - (i-1)
                gb8 = i + (gb8*i) - (i-1)
                py8 = i + (py8*i) - (i-1)
                t_8[1] = t_8[1] + t_8[sc8]
                t_8[2] = t_8[2] + t_8[p8]
                t_8[3] = t_8[3] + t_8[gd8]
                t_8[4] = t_8[4] + t_8[gb8]
                t_8[5] = t_8[5] + t_8[py8]

            x8 = ('Team : {}   Totalscore : {}  Totalpoint : {}  GD : {}  GB: {}  Played: {}'.format(t_8[0],t_8[1],t_8[2],t_8[3],t_8[4],t_8[5]))
            print(x8)
            t8 = Label(wrapper3,text=x8,font="Roboto 12 bold",bg="#EFDB43",fg="#760A0A")
            t8.grid(row=9,column=1,columnspan=3,sticky=W)

        #team 9
        if 1>0:
            for i in range(1,t_9.count(t_9[0])):
                p9 = 7
                sc9 = 6
                sc9 = i+(sc9*i) -(i-1)
                p9 = i+(p9*i) -(i-1)
                gd9 = 8
                gb9 = 9
                py9 = 10
                gd9 = i + (gd9*i) - (i-1)
                gb9 = i + (gb9*i) - (i-1)
                py9 = i + (py9*i) - (i-1)
                t_9[1] = t_9[1] + t_9[sc9]
                t_9[2] = t_9[2] + t_9[p9]
                t_9[3] = t_9[3] + t_9[gd9]
                t_9[4] = t_9[4] + t_9[gb9]
                t_9[5] = t_9[5] + t_9[py9]

            x9 = ('Team : {}   Totalscore : {}  Totalpoint : {}  GD : {}  GB: {}  Played: {}'.format(t_9[0],t_9[1],t_9[2],t_9[3],t_9[4],t_9[5]))
            print(x9)
            t9 = Label(wrapper3,text=x9,font="Roboto 12 bold",bg="#EFDB43",fg="#760A0A")
            t9.grid(row=10,column=1,columnspan=3,sticky=W)

        #team 10
        if 1> 0:
            for i in range(1,t_10.count(t_10[0])):
                p10 = 7
                sc10 = 6
                sc10 = i+(sc10*i) -(i-1)
                p10 = i+(p10*i) -(i-1)
                gd10 = 8
                gb10 = 9
                py10 = 10
                gd10 = i + (gd10*i) - (i-1)
                gb10 = i + (gb10*i) - (i-1)
                py10 = i + (py10*i) - (i-1)
                t_10[1] = t_10[1] + t_10[sc10]
                t_10[2] = t_10[2] + t_10[p10]
                t_10[3] = t_10[3] + t_10[gd10]
                t_10[4] = t_10[4] + t_10[gb10]
                t_10[5] = t_10[5] + t_10[py10]

            x10 = ('Team : {}   Totalscore : {}  Totalpoint : {}  GD : {}  GB: {}  Played: {}'.format(t_10[0],t_10[1],t_10[2],t_10[3],t_10[4],t_10[5]))
            print(x10)
            t10 = Label(wrapper3,text=x10,font="Roboto 12 bold",bg="#EFDB43",fg="#760A0A")
            t10.grid(row=11,column=1,columnspan=3,sticky=W)

    except Exception as e:
        print(e)


bt_ranking = Button(wrapper3,text="Total Score",font="Roboto 11 bold  ",fg="#FFFFFF",bg="#054B0D",command=rangking)
bt_ranking.grid(row=1,column=1,padx=10,pady=10)



root.minsize(400,400)
root.mainloop()