import tkinter as tk
from tkinter import *
from Customer import Customer


class Bank:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("600x600")
        self.window.title("Your Account")
        # bg = ImageTk.PhotoImage(Image.open("images/volleyball.jpg"))
        # myBG = Label(image=bg)
        # myBG.place(x=0, y=0, relwidth=1, relheight=1)

        self.window.resizable(False, False)

        c1 = Customer("Lilly", "Mayor", "Female", "Employed", "Athlone", "089 421 4578", "LillyMayor@gmail.com",
                      "123456", "1234")
        c2 = Customer("Lola", "Kennedy", "Undefined", "Student", "Roscommon", "087 421 1234", "LolaKennedy@gmail.com",
                      "987654", "9876")
        c3 = Customer("Mike", "Smith", "Male", "Unemployed", "Dublin", "086 123 4578", "MikeSmith@gmail.com", "456132",
                      "6789")

        self.cust_list = [c1, c2, c3]

        # customer details button
        cust_details = tk.Button(text="Customer Details", font=('Arial', 16, 'bold'), height=2, width=15, takefocus=1,
                                 command=self.details_screen)
        cust_details.place(x=200, y=100)

        # exit button
        exit_button = tk.Button(text="Exit", width=15, font=('Arial', 16, 'bold'), height=2, command=self.exit_app,
                                bg="gray", fg="black")
        exit_button.place(x=200, y=450)

    # details screen
    def details_screen(self):
        window2 = Toplevel(self.window, bg="grey85")
        window2.geometry("600x500")
        window2.title("Customer Details")
        detail_screen = CustomerDetails(window2, self.cust_list)
        detail_screen.display(0)

        button = Button(window2, text="Close", width=100, height=2, command=window2.destroy, font=("arial", 10, "bold"))
        button.pack(side=tk.BOTTOM)

    # exit app
    def exit_app(self):
        exit()
