class BankAccount:
    """ A class representing bank accounts
    """
    def __init__(self, bank, owner, balance=0):
        """initialize account"""
        self.balance = balance
        self.owner = owner
        self.bank = bank

    def __str__(self):
        return f"Bank account: {self.bank} bank, {self.owner} owner and ${self.balance} balance."

    def deposit(self, amount):
        """add money to account"""
        self.balance += amount

    def withdraw(self, amount):
        """take out money from account"""
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

new_acc = BankAccount("Chase", "Jim Bob")
print(new_acc)
new_acc.deposit(500)
print(new_acc)
new_acc.withdraw(700)
new_acc.withdraw(300)
print(new_acc)


class Box:
    """ class for boxes
    """
    def __init__(self, length, width):
        """initialize box"""
        self.length = length
        self.width = width

    def __eq__(self, other):
        """test for box size equality"""
        return (self.width == other.width and self.length == other.length)

    def invert(self):
        """swaps box length and width"""
        l = self.length
        w = self.width
        self.length = w
        self.width = l


    def get_area(self):
        """returns area of box"""
        return(self.length * self.width)

    def get_perimeter(self):
        """returns the perimiter of the box"""
        return((2 * self.length) + (2 * self.width))

    def double(self):
        """doubles the size of the box"""
        self.length *=2
        self.width *= 2

    def print_dim(self):
        """prints the dim of the box"""
        print(f"The size of the box is length {self.length} and width {self.width}")

    def get_dim(self):
        """retuns the size as a tuple"""
        return tuple(self.length, self.width)

    def combine(self, other):
        """combines 2 boxes"""
        self.length += other.length
        self.width += other.width

    def get_hypot(self):
        """returns the length of the diagonal"""
        return((self.length ** 2 + self.width ** 2) ** (1/2))

    def render(self):
        for length in range(0,self.length):
            print("*" * self.width)

box1 = Box(5,10)
box1.render()
box2 = Box(3,4)
box2.render()
box3 = Box(5,10)

box1.print_dim()
box2.print_dim()
box3.print_dim()

print(box1 == box2)
print(box1 == box3)

box1.combine(box3)
box1.print_dim()

box2.double()
box1.combine(box2)
box1.print_dim()
