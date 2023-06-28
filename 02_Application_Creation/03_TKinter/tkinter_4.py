import tkinter as tk

window = tk.Tk()

window.title("Tkinter app")
window.resizable(0,0)
window.geometry("350x350")

def option_function():
    print("Variable 1:", v1.get(), "Variable 2:", v2.get(),
          "Variable 3:", v3.get())

label = tk.Label(window, text="Choose your variable")
label.grid(row=0, column=0)

v1 = tk.IntVar()
v2 = tk.IntVar()
v3 = tk.IntVar()

tk.Checkbutton(window, text="Option 1", variable=v1).grid(row=1, column=0)
tk.Checkbutton(window, text="Option 2", variable=v2).grid(row=1, column=1)
tk.Checkbutton(window, text="Option 3", variable=v3).grid(row=1, column=2)

tk.Button(window, text="Show choosen options",
          bg="red", fg="white", command=option_function).grid(row=1,column=3)


window.mainloop()