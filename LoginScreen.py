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


# ===== GUI ===== #
window = tk.Tk()
window.geometry("600x600")
window.title("ATM")
window.resizable(False, False)

login_btn = tk.Button(text="LOGIN", font=('Arial', 16, 'bold'), height=2, width=15, bg="limegreen")
login_btn.place(x=80, y=380)

cancel_btn = tk.Button(text="CANCEL", font=('Arial', 16, 'bold'), height=2, width=15, bg="red")
cancel_btn.place(x=320, y=380)

# exit button
exit_btn = tk.Button(text="EXIT", width=15, font=('Arial', 16, 'bold'), height=2, bg="gray", fg="black",
                     command=exit_app)
exit_btn.place(x=200, y=500)

window.mainloop()
