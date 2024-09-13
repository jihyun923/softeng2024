import is_prime

import tkinter as tk
from tkinter import *

window = tk.Tk()


def primenum(num):
    return [i for i in range(2, num + 1) if is_prime(i)]


def gui_prime_list():
    n = int(input_num.get())
    result.delete(0, END)
    result.insert(0, f"{primenum(n)}")


def main():
    global input_num
    global result

    window.title("prime number list")
    window.resizable(width=False, height=False)

    frm_entry = tk.Frame(master=window)

    num_lbl = tk.Label(master=frm_entry, text="Enter number: ")
    input_num = tk.Entry(master=frm_entry, width=50)

    btn = tk.Button(master=frm_entry, text="\N{DOWNWARDS BLACK ARROW}", command=gui_prime_list)

    prime_lbl = tk.Label(master=frm_entry, text="prime num list:")
    result = tk.Entry(master=frm_entry, width=50)

    num_lbl.grid(row=0, column=0, padx=3, pady=5)
    input_num.grid(row=0, column=1, padx=3, pady=5)

    btn.grid(row=1, column=1)

    prime_lbl.grid(row=3, column=0, pady=5)
    result.grid(row=3, column=1, pady=5)

    frm_entry.grid(row=0, column=0, padx=10, pady=10)

    window.mainloop()


if __name__ == "__main__":
    main()