class Stock:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Stock Name: {self.name}, Price: {self.price}, Stock: {self.stock}"

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = value

    @stock.deleter
    def stock(self):
        del self._stock

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        del self._price


stock1 = Stock("Apple", 150, 100)
print(stock1)  # Output: Stock Name: Apple, Price: 150, Stock: 100
stock1.price = 200  # Update price using setter
stock1.stock = 50   # Update stock using setter
print(stock1)  # Output: Stock Name: Apple, Price: 200, Stock: 50

del stock1.price  # Delete price using deleter
del stock1.stock  # Delete stock using deleter

