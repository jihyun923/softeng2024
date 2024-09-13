import tkinter as tk
from tkinter import *

window = tk.Tk()


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def gui_prime():
    try:
        n = int(input_num.get())
        if is_prime(n):
            result.delete(0, END)
            result.insert(0, f"{n}은 소수가 맞습니다.")
        else:
            result.delete(0, END)
            result.insert(0,f"{n}은 소수가 아닙니다.")
    except ValueError:
        result.delete(0,END)
        result.insert(0,"유효한 숫자를 입력해 주세요.")




def main():
    global input_num
    global result

    window.title("is prime")
    window.resizable(width=False, height=False)

    frm_entry = tk.Frame(master=window)

    num_lbl = tk.Label(master=frm_entry, text="Enter number: ")
    input_num = tk.Entry(master=frm_entry, width=50)

    btn = tk.Button(master=frm_entry, text="\N{DOWNWARDS BLACK ARROW}", command=gui_prime)

    prime_lbl = tk.Label(master=frm_entry, text="Check prime num:")
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