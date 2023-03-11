from tkinter import *
import tkinter as tk


class CustomerDetails:
    def __init__(self, customers, customer):
        self.window = tk.Tk()
        self.window.geometry("600x600")
        self.window.title("ATM - Natalia Palej A00279259")
        self.window.resizable(False, False)

        # get current customer
        self.current_customer = customers[customer]
        self.customers = customers

        # title label
        self.label1 = Label(self.window, text="Account Details", fg="black", font=("arial", 20, "bold"))
        self.label1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # accNo
        self.accNo = Label(self.window, text="Account Number: {0}".format(self.current_customer[1])
                           , fg="black", bg="dodgerblue1", width=20, font=("arial", 10, "bold"))
        self.accNo.grid(row=1, column=0, columnspan=2, pady=3)

        # name
        self.name = Label(self.window, text="Name", fg="black", bg="dodgerblue1", width=20,
                          font=("arial", 10, "bold"))
        self.name.grid(row=2, column=0, padx=54, pady=3)
        self.name_entry = Entry(self.window)
        self.name_entry.insert(END, '')
        self.name_entry.grid(row=2, column=1, sticky=W + E)

        # surname
        self.surname = Label(self.window, text="Surname", fg="black", bg="dodgerblue1", width=20,
                             font=("arial", 10, "bold"))
        self.surname.grid(row=3, column=0, pady=3)
        self.surname_entry = Entry(self.window)
        self.surname_entry.insert(END, '')
        self.surname_entry.grid(row=3, column=1, sticky=W + E)

        # sex
        self.sex = Label(self.window, text="Sex", fg="black", bg="dodgerblue1", width=20,
                         font=("arial", 10, "bold"))
        self.sex.grid(row=4, column=0, pady=3)
        self.sex_entry = Entry(self.window, width=20)
        self.sex_entry.insert(END, '0')
        self.sex_entry.grid(row=4, column=1, sticky=W + E)

        # occupation
        self.occupation = Label(self.window, text="Occupation", fg="black", bg="dodgerblue1", width=20,
                                font=("arial", 10, "bold"))
        self.occupation.grid(row=5, column=0, pady=3)
        self.occupation_entry = Entry(self.window)
        self.occupation_entry.insert(END, '0')
        self.occupation_entry.grid(row=5, column=1, sticky=W + E)

        # address
        self.address = Label(self.window, text="Address", fg="black", bg="dodgerblue1", width=20,
                             font=("arial", 10, "bold"))
        self.address.grid(row=6, column=0, pady=3)
        self.address_entry = Entry(self.window)
        self.address_entry.insert(END, '0')
        self.address_entry.grid(row=6, column=1, sticky=W + E)

        # phone
        self.phone = Label(self.window, text="Phone No", fg="black", bg="dodgerblue1", width=20,
                           font=("arial", 10, "bold"), borderwidth=1, relief="solid")
        self.phone.grid(row=7, column=2)
        self.phone_entry = Entry(self.window)
        self.phone_entry.insert(END, '0')
        self.phone_entry.grid(row=7, column=3, sticky=W + E)

        # email
        self.email = Label(self.window, text="Email", fg="black", bg="dodgerblue1", width=20,
                           font=("arial", 10, "bold"))
        self.email.grid(row=8, column=0, pady=3)
        self.email_entry = Entry(self.window)
        self.email_entry.insert(END, '0')
        self.email_entry.grid(row=8, column=1, sticky=W + E)

        # reset
        self.reset = Button(self.window, text="CLEAR", fg="black", bg="white", font=("arial", 10, "bold"),
                            command=lambda: self.clear)
        self.reset.grid(row=12, column=0, columnspan=2, sticky=W + E, padx=3)

        self.window.mainloop()

    def clear(self):
        self.name_entry = ""
        self.surname_entry = ""
        self.sex_entry = ""
        self.occupation_entry = ""
        self.address_entry = ""
        self.phone_entry = ""
        self.email_entry = ""

    def read_data(self):
        with open("customers.txt") as f:
            for line in f:
                customer_data = line.strip().split(";")
                # insert customer data from file to dictionary by key:value key being accNo
                self.customers[customer_data[0]] = customer_data[1:]
        # print each customer
        for customer in self.customers:
            print(customer, self.customers[customer])

    # save new details in the file
    def save_data(self):
        with open('outfile.txt', 'a') as save_data:
            for customer in self.customers:
                # print(customer, self.customers[customer])
                save_data.write(customer + ';')
                for i in self.customers[customer]:
                    save_data.write(str(i) + ';')
                save_data.write("\n")

# TODO: SAVE AND EXIT BUTTON (OPEN ON TOP OF BANK WINDOW)
