#Author: Wen Bin Zhang
#Date: April 10, 2020
#Purpose: Simple Calendar
#==========================================================
from tkinter import *
from datetime import datetime
dateWindow = Tk()
dateWindow.geometry('485x175')
dateWindow.title("Simple Calendar")
dateWindow.resizable(0, 0)

calendar = Text(dateWindow, height = 8, width = 42, bg = "lightgrey", fg = "black", state = 'disabled')
calendar.place(x = 0, y = 40)

#Author: Wen Bin Zhang
#Date: April 10, 2020
#Purpose: A Date/Calendar object for use
#Date Elements:
#   day - integer (1 - maxDay)
#   month - integer (1 - 12)
#   year - integer (1600 - 2200)
#Methods:
#   init
#   str
#   returnMonthName
#   returnLeapYear
#   returnMaxDay
#   calcZeller
#   returnDayName
#   calcValid
#   getDate
#   displayCalendar
#   getPositiveInteger
#   setMonth
#   setYear
#   setDay
#   refresh
#   dayOfYear
#==================================================
class Date:
    def __init__(self, day = 1, month = 2, year = 2019):
        self.intDay = day
        self.intMonth = month
        self.intYear = year
        
#   Author: Wen Bin Zhang
#   Date: April 10, 2020
#   Purpose: Handle print statements
#   Inputs/Parameters: N/A
#   Outputs/Returns: the whole date in string.
#   Dependencies: returnDayName(), returnMonthName()
#==================================================
    def __str__(self):
        return self.returnDayName() + ", " + self.returnMonthName() + " " + str(self.intDay) + ", " + str(self.intYear)
    
#   Author: Wen Bin Zhang
#   Date: April 10, 2020
#   Purpose: Convert month integers to month names
#   Inputs/Parameters: N/A
#   Outputs/Returns: strMonth
#   Dependencies: None
#======================================================
    def returnMonthName(self):
        if self.intMonth == 1:
            strMonth = "January"
        elif self.intMonth == 2:
            strMonth = "February"
        elif self.intMonth == 3:
            strMonth = "March"
        elif self.intMonth == 4:
            strMonth = "April"
        elif self.intMonth == 5:
            strMonth = "May"
        elif self.intMonth == 6:
            strMonth = "June"
        elif self.intMonth == 7:
            strMonth = "July"
        elif self.intMonth == 8:
            strMonth = "August"
        elif self.intMonth == 9:
            strMonth = "September"
        elif self.intMonth == 10:
            strMonth = "October"
        elif self.intMonth == 11:
            strMonth = "Novemeber"
        elif self.intMonth == 12:
            strMonth = "December"
        return strMonth

#   Author: Wen Bin Zhang
#   Date: April 10, 2020
#   Purpose: Calculates if the year is a leap year
#   Inputs/Parameters: N/A
#   Outputs/Returns: leapYear
#   Dependencies: None
#=====================================================
    def returnLeapYear(self):
        if self.intYear % 4 == 0 and self.intYear % 100 != 0:
            leapYear = True
        elif self.intYear % 400 == 0 and self.intYear % 100 == 0:
            leapYear = True
        else:
            leapYear = False
        return leapYear

#   Author: Wen Bin Zhang
#   Date: April 10, 2020
#   Purpose: Indicate the max day in the month
#   Inputs/Parameters: N/A
#   Outputs/Returns: maxDay
#   Dependencies: returnLeapYear()
#=====================================================
    def returnMaxDay(self):
        if self.intMonth == 1:
            maxDay = 31
        elif self.intMonth == 2:
            if self.returnLeapYear():
                maxDay = 29
            else:
                maxDay = 28
        elif self.intMonth == 3:
            maxDay = 31
        elif self.intMonth == 4:
            maxDay = 30
        elif self.intMonth == 5:
            maxDay = 31
        elif self.intMonth == 6:
            maxDay = 30
        elif self.intMonth == 7:
            maxDay = 31
        elif self.intMonth == 8:
            maxDay = 31
        elif self.intMonth == 9:
            maxDay = 30
        elif self.intMonth == 10:
            maxDay = 31
        elif self.intMonth == 11:
            maxDay = 30
        elif self.intMonth == 12:
            maxDay = 31
        return maxDay
        
