class Order:

    global_discount = 10    # 10% global discount

    @classmethod
    def apply_global_discount(cls, amount) ->None:
        cls.global_discount = amount




order = Order()
print(order.global_discount)  # Output: 10
order.apply_global_discount(15)  # Update global discount to 15%
print(order.global_discount)  # Output: 15
