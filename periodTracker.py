import flowEnum
from tkinter.ttk import Progressbar
from tkinter import *

root = Tk()
root.title("Period Tracker")
root.geometry('450x250')
root.resizable(0,0)

tempList = ["2023-05-19","2023-05-18","2023-05-17","2023-05-16","2023-04-17"]

def fillList():
    lst = []
    for dt in tempList:
        lst.append(dt)
    return lst

def popup():

    def getFlowIntensity():
        flowIntensity = flowVar.get()

    def getMoodEntry():
        return moodEntry.get()
    
    def getSymptomEntry():
        return symptomEntry.get()
    
    def saveData():
        mdntry = getMoodEntry()
        #moodEntry.delete(0, END)
        smptmntry = getSymptomEntry()
        #symptomEntry.delete(0, END)
        logPeriod.destroy()

    logPeriod = Toplevel(root)
    logPeriod.title("Log Period")
    logPeriod.geometry('400x200')
    logPeriod.resizable(0,0) 

    logFrame = Frame(logPeriod)
    logFrame.pack(padx=5, pady=5)

    #Label -> DATE showcase
    dateTitleLabel=Label(logFrame, text="Date: ").grid(row=0, column=0) 
    dateLabel=Label(logFrame, text="2023-05-20").grid(row=0, column=2)

    #DropMenu
    flow=[flowEnum.Flow.LIGHT.value,flowEnum.Flow.MEDIUM.value,flowEnum.Flow.HEAVY.value]
    flowVar = StringVar()
    flowVar.set("Flow's intensity")
    flowDropMenu = OptionMenu(logFrame, flowVar, *flow, command=getFlowIntensity).grid(row=1, column=2)
    ###flowDropMenu.configure(width=16, height=2, font='Arial 12')

    #Input
    moodLabel = Label(logFrame, text="Mood: ").grid(row=2, column=0)
    moodEntry = Entry(logFrame)
    moodEntry.grid(row=2, column=2)
    symptomLabel = Label(logFrame, text="Symptom(s): ").grid(row=3, column=0)
    symptomEntry = Entry(logFrame)
    symptomEntry.grid(row=3, column=2)

    #Buttons
    doneButton = Button(logFrame, text="Done", command=saveData).grid(row=4, column=1, pady=10)
    
    logPeriod.mainloop()

#Frames
menuFrame = Frame(root)
menuFrame.pack(padx=5, pady=5)

#Buttons
logButton = Button(menuFrame, text='Log period', command=popup).grid(row=0, column=0)

#Label -> lists the latest 5 period logs with dates
n=1
for x in fillList():
    listLabel = Label(menuFrame, text=x).grid(row=n, column=0)
    n+=1

root.mainloop()