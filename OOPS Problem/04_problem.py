# Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

# Can you change the self-parameter inside a class to something else (say "harry"). Try changing self to "sit" or "harry" and see the effects.
from random import randint

def can_convert_toint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def hello():
    print("Hello")
class Train:
    
    def __init__(self,train_no,fro,to) -> None:
        self.train_no = train_no
        self.fro = fro
        self.to = to
        self.max_tickits = 100
        self.booked_tickits = 0
        self.fare = randint(20,60)
        

    def book_tickits(self,tickits,fro,to):
        if(self.booked_tickits == self.max_tickits):
            print("seats are full")
            return
        if(self.booked_tickits + tickits > self.max_tickits):
            print(f"only {self.max_tickits - self.booked_tickits} setas are available")
            is_yes = input(f"Do you want to continue of booking for {self.max_tickits - self.booked_tickits} seats Enter(y/n)")
            if(is_yes != 'y' and is_yes != 'Y'):
                print("Thank you for your response")
                return
            else:
                fare = self.fare * (self.max_tickits - self.booked_tickits)
                while True:
                    amount = input(f"Your tickits are {self.max_tickits - self.booked_tickits} & Your Total fare is {fare} Enter a amount to Proceed or e to Exit: ")
                    if(not(can_convert_toint(amount))):
                        print("Thank you for your Response")
                        return
                    elif(int(amount) != fare):
                        print("Please Enter Right Amount and Try Again")
                        continue
                    else:
                        self.booked_tickits += (self.max_tickits - self.booked_tickits)
                        print(f"Happy journy!\nyour Tickits Booked Successful!\nfrom {fro} to {to}\nyour train no is {self.train_no}")
                        return
        fare = tickits * self.fare
        
        while True:
            amount = input(f"Your tickits are {tickits} & Your Total fare is {fare} Enter a amount to Proceed or e to Exit: ")
            if(not(can_convert_toint(amount))):
                print("Thank you for your Response")
                return
            elif(int(amount) != fare):
                print("Please Enter Right Amount and Try Again")
                continue
            else:
                self.booked_tickits += tickits
                print(f"Happy journy!\nyour Tickits Booked Successful!\nfrom {fro} to {to}\nyour train no is {self.train_no}")
                return

    
    def train_info(self):
        print("Train is Running undear a Indian Railway")
        print(f"Booked Seats = {self.booked_tickits}\nRemaining seats = {self.max_tickits - self.booked_tickits}\nof train {self.train_no}\nwhich is start from {self.fro} and destination is {self.to}")


    def get_fare(self):
        print(f"Fare per ticket is {self.fare}")

if __name__=='__main__':

    train1 = Train("MH1234","Mumbai","Dubai")
    train1.train_info()
    train1.get_fare()
    train1.book_tickits(77,"wangi","New York")
    train1.train_info()
    train1.book_tickits(40,"New York","Canada")
    train1.get_fare()