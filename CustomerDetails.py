from tkinter import *
import tkinter as tk

import bg

from Customer import Customer


class CustomerDetails:
    def __init__(self, window2, cus_list):
        self.cus_list = cus_list
        self.current = 0  # current team
        self.cus_list = self.cus_list[0]  # initialize to first match

        # ===== GUI ===== #
        self.frame = tk.Frame(window2, width=635, height=590)

        self.frame.place(x=20, y=20)

        # bg = ImageTk.PhotoImage(Image.open("images/volleyball.jpg"))

        self.panel = tk.Label(self.frame, image=bg)
        self.panel.image = bg
        self.panel.place(x=0, y=0, relwidth=1, relheight=1)
        window2.resizable(False, False)

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

        # checkbox injury
        self.var_cb1 = IntVar()  # 0 unchecked, 1 checked
        self.cb1 = Checkbutton(self.frame, text="Injury", variable=self.var_cb1, width=8, borderwidth=1,
                               relief="solid", bg="darkgoldenrod1", fg="black")
        self.cb1.grid(row=8, column=0, pady=3)

        # blank line
        self.labelBlank = Label(self.frame, bg="black")
        self.labelBlank.grid(row=11)

        # reset
        self.reset = Button(self.frame, text="RESET", fg="black", bg="white", font=("arial", 10, "bold"),
                            command=lambda: self.clear_data(self.current))
        self.reset.grid(row=12, column=0, columnspan=2, sticky=W + E, padx=3)

        # blank line
        self.labelBlank = Label(self.frame, bg="black")
        self.labelBlank.grid(row=13)

        # previous and next button
        self.previous = Button(self.frame, text="Previous", fg="black", bg="darkgoldenrod1", font=("arial", 10, "bold"),
                               command=self.previous_button)
        self.previous.grid(row=14, column=0, sticky=W + E, pady=3, columnspan=2)

        self.next_button = Button(self.frame, text="Next", fg="black", bg="dodgerblue3", font=("arial", 10, "bold"),
                                  command=self.next_button)
        self.next_button.grid(row=14, column=2, columnspan=3, sticky=W + E)

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

    def next_button(self):
        if self.current < (len(self.cust_list) - 1):
            self.current += 1
            self.display(self.current)

    def previous_button(self):
        if self.current > 0:
            self.current -= 1
            self.display(self.current)