import tkinter as tk

window = tk.Tk()

window.title("First Tkinter app")
window.resizable(0,0)
window.geometry("350x350")
window.config(bg="blue")

click = 0

def function_click():
    global click
    click += 1
    print("Se ha pulsado:", click, "veces")
    
button = tk.Button(window, fg="white", bg="blue", text="Click here!",
                   width=10, height=5, command=function_click)

button.pack()

window.mainloop()