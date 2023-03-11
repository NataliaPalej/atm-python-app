from tkinter import *
import random
import tkinter.messagebox

def acc_no():
    accNo = random.randint(100000, 999999)
    return accNo


class NewAccount:
    def __init__(self):
        self.window = Toplevel()
        self.window.geometry("600x600")
        self.window.title("ATM - Natalia Palej A00279259")
        self.window.resizable(False, False)

        self.label1 = Label(self.window, text="New Account Details", fg="black", font=("arial", 20, "bold"))
        self.label1.place(x=120, y=20)

        # accNo
        self.accNo = Label(self.window, text="Account Number: {0}".format(acc_no()), fg="black", width=30,
                           font=("arial", 20, "bold"))
        self.accNo.place(x=0, y=60)

        self.name = Label(self.window, text="Name", fg="black", width=15, font=("arial", 15, "bold"))
        self.name.place(x=50, y=120)
        self.name_entry = Entry(self.window, font=("arial", 15, "bold"))
        self.name_entry.insert(END, '')
        self.name_entry.place(x=250, y=120)

        self.surname = Label(self.window, text="Surname", fg="black", width=15, font=("arial", 15, "bold"))
        self.surname.place(x=50, y=160)
        self.surname_entry = Entry(self.window, font=("arial", 15, "bold"))
        self.surname_entry.insert(END, '')
        self.surname_entry.place(x=250, y=160)

        # gender radio buttons
        self.gender = Label(self.window, text="SEX", fg="black", width=15, font=("arial", 15, "bold"))
        # 0 unchecked, 1 checked
        self.radio = StringVar()
        self.radio1 = Radiobutton(self.window, text="Male", variable=self.radio, value="Male",
                                  command=self.gender_choice)
        self.radio2 = Radiobutton(self.window, text="Female", variable=self.radio, value="Female",
                                  command=self.gender_choice)
        self.radio3 = Radiobutton(self.window, text="Undefined", variable=self.radio, value="Undefined",
                                  command=self.gender_choice)
        self.radio1.place(x=250, y=200)
        self.radio1.select()
        self.radio2.place(x=310, y=200)
        self.radio2.deselect()
        self.radio3.place(x=380, y=200)
        self.radio3.deselect()

        self.occupation = Label(self.window, text="Occupation", fg="black", width=15,
                                font=("arial", 15, "bold"))
        self.occupation.place(x=50, y=240)
        self.occupation_entry = Entry(self.window, font=("arial", 15, "bold"))
        self.occupation_entry.insert(END, '')
        self.occupation_entry.place(x=250, y=240)

        self.address = Label(self.window, text="Address", fg="black", width=15,
                             font=("arial", 15, "bold"))
        self.address.place(x=50, y=280)
        self.address_entry = Entry(self.window, font=("arial", 15, "bold"))
        self.address_entry.insert(END, '')
        self.address_entry.place(x=250, y=280)

        self.phone = Label(self.window, text="Phone no", fg="black", width=15,
                           font=("arial", 15, "bold"))
        self.phone.place(x=50, y=320)
        self.phone_entry = Entry(self.window, font=("arial", 15, "bold"))
        self.phone_entry.insert(END, '')
        self.phone_entry.place(x=250, y=320)

        self.email = Label(self.window, text="Email", fg="black", width=15,
                           font=("arial", 15, "bold"))
        self.email.place(x=50, y=360)
        self.email_entry = Entry(self.window, font=("arial", 15, "bold"))
        self.email_entry.insert(END, '')
        self.email_entry.place(x=250, y=360)

        self.pin = Label(self.window, text="PIN", fg="black", width=15,
                         font=("arial", 15, "bold"))
        self.pin.place(x=50, y=400)
        self.pin_entry = Entry(self.window, font=("arial", 15, "bold"), show="*")
        self.pin_entry.insert(END, '')
        self.pin_entry.place(x=250, y=400)

        # save button
        self.save = Button(self.window, text="SAVE", fg="black", bg="limegreen",
                           font=("arial", 15, "bold"), width=15, command=self.save_data)
        self.save.place(x=70, y=440)

        # clear button
        self.clear = Button(self.window, text="CLEAR", fg="black", bg="red", font=("arial", 15, "bold"), width=15,
                            command=self.clear)
        self.clear.place(x=270, y=440)

        self.window.mainloop()

    def clear(self):
        self.name_entry.delete(0, END)
        self.name_entry.insert(END, '')
        self.surname_entry.delete(0, END)
        self.surname_entry.insert(END, '')
        self.radio1.select()
        self.occupation_entry.delete(0, END)
        self.occupation_entry.insert(END, '')
        self.address_entry.delete(0, END)
        self.address_entry.insert(END, '')
        self.phone_entry.delete(0, END)
        self.phone_entry.insert(END, '')
        self.email_entry.delete(0, END)
        self.email_entry.insert(END, '')

    # radiobutton handler
    def gender_choice(self):
        choice = self.radio.get()
        output = ""
        if choice == "Male":
            output = "Male"
        elif choice == "Female":
            output = "Female"
        elif choice == "Undefined":
            output = "Undefined"
        return output

    # save new details in the file
    def save_data(self):
        accNo = acc_no()
        pin = self.pin_entry.get()
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        gender = self.radio.get()
        occupation = self.occupation_entry.get()
        address = self.address_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        balance = 0

        newAcc = [accNo, pin, name, surname, gender, occupation, address, phone, email, balance]
        print(newAcc)

        with open('customers.txt', 'a') as save_data:
            for i in newAcc:
                save_data.write(str(i) + ';')
            save_data.write("\n")

        tkinter.messagebox.showinfo("New Account", "ACCOUNT SUCCESSFULLY CREATED\nWelcome {0}\nYour Account No: "
                                                   "{1}\n\nPLEASE\nREMEMBER YOUR PIN".format(name, accNo))


        self.window.destroy()
