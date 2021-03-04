#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Calculator for IMR & CMR

import tkinter    

window=tkinter.Tk()
window.geometry("400x350")
window.resizable(0,0)

#window title
window.title("Pandemic Analytics Engine")

tkvar1 = tkinter.IntVar()
variable=tkinter.StringVar()
inft=tkinter.StringVar()
recov=tkinter.StringVar()
dead=tkinter.StringVar()

#labelling the window
label=tkinter.Label(window,text="Pandemic Analyzer !",fg="purple3",font=("arial rounded MT bold",16)).grid(row=0,column=0,sticky='W')


#State drop-down button
list1 = ["A&N","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhatisgarh","Dadra & Nagar Haveli","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","J&K","Jharkhand","Karnataka","Kerala","Ladakh","Lakshdweep","Maharashtra","Manipur","Meghalaya","Mizoram","Madhya Pradesh","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telengana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]


variable.set(list1[0]) #default
popupMenu=tkinter.OptionMenu(window,variable,*list1).grid(row = 2, column =1)

tk=tkinter.Label(window,text="Select State",fg="palegreen3",font=("arial rounded MT bold",16)).grid(row = 2, column = 0,sticky='W')


def change_option():
    print( variable.get() )
    variable.trace('w',change_option) # to change the drop-down


               
#labelling buttons

tkinter.Label(window,text="Infected",fg="goldenrod",font=("arial rounded MT bold",16)).grid(row=4 ,column=0,sticky='W')
tkinter.Label(window,text="Recovered",fg="turquoise",font=("arial rounded MT bold",16)).grid(row=5,column=0,sticky='W')             
tkinter.Label(window,text="Deceased",fg="red",font=("arial rounded MT bold",16)).grid(row=7,column=0,sticky='W')
              

tkinter.Entry(window,width=25,textvariable=inft, bg="gold").grid(row=4,column=1,sticky='W')
tkinter.Entry(window,width=25,textvariable=recov, bg="cyan").grid(row=5,column=1,sticky='W')
tkinter.Entry(window,width=25,textvariable=dead, bg="tomato").grid(row=7,column=1,sticky='W')
 
              
#Infected Fatality Ratio
def ifr():
    infected = int(inft.get())
    recovered = int(recov.get())
    deceased = int(dead.get())
    
    Ans1 = (int(dead.get()) / int(inft.get()))*100
    tkvar1.set(Ans1)
    tkinter.Entry(window, text = "%s" %(tkvar1)).grid(row =12, column =1)

    
#Crude Mortality Ratio   
def cmr():
    infected = int(inft.get())
    recovered = int(recov.get())
    deceased = int(dead.get())
    
    total = infected + recovered + deceased
    
    Ans2 = (deceased/total)*100
    tkvar1.set(Ans2)
    tkinter.Entry(window, text = "%s" %(tkvar1)).grid(row =12, column =1)

        
tkinter.Button(window,text="IFR",width=12,fg="black",bg="white",activebackground="gainsboro", command=ifr).grid(row=11,column=0,sticky='E')   

tkinter.Button(window,text="CMR",width=12,fg="black",bg="white",activebackground="gainsboro", command=cmr).grid(row=11,column=1,sticky='E')

#Calculated Value


tkinter.Label(window,text="Value",width=12,fg="gray35",font=("arial rounded MT bold",16)).grid(row=12,column=0,sticky='W')
tkinter.Entry(window,bg="ivory2").grid(row=12,column=1)


window.mainloop()


# In[ ]:




