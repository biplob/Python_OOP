class cls:

    # Constractor
    def __init__(self, fname, mname, lname):
        self.firstname = fname
        self.middlename = mname
        self.lastname = lname

    # Function
    def print(self):
        print(self.firstname, self.middlename, self.lastname)


x = cls("Monsur", "Islam", "Bhuiyan")
x.print()