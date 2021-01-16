import tkinter as tk

root = tk.Tk()

#Label in Grid
'''
myLabel1 = tk.Label(root, text="Hello World")
myLabel2 = tk.Label(root, text="Ich bin Thomas Dörig")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

'''
#Entry 
e = tk.Entry(root, )
e.insert(0, "Name")
e.pack()
e.get()


#Button
def myClick():
    myLabel = tk.Label(root, text = e.get())
    myLabel.pack()

myButton = tk.Button(root, text ="Enter your Name", command = myClick) # state = DISABLED, pady=20 padx = 20 buttongrösse)
myButton.pack()



root.mainloop()