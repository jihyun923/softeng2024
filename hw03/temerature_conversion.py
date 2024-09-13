import tkinter as tk
from tkinter import ttk
from tkinter import *

window = tk.Tk()


def trans_temp(tp, temp):
    if tp == "f":
        return (temp * 1.8) + 32
    elif tp == "c":
        return (temp - 32) / 1.8


def gui_trans():
    n = float(input_num.get())
    unit = tp.get()
    result.delete(0, END)
    if unit == "f":
        result.insert(0, f"{n}f => {trans_temp(unit, n):.1f}c")
    else:
        result.insert(0, f"{n}c => {trans_temp(unit, n):.1f}f")


def main():
    global input_num
    global result
    global tp

    window.title("Temperature Conversion")
    window.resizable(width=False, height=False)

    frm_entry = tk.Frame(master=window)

    tp_lbl = tk.Label(master=frm_entry, text="Type: ")
    tp = ttk.Combobox(master=frm_entry, width=10, height=10, values=["f", "c"])

    num_lbl = tk.Label(master=frm_entry, text="Temperature: ")
    input_num = tk.Entry(master=frm_entry, width=50)

    btn = tk.Button(master=frm_entry, text="\N{DOWNWARDS BLACK ARROW}", command=gui_trans)

    prime_lbl = tk.Label(master=frm_entry, text="Result:")
    result = tk.Entry(master=frm_entry, width=50)

    tp_lbl.grid(row=0, column=0, padx=3, pady=5)
    tp.grid(row=0, column=1, padx=3, pady=5)

    tp.current(0)

    num_lbl.grid(row=1, column=0, pady=5)
    input_num.grid(row=1, column=1, pady=5)

    btn.grid(row=2, column=1, pady=5)

    prime_lbl.grid(row=3, column=0, pady=5)
    result.grid(row=3, column=1, pady=5)

    frm_entry.grid(row=0, column=0, padx=10, pady=10)

    window.mainloop()


if __name__ == "__main__":
    main()