from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=80)
window.config(padx=20,pady=20)

entry_miles = Entry(width=15)
entry_miles.insert(END, string="enter Miles")
entry_miles.place(x=80,y=0)

label_miles = Label(text="Miles")
label_miles.place(x=150,y=0)

label_km = Label(text="is equal to")
label_km.place(x=18,y=30)

entry_km = Entry(width=15,state='readonly') 
entry_km.place(x=80,y=30)

label = Label(text="Km")
label.place(x=150,y=30)

#Buttons
def action():
    miles=float(entry_miles.get())
    km = miles * 1.60934
    entry_km.config(state=NORMAL)
    entry_km.delete(0, END)  # Clear any existing text
    entry_km.insert(END, f"{km:.2f}")
    entry_km.config(state='readonly')

button = Button(text="Calculate", command=action, width=10,height=1)
button.place(x=80,y=55)

window.mainloop()