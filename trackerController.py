import trackerModel
from tkinter import *
import datetime

today = datetime.datetime.today()
formatToday = today.strftime("%Y-%m-%d")

def fillList():
    lst = []
    for dt in trackerModel.selectFiveDates():
        lst.append(dt)
    return lst

def saveData(fvar,entry1,entry2,var):
    def getEntryData(entry):
        return entry.get()
    
    flwdrp = getEntryData(fvar)
    mdntry = getEntryData(entry1)
    smptmntry = getEntryData(entry2)

    trackerModel.insertPeriod(formatToday)
    trackerModel.insertSymptoms(flwdrp,mdntry,smptmntry)

    var.destroy()
