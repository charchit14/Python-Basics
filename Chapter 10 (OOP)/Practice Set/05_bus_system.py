"""Create a class Bus that has methods to book a ticket, get status (no. of seats), 
and get fare information of bus running"""


class Bus:
    def __init__(self):
        print()
        print("\t\t\t\t**Welcome to Bus Reservation System**")
        print("1.Book Ticket\t\t2.Get Status\t\t3.Get Fare Info\t\t4.Cancel Ticket")
        print()

    def book(self):
        z = input("Press 'y' to book ticket: ")
        if z.lower() == "y":
            print("Ticekt Booked")
            self.se -= 1
        else:
            print("Ticket not booked")

    def status(self):
        print(f"The number of seats are: {self.se}")

    def fare(self):
        print("The fare system are as follows:\nKTM to Achham = 900\nKTM to Baitadi = 800")

    def cancel(self):
        if self.se == 99:
            print("No ticket booked to cancel")
            print(f"The number of seats are: {self.se}")
        else:
            print("Your ticket has been canceled")
            self.se += 1
            print(f"The number of seats are: {self.se}")

c = Bus()
c.se = 99   #This is the total number of available seats


'''Keeping the loop here will not completely reset the program status 
rather it will continue from current status 
(Eg: If you book a ticket then total tickets will be 98 and when you press 'y' to check again 
rather than reseting ticket to 99, it will continue with 98 until you exit the program)'''

while True:
    i = int(input("Choose your option: "))

    if i == 1:
        c.status()
        c.book()
        c.status()
    elif i == 2:
        c.status()
    elif i == 3:
        c.fare()
    elif i == 4:
        c.cancel()
    else:
        print("Invalid Input")

    print()
    re = input("Press 'y' to check again: ")
    print()
    if re.lower() != "y":
        break