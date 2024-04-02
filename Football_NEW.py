from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
#import mysql.connector

root = Tk()
root.title("My Application")
#root.iconbitmap("C:/Users/sarif/Desktop/project.compro/GUI/icon.ico")


wrapper1 = LabelFrame(root,text="Enter Name Team")
wrapper2 = LabelFrame(root,text="Match Score")
wrapper3 = LabelFrame(root,text="Team All")

wrapper1.pack(fill="both", expand="yes",padx=20,pady=20)
wrapper2.pack(fill="both", expand="yes",padx=20,pady=20)
wrapper3.pack(fill="both", expand="yes",padx=20,pady=20)
#wraooer 1 ---------------------------------------------
#my combo
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

class football:
    def __init__(self,name):
            self.name = name
            self.points = self.gf = self.ga = self.wins = self.draws = self.losses = 0

    def add_goals(self, goals):
            self.gf += goals

    # list ชื่อทีมฟุตบอล
listteam = []
football(len(listteam))


        #text 
Enter_name_team = Label(wrapper1,text="Enter Name Team : ",font="Helevic 11 bold  ",fg="black")
Enter_name_team.grid(row=1,column=1,pady=20,padx=10,sticky=E)

        #input name team
input_name_team = Entry(wrapper1,width=20,font="Tohama 12   ",fg="black")
input_name_team.grid(row=1,column=2,columnspan=3,pady=20,padx=10)

            # bt
btsubmit = Button(wrapper1,text="Add Name Team",command=sb,font="Tohama 11   ",fg="white",bg="green")
btsubmit.grid(row=2,column=1,columnspan=5,ipadx=50,padx=10)


#-----------------------wraper 2-------------------------
    #funtion def\
    #รวมทีมที่ใส่มาทั้งหมด
league_size=len(listteam)
    #จำนวนทีมที่มาแข่ง
league_size=len(listteam)

    #list ทีไว้ใส่ข้อมูล
POINTS = []
GOALS_FOR = []
GOALS_AGAINST = []
WINS =[]
DRAWS = []
LOSSES = []

for x in range(league_size):
    POINTS += [0]
    WINS += [0]
    DRAWS += [0]
    LOSSES += [0]

def home_score(home, away):
        homescore = home
        awayscore = away

        if homescore == awayscore:
                raise ValueError 

        if homescore > awayscore:
                homeGoals = 0
                while homescore > awayscore :
                    homeGoals += 1
                return (homeGoals - 1)

        if homescore < awayscore:
                homeGoals = 0
                while homescore < awayscore :
                    homeGoals += 1
                return (homeGoals - 1)

def away_score(home, away):
        awayscore = away
        homescore = home

        if awayscore == homescore:
                return  "Teams cannot play themselves!!!"

        if awayscore > homescore:
                awayGoals = 0
                while homescore > awayscore :
                    awayGoals += 1
                return (awayGoals - 1)
                        
        if awayscore < homescore:
                awayGoals = 0
                while awayscore < homescore :
                    awayGoals += 1
                return (awayGoals - 1)

def submit():    
        
            mycombo_1.get()
            mycombo_2.get()
            homeScore = Escore1.get() 
            awayScore = Escore2.get()
                
            for x in range(league_size):
                print("========================================")
                print(listteam[x].name + "'s home games: ")
                print("========================================")
                for y in range(league_size):
                    error = 0
                try:
                    homeScore = home_score(listteam[x], listteam[y])
                except ValueError:
                    pass
                    error += 1
                try:
                    awayScore = away_score(listteam[x], listteam[y])
                except ValueError:
                    pass
                if error == 0:

                    print(listteam[x].name, homeScore, ":", awayScore, listteam[y].name)
                    GOALS_FOR[x] += homeScore
                    GOALS_FOR[y] += awayScore
                    GOALS_AGAINST[x] += awayScore
                    GOALS_AGAINST[y] += homeScore

                    if homeScore > awayScore:
                        WINS[x] += 1
                        LOSSES[y] += 1
                        POINTS[x] += 3

                    elif homeScore == awayScore:
                        DRAWS[x] += 1
                        DRAWS[y] += 1
                        POINTS[x] += 1
                        POINTS[y] += 1

                    else:
                        WINS[y] += 1
                        LOSSES[x] += 1
                        POINTS[y] += 3
                else:
                    pass

            #label
            lb_nametemehost = Label(wrapper2,text=mycombo_1.get(),font="Tohama 11   ",fg="black")
            lb_nametemeguest = Label(wrapper2,text=mycombo_2.get(),font="Tohama 11   ",fg="black")
            lb_nametemehost.grid(row=3,column=1)
            lb_nametemeguest.grid(row=3,column=5)
            lb_score_1 = Label(wrapper2,text=Escore1.get(),font="Tohama 11   ",fg="black")
            lb_score_2 = Label(wrapper2,text=Escore2.get(),font="Tohama 11   ",fg="black")
            lb_score_1.grid(row=3,column=2)
            lb_score_2.grid(row=3,column=4)
            
for x in range(league_size):
    listteam[x].points = POINTS[x]
    listteam[x].gf = GOALS_FOR[x]
    listteam[x].ga = GOALS_AGAINST[x]
    listteam[x].wins = WINS[x]
    listteam[x].draws = DRAWS[x] 
    listteam[x].losses = LOSSES[x]
            
            


        
#def clear():
    
    #Escore1.delete(0,END)
    #Escore2.delete(0,END)

#Text
team_host = Label(wrapper2,text="Team Host",font="Helevic 11   ",fg="black")
team_guest = Label(wrapper2,text="Team Guest",font="Helevic 11   ",fg="black")
team_score_1 = Label(wrapper2,text="Score",font="Helevic 11   ",fg="black")
team_score_2 = Label(wrapper2,text="Score",font="Helevic 11  ",fg="black")
team_host.grid(row=1,column=1,pady=10,sticky=S)
team_guest.grid(row=1,column=5,pady=10)
team_score_1.grid(row=1,column=2)
team_score_2.grid(row=1,column=4)
# Input Name Team

# Input score Team
Escore1 = Entry(wrapper2,width=10)
Escore2 = Entry(wrapper2,width=10)
Escore1.grid(row=2,column=2,padx=10)
Escore2.grid(row=2,column=4,padx=10)

vs = Label(wrapper2,text="VS",font="Helevic 14 bold italic ",fg="crimson")
vs.grid(row=2,column=3)


# button

bt_submit = Button(wrapper2,text="Add Score Team -->>>",command=submit)
#bt_clear = Button(wrapper2,text="CLEAR!!!!!",command=clear)
bt_submit.grid(row=4,column=1,columnspan=5,ipadx=100,padx=10,pady=10)
#bt_clear.grid(row=5,column=1,columnspan=5,ipadx=100,padx=10)



#-----------------------wraper 3-------------------------
sorted_teams = sorted(listteam, key=lambda t: t.points, reverse=True)
listteam.append(sorted_teams)
filepath='DATA ALL TEAM.txt'
row = sorted_teams
with open(filepath,"w",encoding='utf8')as outfile:
    write = csv.writer(outfile)
    write.writerow(row) 
trv = ttk.Treeview(wrapper3,columns=(1,2,3,4,5,6,7,8), show="headings",height="20")
trv.pack()
trv.heading(1, text="Rank")
trv.heading(2, text="Name Team")
trv.heading(3, text="Played")
trv.heading(4, text="Won")
trv.heading(5, text="Draw")
trv.heading(6, text="Lost")
trv.heading(7, text="Goals")
trv.heading(8, text="Piont")

root.minsize(400,400)
root.mainloop()

