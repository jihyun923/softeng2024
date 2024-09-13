from tkinter import *

def is_even(n):
    return n % 2 == 0

def check_even_odd():
    try:
        n = int(input_text.get())
        if is_even(n):
            result_text.delete(0, END)
            result_text.insert(END, f"{n}은(는) 짝수입니다.")
        else:
            result_text.delete(0, END)
            result_text.insert(END, f"{n}은(는) 홀수입니다.")
    except ValueError:
        result_text.delete(0, END)
        result_text.insert(END, "유효한 숫자를 입력해 주세요.")



root = Tk()
root.geometry("400x300+300+300")
root.title("짝수/홀수")
root.resizable(False, False)

input_text = Entry(root)
input_text.pack()

check_button = Button(root, text="짝수 or 홀수", fg="blue",command=check_even_odd)
check_button.pack()

result_text = Text(root, width=50, height=5)
result_text.pack()


root.mainloop()