#   Author: Wen Bin Zhang
#   Date: April 10, 2020
#   Purpose: Calculate the day of the week of the date
#   Inputs/Parameters: N/A
#   Outputs/Returns: zeller - the day of the week
#   Dependencies: None
#=====================================================
    def calcZeller(self):
        m = self.intMonth - 2
        y = self.intYear
        if m <= 0:
            m = m + 12
            y = y - 1
        p = y // 100
        r = y % 100
        return (self.intDay + (26 * m - 2) // 10 + r + r // 4 + p // 4 + 5 * p) % 7

#   Author: Wen Bin Zhang
#   Date: April 10, 2020
#   Purpose: Returns the day name
#   Inputs/Parameters: N/A
#   Outputs/Returns: strDay - day in string
#   Dependencies: calcZeller()
#=====================================================
    def returnDayName(self):
        if self.calcZeller() == 0:
            strDay = "Sunday"
        elif self.calcZeller() == 1:
            strDay = "Monday"
        elif self.calcZeller() == 2:
            strDay = "Tuesday"
        elif self.calcZeller() == 3:
            strDay = "Wednesday"
        elif self.calcZeller() == 4:
            strDay = "Thursday"
        elif self.calcZeller() == 5:
            strDay = "Friday"
        elif self.calcZeller() == 6:
            strDay = "Saturday"
        return strDay

#   Author: Wen Bin Zhang
#   Date: April 10, 2020
#   Purpose: Checks if the data elements are valid
#   Inputs/Parameters: N/A
#   Outputs/Returns: valid - validated boolean
#   Dependencies: returnMaxDay()
#=====================================================
    def calcValid(self):
        if ( self.intDay >= 1 and self.intDay <= self.returnMaxDay() ) and ( self.intMonth >= 1 and self.intMonth <= 12 ) and ( self.intYear >= 1600 and self.intYear <= 2200 ) \
        and str(self.intDay).isdigit() == True and str(self.intMonth).isdigit() == True and str(self.intYear).isdigit() == True:
            valid = True
        else:
            valid = False
        return valid
        
#   Author: Wen Bin Zhang
#   Date: April 10, 2020
#   Purpose: Get the input from user
#   Inputs/Parameters: N/A
#   Outputs/Returns: the user input values
#   Dependencies: getPositiveInteger(), returnMaxDay()
#==================================================
    def getDate(self):
        self.intDay = datetime.now().day
        self.intMonth = datetime.now().month
        self.intYear = datetime.now().year
        # self.intYear = self.getPositiveInteger("Enter the year in positive integers: ", 1600, 2200)
        # self.intMonth = self.getPositiveInteger("Enter the month in positive integers: ", 1, 12)
        # self.intDay = self.getPositiveInteger("Enter the day in positive integers: ", 1, self.returnMaxDay())
        # while self.calcValid() == False:
        #     print("Error: Re-enter VALID values. Values provided is not valid")
        #     print("Re-enter valid year: ")
        #     self.intYear = getPositiveInteger("Enter the year in positive integers: ", 1600, 2200)
        #     print("Re-enter valid month: ")
        #     self.intMonth = getPositiveInteger("Enter the year in positive integers: ", 1, 12)
        #     print("Re-enter valid day: ")
        #     self.intDay = getPositiveInteger("Enter the day in positive integers: ", 1, self.returnMaxDay())
        # print("GUI Calendar has been made/edited.")

#   Author: Wen Bin Zhang
#   Date: April 10, 2020
#   Purpose: Displays the calendar for the date
#   Inputs/Parameters: N/A
#   Outputs/Returns: A whole calender
#   Dependencies: returnMaxDay(), calcZeller(), setDay(), Tkinter
#==================================================
    def displayCalendar(self):
        calendar.config(state = 'normal')
        calendar.delete(1.0, 'end')
        temp = self.intDay
        self.intDay = 1
        count= 0
        calendar.insert(INSERT, "Sun   Mon   Tue   Wed   Thu   Fri   Sat")
        for space in range(1, self.calcZeller() + 1):
            calendar.insert(INSERT, 6 * " ")
            count += 1
        calendar.insert(INSERT, "   ")
        
        for days in range (1, self.returnMaxDay() + 1):
            if temp == days:
                calendar.insert(INSERT, "%3s" % days + " ", ('main'))
                calendar.insert(INSERT, "  ")
                calendar.tag_configure('main', foreground="black", background="white")
            else:
                calendar.insert(INSERT, "%3s" % days + "   ")
            if (days + count) % 7 == 0:
                calendar.insert(INSERT, "\n")
        calendar.config(state = 'disabled')
        self.setDay(temp)
        
#   Author: Wen Bin Zhang
#   Date: March 3, 2020
#   Purpose: Check for positive integer and see if value is in range.
#   Inputs/Parameters: prompt - Dynamic Prompt to use with the user question
#                      low - Low Boundary
#                      high - High Boundary
#   Outputs/Returns: Checked integers
#   Dependencies: None
#==============================================================================
    def getPositiveInteger(self, prompt = "Enter a positive integer: ", low = 0, high = 100): #Receives a prompt along with a low to high boundary
            strInput = input(prompt) #Ask question
            while (not strInput.isdigit()) or (not int(strInput) in range(low, high + 1)): 
                if not strInput.isdigit():
                    print("Error: Value is not in digits")
                elif not int(strInput) in range(low, high + 1):
                    print("Error: Value is not in range", low, " to ", high)
                strInput = input(prompt)
            inputValue = int(strInput)
            return inputValue
        
#   Author: Wen Bin Zhang
#   Date: April 10, 2020
#   Purpose: Sets the month
#   Inputs/Parameters:
#                   value - the value to be set
#                   counter - boolean value to check if the setting is for counter purpose
#   Outputs/Returns: a month that is set to the value
#   Dependencies: returnMaxDay()
#==================================================              
    def setMonth(self, value, counter = False):
        if value < 1:
            value = 12
        elif value > 12:
            value = 1
        self.intMonth = value
        if counter == False and self.intDay > self.returnMaxDay():
            self.intDay = self.returnMaxDay()
#   Author: Wen Bin Zhang
#   Date: April 10, 2020
#   Purpose: Sets the year
#   Inputs/Parameters:
#                   value - the value to be set
#   Outputs/Returns: year that is set to the value
#   Dependencies: returnMaxDay()
#==================================================    
    def setYear(self, value):
        if value < 1600:
            value = 2200
        elif value > 2200:
            value = 1600
        self.intYear = value
        if self.intDay > self.returnMaxDay():
            self.intDay = self.returnMaxDay()
#   Author: Wen Bin Zhang
#   Date: April 10, 2020
#   Purpose: Sets the day
#   Inputs/Parameters:
#                   value - the value to be set
#   Outputs/Returns: day that is set to the value
#   Dependencies: returnMaxDay()
#==================================================    
    def setDay(self, value):
        if value < 1:
            value = self.returnMaxDay()
        elif value > self.returnMaxDay():
            value = 1
        self.intDay = value

#   Author: Wen Bin Zhang
#   Date: April 10, 2020
#   Purpose: refreshs the gui labels
#   Inputs/Parameters: date
#   Outputs/Returns: refreshed gui variables
#   Dependencies: __str__(), displayCalendar(), dayOfYear()
#==================================================    
    def refresh(self):
        yearValue.set(str(self.intYear))
        monthValue.set(str(self.intMonth))
        dayValue.set(str(self.intDay))
        currentDate.set(self.__str__())
        self.displayCalendar()
        dayOfYear.set("Day of Year: " + str(self.dayOfYear()))

#   Author: Wen Bin Zhang
#   Date: April 10, 2020
#   Purpose: Calculates the day of year in the year
#   Inputs/Parameters: date
#   Outputs/Returns: the total day of year
#   Dependencies: setMonth(), returnMaxDay()
#==================================================    
    def dayOfYear(self):
        totalDay = 0
        temp = self.intMonth
        for month in range (1, temp):
            self.setMonth(month, counter = True)
            totalDay += self.returnMaxDay()
        self.setMonth(temp)
        return totalDay + self.intDay



#Textbox
calendar = Text(dateWindow, height = 8, width = 42, bg = "lightgrey", fg = "black", state = 'disabled')
calendar.place(x = 0, y = 40)

#Main
date = Date()
date.getDate()

#Variables
dayValue = StringVar()
monthValue = StringVar()
yearValue = StringVar()
currentDate = StringVar()
dayOfYear = StringVar()
date.refresh()

#Labels
dateLabel = Label(dateWindow, textvariable = currentDate, bg = "black", fg = "white", font='Helvetica 8 bold', width = 48).place(x = 0, y = 0)
dayOfYearLabel = Label(dateWindow, textvariable = dayOfYear, bg = "black", fg = "white", font='Helvetica 8 bold', width = 48).place(x = 0, y = 20)

#Frame
controlFrame = LabelFrame(dateWindow, text = "Date Control", padx = 10, pady = 1, bg = "silver")

#Labels in the Frame
yearLabelMain = Label(controlFrame, text = "Year: ", bg = "silver").grid(row = 1, column = 1)
yearButtonLeft = Button(controlFrame, text = "<", command = lambda:[date.setYear(date.intYear - 1), date.refresh()]).grid(row = 1, column = 2)
yearButtonRight = Button(controlFrame, text = ">", command = lambda:[date.setYear(date.intYear + 1), date.refresh()]).grid(row = 1, column = 4)
yearLabel = Label(controlFrame, textvariable = yearValue, bg = "silver").grid(row = 1, column = 3)

monthLabelMain = Label(controlFrame, text = "Month: ", bg = "silver").grid(row = 2, column = 1)
monthButtonLeft = Button(controlFrame, text = "<", command = lambda:[date.setMonth(date.intMonth - 1), date.refresh()]).grid(row = 2, column = 2)
monthButtonRight = Button(controlFrame, text = ">", command = lambda:[date.setMonth(date.intMonth + 1), date.refresh()]).grid(row = 2, column = 4)
monthLabel = Label(controlFrame, textvariable = monthValue, bg = "silver").grid(row = 2, column = 3)

dayLabelMain = Label(controlFrame, text = "Day: ", bg = "silver").grid(row = 3, column = 1)
dayButtonLeft = Button(controlFrame, text = "<", command = lambda:[date.setDay(date.intDay - 1), date.refresh()]).grid(row = 3, column = 2)
dayButtonRight = Button(controlFrame, text = ">", command = lambda:[date.setDay(date.intDay + 1), date.refresh()]).grid(row = 3, column = 4)
dayLabel = Label(controlFrame, textvariable = dayValue, bg = "silver").grid(row = 3, column = 3)

#Exit Button
exitButton = Button(dateWindow, text = "EXIT", width = 19, command = lambda:dateWindow.destroy()).place(x = 341, y = 145)
#Placing the Frame
controlFrame.place(x = 340, y = 0)

mainloop()
