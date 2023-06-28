import tkinter as tk

window = tk.Tk()
window.title("Destroy")
window.resizable(0,0)
window.geometry("350x350")

def quit():
    window.quit()
    window.destroy()
    
    
button = tk.Button(window, fg="white", bg="blue", text="Close",
                   width=10, height=5, command=quit)
button.pack(side=tk.BOTTOM)

window.mainloop()