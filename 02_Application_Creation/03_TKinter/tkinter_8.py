import tkinter as tk

window = tk.Tk()

window.title("Screen location")
window.resizable(0,0)
window.geometry("500x500")
    
tk.Label(window, text="Label 1", fg="red").place(x=20, y=20)
tk.Label(window, text="Label 2", fg="green").place(x=200, y=200)
tk.Label(window, text="Label 3", fg="yellow").place(x=400, y=400)


tk.Label(window, text="Label 4", fg="white").place(x=2000, y=2000)

window.mainloop()