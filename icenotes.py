import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = tk.Tk()
window.title("Notepad")
window.geometry("800x600")
entry = tk.Text(window, font="calibri")
entry.grid(row=0, column=1, sticky="nsew")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "r") as opening:
        text = opening.read()
        entry.insert(tk.END, text)
        window.title("Notepad " + filepath)
def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as saving:
        text = entry.get(1.0, tk.END)
        saving.write(text)
        window.title("Notepad " + filepath)
def clear():
    entry.delete(1.0, tk.END)
def new():
    import tkinter as tk
    from tkinter.filedialog import askopenfilename, asksaveasfilename
    window = tk.Tk ()
    window.title ("Notepad")
    window.geometry ("800x600")
    entry = tk.Text (window, font="comicsans")
    entry.grid (row=0, column=1, sticky="nsew")
    window.rowconfigure (0, minsize=800, weight=1)
    window.columnconfigure (1, minsize=800, weight=1)

    def open_file():
        filepath = askopenfilename (
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        with open (filepath, "r") as opening:
            text = opening.read ()
            entry.insert (tk.END, text)
            window.title ("Notepad " + filepath)

    def save_file():
        filepath = asksaveasfilename (
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        with open (filepath, "w") as saving:
            text = entry.get (1.0, tk.END)
            saving.write (text)
            window.title ("Notepad " + filepath)

    def clear():
        entry.delete (1.0, tk.END)

    fr_buttons = tk.Frame (window)
    fr_buttons.grid (row=0, column=0, sticky="ns")
    open_button = tk.Button (fr_buttons, text="Open", command=open_file)
    open_button.grid (row=0, column=1, sticky="ew", padx=5, pady=5)
    save_button = tk.Button (fr_buttons, text="Save", command=save_file)
    save_button.grid (row=1, column=1, sticky="ew", padx=5, pady=5)
    clear_button = tk.Button (fr_buttons, text="Clear", command=clear)
    clear_button.grid (row=2, column=1, sticky="ew", padx=5, pady=5)
    window.mainloop ()



fr_buttons = tk.Frame(window)
fr_buttons.grid(row=0, column=0, sticky="ns")
open_button = tk.Button(fr_buttons, text="Open", command=open_file)
open_button.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
save_button = tk.Button(fr_buttons, text="Save", command=save_file)
save_button.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
clear_button = tk.Button(fr_buttons, text="Clear", command=clear)
clear_button.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
new_button = tk.Button(fr_buttons, text="New", command=new)
new_button.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
window.mainloop()
