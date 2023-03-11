from tkinter import *
import tkinter as tk


# TODO: Sub-Menu for CreateNewAccount
# TODO: GUI accNo, accPIN, buttons 0-9 display
# TODO: Login, Exit buttons

# ===== Methods ===== #
def exit_app():
    exit()


# ===== GUI ===== #
window = tk.Tk()
window.geometry("600x600")
window.title("ATM")
window.resizable(False, False)

login_btn = tk.Button(text="Login", font=('Arial', 16, 'bold'), height=2, width=15, takefocus=1)
login_btn.place(x=100, y=380)

# exit button
exit_btn = tk.Button(text="Exit", width=15, font=('Arial', 16, 'bold'), height=2, bg="gray", fg="black",
                        command=exit_app)
exit_btn.place(x=200, y=500)

window.mainloop()
