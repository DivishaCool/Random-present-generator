# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:31:16 2022

@author: 91977
"""
#library upload
from tkinter import *
import random
#end

#Tkinter window creation and configuration
root = Tk()
root.title("Random List")
root.geometry("900x600")
root.configure(bg = "#db4481")
#window end


#variables starting
random_number_list = Label(root)
random_number_sorted_list = Label(root)
list_of_items = Label(root)
# var end

#heading
heading = Label(root)
heading["text"] = "Random Present Generator"
heading.configure(font=("Comic Sans MS", 20, "italic" ,"bold"))
heading.configure(background = "#db4481" , )
# heading_end

#extra styling for rest of the elements on the window
list_of_items.configure(background = "#db4481")
random_number_list.configure(background="#db4481")


random_list = ["Bottle" , "Lunchbox" , "Pen Holder" , "Succulent Planter" , "Steam E-Gift Card" , "Cat Lamp" , "Children's Encyclopedia" , "Personalized photo frame"]
list_of_items["text"] = "Listed items"  + str(random_list)

def randomlist():
    random_number = random.randint(0,7)
    gift = random.choice(random_list)
    print(gift)
    random_number_list["text"] = "Put"+ " " + str(gift)+ " " + "in bag."
    random_list.sort()
    
    
btn = Button(root , text = "Which item to put in bag ?" , command = randomlist)   
btn.place(relx = 0.5 ,  rely = 0.4 , anchor = CENTER) 

random_number_list.place(relx = 0.5 ,  rely = 0.5 , anchor = CENTER) 
list_of_items.place(relx = 0.5 ,  rely = 0.3 , anchor = CENTER) 
heading.place(relx = 0.5 ,  rely = 0.2 , anchor = CENTER) 

root.mainloop()