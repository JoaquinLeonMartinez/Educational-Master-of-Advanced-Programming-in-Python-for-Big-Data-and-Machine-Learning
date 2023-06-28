import tkinter as tk

window = tk.Tk()

window.title("Tkinter app")
window.resizable(0,0)
window.geometry("350x350")

def users_function():
    print("Name:", e1.get(), "Surname", e2.get())
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    
tk.Label(window, text="Enter name and surname").grid(row=1,column=0)
tk.Label(window, text="Name").grid(row=2,column=0)
tk.Label(window, text="Surname").grid(row=3,column=0)

e1 = tk.Entry(window)
e1.insert(0, "")
e1.grid(row=2, column=1)

e2 = tk.Entry(window)
e2.insert(0, "")
e2.grid(row=3, column=1)

tk.Button(window, text="Show", fg="white", 
          bg="blue", command=users_function).grid(row=4, column=0)

window.mainloop()