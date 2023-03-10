class Customer:
    # New customer constructor
    def __init__(self, name, surname, sex, occupation, address, phone, email, accNo, accPIN):
        self.__name = name
        self.__surname = surname
        self.__sex = sex
        self.__occupation = occupation
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__accNo = accNo
        self.__accPIN = accPIN
        self.__balance = 0

    # Clear all fields
    def reset_all(self):
        self.__name = " "
        self.__surname = " "
        self.__sex = " "
        self.__occupation = " "
        self.__address = " "
        self.__phone = " "
        self.__email = " "
        self.__accNo = " "
        self.__accPIN = " "

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_sex(self):
        return self.__sex

    def get_occupation(self):
        return self.__occupation

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_accNo(self):
        return self.__accNo

    def get_accPIN(self):
        return self.__accPIN

    def get_balance(self):
        return self.__balance

    def withdraw(self, amt):
        if self.__balance >= amt:
            self.__balance -= amt
        else:
            self.__balance -= amt
            print("YOUR BALANCE IS NOW NEGATIVE")

    def deposit(self, amt):
        self.__balance += amt

    def transfer(self, amt):
        if self.__balance < amt:
            print("Not enough funds")
        else:
            self.__balance -= amt



