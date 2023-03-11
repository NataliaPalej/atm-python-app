from tkinter import *
import tkinter as tk


class CustomerDetails:
    def __init__(self):
        self.frame = tk.Tk()
        self.frame.geometry("600x600")
        self.frame.title("ATM - Natalia Palej A00279259")
        self.frame.resizable(False, False)

        # title label
        self.label1 = Label(self.frame, text="Customer Details", fg="white", bg="black", font=("arial", 16, "bold"))
        self.label1.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # place on screen

        # name
        self.name = Label(self.frame, text="Name", fg="black", bg="dodgerblue1", width=10, font=("arial", 10, "bold"))
        self.name.grid(row=1, column=0, padx=54, pady=3)
        self.name_entry = Entry(self.frame)
        self.name_entry.insert(END, '')
        self.name_entry.grid(row=1, column=1, columnspan=3, sticky=W + E)

        # surname
        self.surname = Label(self.frame, text="Surname", fg="black", bg="dodgerblue1", width=10,
                             font=("arial", 10, "bold"))
        self.surname.grid(row=2, column=0, pady=3)
        self.surname_entry = Entry(self.frame)
        self.surname_entry.insert(END, '')
        self.surname_entry.grid(row=2, column=1, sticky=W + E)

        # sex
        self.sex = Label(self.frame, text="Sex", fg="black", bg="dodgerblue1", width=10, font=("arial", 10, "bold"))
        self.sex.grid(row=3, column=0, pady=3)
        self.sex_entry = Entry(self.frame, width=20)
        self.sex_entry.insert(END, '0')
        self.sex_entry.grid(row=3, column=1, sticky=W + E)

        # occupation
        self.occupation = Label(self.frame, text="Occupation", fg="black", bg="dodgerblue1", width=10,
                                font=("arial", 10, "bold"))
        self.occupation.grid(row=4, column=0, pady=3)
        self.occupation_entry = Entry(self.frame)
        self.occupation_entry.insert(END, '0')
        self.occupation_entry.grid(row=4, column=1, sticky=W + E)

        # address
        self.address = Label(self.frame, text="Address", fg="black", bg="dodgerblue1", width=10,
                             font=("arial", 10, "bold"))
        self.address.grid(row=5, column=0, pady=3)
        self.address_entry = Entry(self.frame)
        self.address_entry.insert(END, '0')
        self.address_entry.grid(row=5, column=1, sticky=W + E)

        # phone
        self.phone = Label(self.frame, text="Phone No", fg="black", bg="dodgerblue1", width=10,
                           font=("arial", 10, "bold"), borderwidth=1, relief="solid")
        self.phone.grid(row=5, column=2)
        self.phone_entry = Entry(self.frame)
        self.phone_entry.insert(END, '0')
        self.phone_entry.grid(row=5, column=3, sticky=W + E)

        # email
        self.email = Label(self.frame, text="Email", fg="black", bg="dodgerblue1", width=10,
                           font=("arial", 10, "bold"))
        self.email.grid(row=6, column=0, pady=3)
        self.email_entry = Entry(self.frame)
        self.email_entry.insert(END, '0')
        self.email_entry.grid(row=6, column=1, sticky=W + E)

        # accNo
        self.accNo = Label(self.frame, text="AccNo", fg="black", bg="dodgerblue1", width=10, font=("arial", 10, "bold"))
        self.accNo.grid(row=7, column=0, pady=3)
        self.accNo_entry = Entry(self.frame)
        self.accNo_entry.insert(END, '0')
        self.accNo_entry.grid(row=7, column=1, sticky=W + E)

        # reset
        self.reset = Button(self.frame, text="RESET", fg="black", bg="white", font=("arial", 10, "bold"),
                            command=lambda: self.clear_data(self.current))
        self.reset.grid(row=12, column=0, columnspan=2, sticky=W + E, padx=3)

        self.frame.mainloop()

    # Event Handling Methods
    def display(self, index):
        self.current = index
        customer = self.cust_list[index]

        self.name_entry.delete(0, END)
        self.name_entry.insert(END, customer.get_name())

        self.surname_entry.delete(0, END)
        self.surname_entry.insert(END, customer.get_surname())

        self.sex_entry.delete(0, END)
        self.sex_entry.insert(END, customer.get_sex())

        self.occupation_entry.delete(0, END)
        self.occupation_entry.insert(END, customer.get_occupation())

        self.address_entry.delete(0, END)
        self.address_entry.insert(END, customer.get_address())

        self.phone_entry.delete(0, END)
        self.phone_entry.insert(END, customer.get_phone())

        self.email_entry.delete(0, END)
        self.email_entry.insert(END, customer.get_email())

        self.accNo_entry.delete(0, END)
        self.accNo_entry.insert(END, customer.get_accNo())


# TODO: SAVE AND EXIT BUTTON (OPEN ON TOP OF BANK WINDOW)

CustomerDetails().frame.mainloop()