import random
import tkinter
 
 
def roll():
    lbl_result["text"] = str(random.randint(1, 6))
 
 
window = tkinter.Tk()
window.columnconfigure(0, minsize=150)
window.rowconfigure([0, 1], minsize=50)
 
btn_roll = tkinter.Button(text="Бросить кости", command=roll)
lbl_result = tkinter.Label()
 
btn_roll.grid(row=0, column=0, sticky="nsew")
lbl_result.grid(row=1, column=0)
 
window.mainloop()