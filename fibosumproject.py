from tkinter import *

root = Tk()

root.title("Fibonacci")
root.geometry("400x400")

enter_num = Entry(root)
label_series = Label(root, text = "Fibonacci Series: ")
label_sum = Label(root, text = "Fibonicci Sum- ")

def Fibonacci():
    num = int(enter_num.get())
    first_no = 0
    second_no = 1
    sum = 0
    total = 0
    counter = 1
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        label_sum["text"] = "Fibonicci Sum- " + str(total)
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        total = total + sum

enter_num.pack()
btn = Button(root, text = "Show Fibonacci Series", command = Fibonacci)
btn.pack()
label_series.pack()
label_sum.pack()

root.mainloop()