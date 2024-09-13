from tkinter import *


def even_sum(n):
    even_n = [i for i in range(1,n) if i % 2 == 0]
    return sum(even_n)

def even():
    try:
        n = int(input_text.get())
        result_text.delete(0,END)
        result_text.insert(END,f"1부터 {n}까지 짝수의 합은 {even_sum(n)}입니다.")
    except ValueError:
        result_text.delete(0,END)
        result_text.insert(END,"유효한 숫자를 입력해 주세요.")

root = Tk()
root.geometry("500x300")
root.title("Even_sum")
root.resizable(False, False)

input_text = Entry(root)
input_text.pack()

Btn = Button(root, text="더하기",fg="green", command=even)
Btn.pack()

result_text = Text(root, width=50, height=5)
result_text.pack()

root.mainloop()