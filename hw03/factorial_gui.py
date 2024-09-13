from tkinter import *

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def carcul():
    try:
        n = int(input_text.get())
        if n < 0:
            result_text.delete(0,END)
            result_text.insert(END,"양수를 입력해 주세요.")
        else:
            # fact = factorial(n)
            result_text.delete(0, END)
            result_text.insert(END,f"{n}! = {factorial(n)}")
    except ValueError:
        result_text.delete(0,END)
        result_text.insert(END,"유효한 숫자를 입력해 주세요.")


root = Tk()
root.geometry("400x300")
root.title("factorial")
root.resizable(False, False)

input_text = Entry(root)
input_text.pack()

Btn = Button(root, text="FACTORIAL!", fg="green", command=carcul)
Btn.pack()

result_text = Text(root, height=10, width=40)
result_text.pack()

root.mainloop()