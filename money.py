import functools

@functools.total_ordering
class Money:
    """
    Klasa obśługująca finanse
    """
    def __init__(self, amount, currency="PLN"):
        self.amount = float(amount)
        self.currency = currency
    
    def __repr__(self):
        return f"Money({self.amount}, {self.currency})"
    
    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"
    
    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency
    
    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Nie można porównać pieniędzy w różnych walutach")
        return self.amount < other.amount
    
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Nie można dodać pieniędzy w różnych walutach")
        return Money(self.amount + other.amount, self.currency)
    
    def __mul__ (self, scalar):
        return Money(self.amount * scalar, self.currency)
    
    def __hash__(self):
        return hash((self.amount, self.currency))