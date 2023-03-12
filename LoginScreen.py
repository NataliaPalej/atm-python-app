from tkinter import *
import tkinter as tk
from tkinter import Menu
from Bank import Bank
from NewAccount import NewAccount


def exit_app():
    exit()


def new_account():
    NewAccount()


class LoginScreen:
    def __init__(self):
        # initialize empty dictionary to store customer data from file
        self.customers = {}
        # read data from file
        self.read_data()

        # ===== GUI ===== #
        self.window = tk.Tk()
        self.window.geometry("600x600")
        self.window.title("ATM - Natalia Palej A00279259")
        self.window.resizable(False, False)

        # ==== SUB MENU ==== #
        submenu = Menu(self.window)
        self.window.config(menu=submenu)
        new_user = Menu(submenu)
        # name the submenu
        submenu.add_cascade(label="OPTIONS", menu=new_user)
        # add option in submenu
        new_user.add_command(
            label="CREATE NEW ACCOUNT", command=new_account)

        label = Label(self.window, text="A T M", fg="black", font=("arial", 30, "bold"))
        label.grid(row=0, column=0, columnspan=2, pady=20, padx=250)

        label3 = Label(self.window, text="ACC:", fg="black", font=("arial", 20, "bold"), )
        label3.place(x=80, y=120)
        self.accNo_entry = Entry(self.window, font="Arial 20")
        self.accNo_entry.insert(END, '')
        self.accNo_entry.place(x=160, y=120, width=300, height=40)
        self.accNo_entry.focus()

        label4 = Label(self.window, text="PIN:", fg="black", font=("arial", 20, "bold"))
        label4.place(x=80, y=180)
        # Show *** to hide PIN input
        self.PIN_entry = Entry(self.window, font="Arial 20", show="*")
        self.PIN_entry.insert(END, '')
        self.PIN_entry.place(x=160, y=180, width=300, height=40)

        btn7 = tk.Button(text="7", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(7))
        btn7.place(x=120, y=227)
        btn4 = tk.Button(text="4", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(4))
        btn4.place(x=120, y=290)
        btn1 = tk.Button(text="1", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(1))
        btn1.place(x=120, y=352)
        login_btn = tk.Button(text="LOGIN", font=('Arial', 16, 'bold'), height=2, width=8, bg="limegreen",
                              command=self.validate_login)
        login_btn.place(x=120, y=418)

        btn8 = tk.Button(text="8", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(8))
        btn8.place(x=235, y=227)
        btn5 = tk.Button(text="5", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(5))
        btn5.place(x=235, y=290)
        btn2 = tk.Button(text="2", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(2))
        btn2.place(x=235, y=352)
        btn0 = tk.Button(text="0", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(0))
        btn0.place(x=235, y=418)

        btn9 = tk.Button(text="9", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(9))
        btn9.place(x=350, y=227)
        btn6 = tk.Button(text="6", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(6))
        btn6.place(x=350, y=290)
        btn3 = tk.Button(text="3", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(3))
        btn3.place(x=350, y=352)
        clearbtn = tk.Button(text="CANCEL", font=('Arial', 16, 'bold'), height=2, width=8, bg="red", command=self.clear)
        clearbtn.place(x=350, y=418)

        # exit button
        exit_btn = tk.Button(text="EXIT", width=15, font=('Arial', 16, 'bold'), height=2, bg="gray", fg="black",
                             command=exit_app)
        exit_btn.place(x=15, y=520)

    # ===== Methods ===== #
    def clear(self):
        entry_focused = self.window.focus_get()
        if entry_focused == self.accNo_entry:
            current_acc = self.accNo_entry.get()
            self.accNo_entry.delete(0, END)
            self.accNo_entry.insert(END, current_acc[:-1])
        elif entry_focused == self.PIN_entry:
            current_pin = self.PIN_entry.get()
            self.PIN_entry.delete(0, END)
            self.PIN_entry.insert(END, current_pin[:-1])
        else:
            print("Nothing Selected")

    def button_handler(self, number):
        entry_focused = self.window.focus_get()
        entry_focused = str(entry_focused)
        if entry_focused == ".!entry":
            self.accNo_entry.insert(END, number)
        elif entry_focused == ".!entry2":
            self.PIN_entry.insert(END, number)
        else:
            print("Nothing Selected")

    def read_data(self):
        with open("customers.txt") as f:
            for line in f:
                customer_data = line.strip().split(";")
                # insert customer data from file to dictionary by key:value key being accNo
                self.customers[customer_data[0]] = customer_data[1:]
        # print each customer
        for customer in self.customers:
            print(customer, self.customers[customer])

    def validate_login(self):
        # read the file again to make sure new account is accessible
        self.read_data()
        account = self.accNo_entry.get()
        pin = self.PIN_entry.get()

        # check if account exists in dictionary
        if account in self.customers:
            # check if account and pin matches
            if self.customers[account][0] == pin:
                self.window.destroy()
                Bank(self.customers, account)
                print("Valid")
            else:
                print("Wrong PIN")
        else:
            print("Account doesnt exist")


LoginScreen().window.mainloop()
