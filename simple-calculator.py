import tkinter as tk

def on_click(char):
    current = entry.get()
    if char == 'C':
        entry.delete(0, tk.END)
    elif char == '=':
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, char)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("240x300")

# Entry field for display
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


root.mainloop()   