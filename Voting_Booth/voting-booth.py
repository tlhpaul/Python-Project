"""Name: Tse-Lun Hsu, Student ID: 61737979"""
"""Program Description: Voting simulator for the next president of USA."""

from tkinter import *

voting = Tk()
frame1 = Frame(voting)
frame1.pack(side="top")
Label(frame1, text = "Vote for your next president of USA!", fg = "red").pack()
winner = "Tied!"

def bigger(a, b, c, d):
    """Determining who is winning or it is tied between at least two candidates."""
    lst = [a["text"] , b["text"] , c["text"] , d["text"]]
    if a["text"] == max (lst) != max([b["text"] , c["text"] , d["text"]]):
        return "Hillary Clinton"
    elif b["text"] == max (lst) != max([a["text"] , c["text"] , d["text"]]):
        return "Donald Trump"
    elif c["text"] == max (lst) != max([a["text"] , b["text"] , d["text"]]):
        return "Bernie Sanders"
    elif d["text"] == max (lst) != max([a["text"] , b["text"] , c["text"]]):
        return "Ted Cruz"
    else:
        return "Tied!"

def clicked1():
    """When button Hillary Clinton is clicked"""
    l1["text"] = l1["text"]+1
    winner = bigger(l1, l2, l3, l4)
    l5["text"] = "Winner so far: "+str(winner)

def clicked2():
    """When button Donald Trump is clicked"""
    l2["text"] = l2["text"]+1
    winner = bigger(l1, l2, l3, l4)
    l5["text"] = "Winner so far: "+str(winner)
    
def clicked3():
    """When button Bernie Sanders is clicked"""
    l3["text"] = l3["text"]+1
    winner = bigger(l1, l2, l3, l4)
    l5["text"] = "Winner so far: "+str(winner)
    
def clicked4():
    """When button Ted Cruz is clicked"""
    l4["text"] = l4["text"]+1
    winner = bigger(l1, l2, l3, l4)
    l5["text"] = "Winner so far: "+str(winner)
    
frame2 = Frame(voting, bg = "light gray")
frame2.pack(side="top")
Label(frame2, text = "CANDIDATE", width = 20, bg = "light gray").grid(row=0, column = 0, sticky = W+E, padx = 5, pady=5)
Label(frame2, text = "VOTES",width = 20, bg = "light gray").grid(row=0, column = 1, sticky = W + E, padx = 5,  pady=5)
l1 = Label(frame2, text = 0, bg = "light gray")
l1.grid(row=1, column = 1, sticky = W + E)
Button(frame2, text = "Hillary Clinton", command = clicked1, width = 20, fg = "blue").grid(row=1, column = 0, sticky = W + E, padx = 5,  pady=5)
l2 = Label(frame2, text = 0, bg = "light gray")
l2.grid(row=2, column = 1, sticky = W + E)
Button(frame2, text = "Donald Trump", command = clicked2, width = 20).grid(row=2, column = 0, sticky = W + E, padx = 5,  pady=5 )
l3 = Label(frame2, text = 0, bg = "light gray")
l3.grid(row=3, column = 1, sticky = W + E)
Button(frame2, text = "Bernie Sanders", command = clicked3, width = 20).grid(row=3, column = 0, sticky = W + E, padx = 5,  pady=5)
l4 = Label(frame2, text = 0, bg = "light gray")
l4.grid(row=4, column = 1, sticky = W + E)
Button(frame2, text = "Ted Cruz", command = clicked4, width = 20).grid(row=4, column = 0, sticky = W + E, padx = 5,  pady=5 ) 
l5 = Label(frame2, text = "Winner so far: "+ str(winner), width = 20, bg = "light gray")
l5.grid(row = 5, sticky = W + E)

mainloop()
