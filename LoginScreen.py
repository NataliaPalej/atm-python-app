from tkinter import *
import tkinter as tk


class LoginScreen:
    def __init__(self):
        print("Hello")


# TODO: Sub-Menu for CreateNewAccount
# TODO: GUI accNo, accPIN, buttons 0-9 display

# ===== Methods ===== #
def exit_app():
    exit()


def clear():
    entry_focused = window.focus_get()
    entry_focused = str(entry_focused)
    if entry_focused == ".!entry":
        accNo_entry.delete(0, END)
        accNo_entry.insert(END, "")
    elif entry_focused == ".!entry2":
        PIN_entry.delete(0, END)
        PIN_entry.insert(END, "")
    else:
        print("Nothing Selected")


def button_handler(number):
    entry_focused = window.focus_get()
    entry_focused = str(entry_focused)
    if entry_focused == ".!entry":
        accNo_entry.insert(END, number)
    elif entry_focused == ".!entry2":
        PIN_entry.insert(END, number)
    else:
        print("Nothing Selected")


# ===== GUI ===== #
window = tk.Tk()
window.geometry("600x600")
window.title("ATM - Natalia Palej A00279259")
window.resizable(False, False)

label = Label(window, text="A T M", fg="black", font=("arial", 30, "bold"))
label.grid(row=0, column=0, columnspan=2, pady=20, padx=250)
# label2 = Label(window, text="Automated Teller Machine", fg="black", font=("arial", 15, "bold"))
# label2.grid(row=1, column=0, columnspan=2, padx=180)

label3 = Label(window, text="ACC:", fg="black", font=("arial", 20, "bold"), )
label3.place(x=80, y=120)
accNo_entry = Entry(window, font="Arial 20")
accNo_entry.insert(END, '')
accNo_entry.place(x=160, y=120, width=300, height=40)
accNo_entry.focus()

label4 = Label(window, text="PIN:", fg="black", font=("arial", 20, "bold"))
label4.place(x=80, y=180)
# Show *** to hide PIN input
PIN_entry = Entry(window, font="Arial 20", show="*")
PIN_entry.insert(END, '')
PIN_entry.place(x=160, y=180, width=300, height=40)

btn7 = tk.Button(text="7", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                 command=lambda: button_handler(7))
btn7.place(x=120, y=227)
btn4 = tk.Button(text="4", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                 command=lambda: button_handler(4))
btn4.place(x=120, y=290)
btn1 = tk.Button(text="1", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                 command=lambda: button_handler(1))
btn1.place(x=120, y=352)
login_btn = tk.Button(text="LOGIN", font=('Arial', 16, 'bold'), height=2, width=8, bg="limegreen")
login_btn.place(x=120, y=418)

btn8 = tk.Button(text="8", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                 command=lambda: button_handler(8))
btn8.place(x=235, y=227)
btn5 = tk.Button(text="5", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                 command=lambda: button_handler(5))
btn5.place(x=235, y=290)
btn2 = tk.Button(text="2", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                 command=lambda: button_handler(2))
btn2.place(x=235, y=352)
btn0 = tk.Button(text="0", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                 command=lambda: button_handler(0))
btn0.place(x=235, y=418)

btn9 = tk.Button(text="9", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                 command=lambda: button_handler(9))
btn9.place(x=350, y=227)
btn6 = tk.Button(text="6", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                 command=lambda: button_handler(6))
btn6.place(x=350, y=290)
btn3 = tk.Button(text="3", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                 command=lambda: button_handler(3))
btn3.place(x=350, y=352)
clearbtn = tk.Button(text="CANCEL", font=('Arial', 16, 'bold'), height=2, width=8, bg="red", command=clear)
clearbtn.place(x=350, y=418)

# exit button
exit_btn = tk.Button(text="EXIT", width=15, font=('Arial', 16, 'bold'), height=2, bg="gray", fg="black",
                     command=exit_app)
exit_btn.place(x=15, y=520)

window.mainloop()
