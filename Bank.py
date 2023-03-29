import tkinter as tk
from tkinter import *
from tkinter import messagebox
from CustomerDetails import CustomerDetails
from tkinter.ttk import Combobox


def help_details():
    # Create a new window
    new_window = tk.Toplevel()
    new_window.title("Help Page")
    new_window.geometry("400x400")
    new_window.configure(bg="#fce8d5")

    frame = tk.Frame(new_window, bg="#fce8d5")
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    message_label1 = tk.Label(frame, text="Max deposit amount €10,000 at a time", font=("Helvetica", 16),
                              bg="#fce8d5", fg="grey15")
    message_label1.pack(pady=10)

    message_label2 = tk.Label(frame, text="Unlimited fund transfer to other users", font=("Helvetica", 16),
                              bg="#fce8d5", fg="grey15")
    message_label2.pack(pady=10)

    message_label3 = tk.Label(frame, text="Max dept amount -€1,000", font=("Helvetica", 16), bg="#fce8d5",
                              fg="grey15")
    message_label3.pack(pady=10)

    ok_button = tk.Button(frame, text="OK", font=("Helvetica", 14), bg="#4caf50", fg="#fff", command=new_window.destroy)
    ok_button.pack(pady=20, side="bottom")

    new_window.mainloop()


class Bank:
    def __init__(self, customers, customer):
        self.window2 = tk.Tk()
        self.window2.geometry("600x600")
        self.window2.title("Your Account")
        self.window2.resizable(False, False)

        # ==== SUB MENU ==== #
        submenu = Menu(self.window2)
        self.window2.config(menu=submenu)
        edit_details = Menu(submenu)
        # Name the submenu
        submenu.add_cascade(label="OPTIONS", menu=edit_details)
        # Add option in submenu
        edit_details.add_command(
            label="EDIT DETAILS", command=self.edit_details)
        edit_details.add_command(
            label="HELP", command=help_details)

        # === Get current customer === #
        self.current_customer = customers[customer]
        self.customers = customers
        self.customer = customer

        # === Get other customers === #
        self.customers_list = {}
        for key, value in customers.items():
            if value != self.current_customer:
                self.customers_list[key] = "{0} {1}".format(value[1], value[2])
        print(self.customers_list)

        label = Label(self.window2, text="WELCOME, {0}".format(self.current_customer[1]), fg="black",
                      font=("arial", 20, "bold"))
        label.grid(row=0, column=0, pady=20, padx=150)

        self.label0 = Label(self.window2, text="BALANCE:       €", fg="black",
                            font=("arial", 20, "bold"))
        self.label0.place(x=80, y=80)

        # === Update balance dynamically === #
        self.v = StringVar()
        self.v.set(self.current_customer[8])
        self.label1 = Label(self.window2, textvariable=self.v, fg="black",
                            font=("arial", 20, "bold"))
        self.label1.place(x=300, y=80)

        # === Create a dropdown to select customer to transfer money to === #
        label2 = Label(self.window2, text="TRANSFER TO:", fg="black", font=("arial", 15, "bold"))
        label2.place(x=60, y=123)
        self.customer_dropdown = Combobox(self.window2, font=("Arial", 15), values=list(self.customers_list.values()),
                                          state="readonly")
        self.customer_dropdown.place(x=230, y=120, width=250, height=40)

        label4 = Label(self.window2, text="AMOUNT:", fg="black", font=("arial", 15, "bold"))
        label4.place(x=60, y=185)
        self.amount_entry = Entry(self.window2, font="Arial 20")
        self.amount_entry.insert(END, '')
        self.amount_entry.place(x=164, y=180, width=380, height=40)
        self.amount_entry.focus()

        btn7 = tk.Button(self.window2, text="7", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(7))
        btn7.place(x=60, y=227)
        btn4 = tk.Button(self.window2, text="4", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(4))
        btn4.place(x=60, y=293)
        btn1 = tk.Button(self.window2, text="1", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(1))
        btn1.place(x=60, y=359)
        empty = tk.Button(self.window2, text=" ", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue")
        empty.place(x=60, y=425)
        empty.config(state="disabled")

        btn8 = tk.Button(self.window2, text="8", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(8))
        btn8.place(x=175, y=227)
        btn5 = tk.Button(self.window2, text="5", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(5))
        btn5.place(x=175, y=293)
        btn2 = tk.Button(self.window2, text="2", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(2))
        btn2.place(x=175, y=359)
        btn0 = tk.Button(self.window2, text="0", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(0))
        btn0.place(x=175, y=425)

        btn9 = tk.Button(self.window2, text="9", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(9))
        btn9.place(x=290, y=227)
        btn6 = tk.Button(self.window2, text="6", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(6))
        btn6.place(x=290, y=293)
        btn3 = tk.Button(self.window2, text="3", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue",
                         command=lambda: self.button_handler(3))
        btn3.place(x=290, y=359)
        empty2 = tk.Button(self.window2, text=" ", font=('Arial', 16, 'bold'), height=2, width=8, bg="lightblue")
        empty2.place(x=290, y=425)
        empty2.config(state="disabled")

        withdraw = tk.Button(self.window2, text="WITHDRAW", font=('Arial', 16, 'bold'), height=2, width=10,
                             bg="limegreen", command=self.withdraw)
        withdraw.place(x=405, y=227)

        deposit = tk.Button(self.window2, text="DEPOSIT", font=('Arial', 16, 'bold'), height=2, width=10,
                            bg="yellow", command=self.deposit)
        deposit.place(x=405, y=293)

        # empty3 = tk.Button(self.window2, text=" ", font=('Arial', 16, 'bold'), height=2, width=10,
        #                    bg="lightblue")
        # empty3.place(x=405, y=359)
        # empty3.config(state="disabled")

        # === Create a button to transfer funds to selected customer === #
        transfer_btn = tk.Button(self.window2, text="TRANSFER", font=('Arial', 16, 'bold'), height=2, width=10,
                                 bg="lightblue", command=self.transfer_funds)
        transfer_btn.place(x=405, y=359)

        clearbtn = tk.Button(self.window2, text="CANCEL", font=('Arial', 16, 'bold'), height=2, width=10, bg="red",
                             command=self.clear)
        clearbtn.place(x=405, y=425)

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
        current_amt = self.amount_entry.get()
        new_amt = current_amt[:-1]
        self.amount_entry.delete(0, END)
        self.amount_entry.insert(END, new_amt)

    def button_handler(self, number):
        self.amount_entry.insert(END, number)

    def withdraw(self):
        try:
            amt = int(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("WARNING", "Please enter valid amount.")
            return

        balance = int(self.current_customer[8])
        new_balance = balance - amt
        if new_balance < -1000:
            messagebox.showwarning("WARNING", "Your balance is €{0}! Maximum dept is -€1,000".format(balance))
        elif new_balance < 0:
            answer = messagebox.askquestion("WARNING", "Your balance will be negative (€{0}), "
                                                       "are you sure you want to proceed?".format(new_balance))
            if answer == 'yes':
                self.current_customer[8] = new_balance
                self.v.set(str(new_balance))
                self.amount_entry.delete(0, END)
                self.amount_entry.insert(END, "")
            else:
                # Withdrawal cancelled, balance remains unchanged
                self.amount_entry.delete(0, END)
                self.amount_entry.insert(END, "")
                pass
        else:
            self.current_customer[8] = new_balance
            self.v.set(str(new_balance))

    def deposit(self):
        try:
            amt = int(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("WARNING", "Please enter valid amount.")
            return

        balance = int(self.current_customer[8])
        if amt > 10000:
            formatted_amt = "{:,}".format(amt)
            messagebox.showwarning("WARNING", "You cannot deposit more than €10,000 at a time.\n"
                                              "You are trying to deposit €{0}".format(formatted_amt))
        else:
            new_balance = balance + amt
            self.current_customer[8] = new_balance
            self.v.set(str(new_balance))

    def transfer_funds(self):
        try:
            amt = int(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("WARNING", "Please enter valid amount.")
            return

        # Get the selected customer's details
        selected_customer = self.customer_dropdown.get()
        selected_customer_acc = 0
        for key, val in self.customers_list.items():
            if val == selected_customer:
                selected_customer_acc = key
        selected_customer_balance = int(self.customers[selected_customer_acc][8])

        if amt > int(self.current_customer[8]):
            messagebox.showerror("Insufficient balance", "You have insufficient balance.")
        elif amt <= 0:
            messagebox.showerror("Invalid amount", "Please enter a valid amount.")
        else:
            # Update balances
            selected_customer_balance += amt
            self.current_customer[8] = str(int(self.current_customer[8]) - amt)
            self.v.set(self.current_customer[8])
            # Show success message
            messagebox.showinfo("Success", "Transfer Successfull\nYou transferred €{0} to "
                                           "{1}".format(amt, selected_customer))
            print("Your balance €{0}, {1} balance €{2}".format(self.current_customer[8],
                                                               selected_customer, selected_customer_balance))
        # Update selected customer's balance
        self.customers[selected_customer_acc][8] = selected_customer_balance

    # Save updated balance in the file
    def save_data(self):
        with open('customers.txt', 'w') as save_data:
            for customer in self.customers:
                save_data.write(customer + ';')
                # Enumerate gets index and value of each element in self.cust[cust]
                for i, data in enumerate(self.customers[customer]):
                    save_data.write(str(data))
                    # Condition that adds ";" until its last element in the list
                    if i != len(self.customers[customer]) - 1:
                        save_data.write(';')
                save_data.write("\n")

    def edit_details(self):
        CustomerDetails(self.customers, self.customer)
