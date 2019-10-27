import tkinter as tk
from tkinter import *
from tkinter import ttk

root=Tk()
mainframe = ttk.Frame(root, padding="10 10 17 17")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=4)
mainframe.rowconfigure(0, weight=1)

#taking the variables which will hold those value entered in boxes
name=tk.StringVar()
rollno=tk.StringVar()
regno=tk.StringVar()
#taking the variables which will hold those value entered in boxes gor grades
grade1=tk.StringVar()
grade2=tk.StringVar()
grade3=tk.StringVar()
grade4=tk.StringVar()
#for setting the variables which will hold those value entered in boxes for credit aquired
credits1=tk.IntVar()
credits2=tk.IntVar()
credits3=tk.IntVar()
credits4=tk.IntVar()

mmarks=150
maxmarks=tk.IntVar()
maxmarks.set(mmarks)
#taking the variables which will hold those value entered in boxes
totalCredit=tk.IntVar()
SGPA=tk.IntVar()
#defining the list for computation of the result
grades = [0,0,0,0]
credit = [0,0,0,0]
#defining the functions which will change the input grades to integer values
def getgrade(str1,int1):
    if str1=='A' or str1=='a':
        grades[int1]=10
    if str1=='B' or str1=='b':
        grades[int1]=9
    if str1=='C' or str1=='c':
        grades[int1]=8
    if str1=='D' or str1=='d':
        grades[int1]=7
    if str1=='E' or str1=='e':
        grades[int1]=6
    if str1=='F' or str1=='f':
        grades[int1]=5
    if str1=='P' or str1=='p':
        grades[int1]=2
#defining a function to calculate the credits for each subject
def getCredit(grade_value, sub_credit, int3):
    credit[int3]=grade_value*sub_credit
#this is the function or the method whioch will be used by the button
def button():    
    getgrade(grade1.get(),0)
    getgrade(grade2.get(),1)
    getgrade(grade3.get(),2)
    getgrade(grade4.get(),3)
    
    getCredit(grades[0],4,0)
    credits1.set(credit[0])
    getCredit(grades[1],4,1)
    credits2.set(credit[1])
    getCredit(grades[2],3,2)
    credits3.set(credit[2])
    getCredit(grades[3],4,3)
    credits4.set(credit[3])
    
    ttk.Entry(mainframe, width=7,textvariable=credits1).grid(column=5, row=5)
    ttk.Entry(mainframe, width=7,textvariable=credits2).grid(column=5, row=6)
    ttk.Entry(mainframe, width=7,textvariable=credits3).grid(column=5, row=7)
    ttk.Entry(mainframe, width=7,textvariable=credits4).grid(column=5, row=8)
    #calculation for the total credits
    totCre=credit[0]+credit[1]+credit[2]+credit[3]
    totalCredit.set(totCre)
    
    ttk.Entry(mainframe, width=7, textvariable=totalCredit).grid(column=5, row=9)
    #calculation for SGPA
    mmarks=maxmarks.get()
    sgpa=(totCre/mmarks)*10
    SGPA.set(sgpa)
    ttk.Entry(mainframe, width=7, textvariable=SGPA).grid(column=5, row=10)
    
ttk.Label(mainframe, text="MARSHEET").grid(column=3, row=1)
ttk.Label(mainframe, text="Name : ").grid(column=1, row=2)
ttk.Entry(mainframe, width=7, textvariable=name).grid(column=2, row=2)
ttk.Label(mainframe, text="Roll No.").grid(column=1, row=3)
ttk.Entry(mainframe, width=7, textvariable=rollno).grid(column=2, row=3)
ttk.Label(mainframe, text="Reg No.").grid(column=3, row=3)
ttk.Entry(mainframe, width=7, textvariable=regno).grid(column=4, row=3)
#the labeks for the sheet
ttk.Label(mainframe, text="Sl No.").grid(column=1, row=4)
ttk.Label(mainframe, text="1").grid(column=1, row=5)
ttk.Label(mainframe, text="2").grid(column=1, row=6)
ttk.Label(mainframe, text="3").grid(column=1, row=7)
ttk.Label(mainframe, text="4").grid(column=1, row=8)
#the labeks for the sheet
ttk.Label(mainframe, text="Sub Code  ").grid(column=2, row=4)
ttk.Label(mainframe, text="CS201").grid(column=2, row=5)
ttk.Label(mainframe, text="CS202").grid(column=2, row=6)
ttk.Label(mainframe, text="MA201").grid(column=2, row=7)
ttk.Label(mainframe, text="EC201").grid(column=2, row=8)
#the labeks for the sheet
ttk.Label(mainframe, text="Grade  ").grid(column=3, row=4)
ttk.Entry(mainframe, width=7, textvariable=grade1).grid(column=3, row=5)
ttk.Entry(mainframe, width=7, textvariable=grade2).grid(column=3, row=6)
ttk.Entry(mainframe, width=7, textvariable=grade3).grid(column=3, row=7)
ttk.Entry(mainframe, width=7, textvariable=grade4).grid(column=3, row=8)

#the labeks for the sheet
ttk.Label(mainframe, text="Sub Credit  ").grid(column=4, row=4)
ttk.Label(mainframe, text="4").grid(column=4, row=5)
ttk.Label(mainframe, text="4").grid(column=4, row=6)
ttk.Label(mainframe, text="3").grid(column=4, row=7)
ttk.Label(mainframe, text="4").grid(column=4, row=8)
ttk.Label(mainframe, text="Total Credit Obtained").grid(column=4, row=9)
ttk.Label(mainframe, text="SGPA").grid(column=4, row=10)
ttk.Button(mainframe, text="Get Result", command=button).grid(column=4, row=11)

ttk.Label(mainframe, text="Credit Obtained").grid(column=5, row=4)

ttk.Label(mainframe, text="Maximum Marks").grid(column=2, row=12)
ttk.Entry(mainframe, width=7, textvariable=maxmarks).grid(column=3, row=12)

root.mainloop()