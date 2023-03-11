import tkinter as tk
from tkinter import *
from tkinter import messagebox

# TODO: Submenu to show your account details (pop up only)
# TODO: Submenu to edit your account details (screen with editable)
class Bank:
    def __init__(self, customers, customer):
        self.window2 = tk.Tk()
        self.window2.geometry("600x600")
        self.window2.title("Your Account")
        self.window2.resizable(False, False)

        # get current customer
        self.current_customer = customers[customer]

        self.customers = customers

        label = Label(self.window2, text="WELCOME, {0}".format(self.current_customer[1]), fg="black",
                      font=("arial", 20, "bold"))
        label.grid(row=0, column=0, pady=20, padx=150)

        # ==== balance ====
        self.label0 = Label(self.window2, text="BALANCE: ", fg="black",
                            font=("arial", 20, "bold"))
        self.label0.place(x=80, y=100)

        self.v = StringVar()
        self.v.set(self.current_customer[8])
        self.label1 = Label(self.window2, textvariable=self.v, fg="black",
                            font=("arial", 20, "bold"))
        self.label1.place(x=300, y=100)

        label4 = Label(self.window2, text="AMOUNT:", fg="black", font=("arial", 10, "bold"))
        label4.place(x=80, y=180)
        self.amount_entry = Entry(self.window2, font="Arial 20")
        self.amount_entry.insert(END, '')
        self.amount_entry.place(x=160, y=180, width=300, height=40)
        self.amount_entry.focus()

        btn7 = tk.Button(self.window2, text="7", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(7))
        btn7.place(x=120, y=227)
        btn4 = tk.Button(self.window2, text="4", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(4))
        btn4.place(x=120, y=290)
        btn1 = tk.Button(self.window2, text="1", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(1))
        btn1.place(x=120, y=352)
        login_btn = tk.Button(self.window2, text="WITHDRAW", font=('Arial', 16, 'bold'), height=2, width=8,
                              bg="limegreen", command=self.withdraw)
        login_btn.place(x=120, y=418)

        btn8 = tk.Button(self.window2, text="8", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(8))
        btn8.place(x=235, y=227)
        btn5 = tk.Button(self.window2, text="5", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(5))
        btn5.place(x=235, y=290)
        btn2 = tk.Button(self.window2, text="2", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(2))
        btn2.place(x=235, y=352)
        btn0 = tk.Button(self.window2, text="0", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(0))
        btn0.place(x=235, y=418)

        btn9 = tk.Button(self.window2, text="9", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(9))
        btn9.place(x=350, y=227)
        btn6 = tk.Button(self.window2, text="6", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(6))
        btn6.place(x=350, y=290)
        btn3 = tk.Button(self.window2, text="3", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(3))
        btn3.place(x=350, y=352)
        clearbtn = tk.Button(self.window2, text="CANCEL", font=('Arial', 16, 'bold'), height=2, width=8, bg="red",
                             command=self.clear)
        clearbtn.place(x=350, y=418)

        # exit button
        exit_btn = tk.Button(self.window2, text="LOGOUT", width=15, font=('Arial', 16, 'bold'), height=2, bg="gray",
                             fg="black",
                             command=self.exit)
        exit_btn.place(x=15, y=520)

        self.window2.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window2.mainloop()

    # ===== Methods ===== #
    def exit(self):
        self.save_data()
        exit()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.save_data()
            self.window2.destroy()

    def clear(self):
        self.amount_entry.delete(0, END)
        self.amount_entry.insert(END, "")

    def button_handler(self, number):
        self.amount_entry.insert(END, number)

    def withdraw(self):
        amt = self.amount_entry.get()
        balance = self.current_customer[8]
        new_balance = int(balance) - int(amt)
        self.current_customer[8] = new_balance
        self.v.set(self.current_customer[8])

    # save updated balance in the file
    def save_data(self):
        with open('customers.txt', 'w') as save_data:
            for customer in self.customers:
                # print(customer, self.customers[customer])
                save_data.write(customer + ';')
                for i in self.customers[customer]:
                    save_data.write(str(i) + ';')
                save_data.write("\n")
