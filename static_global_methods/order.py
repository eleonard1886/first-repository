class Order:


    @staticmethod
    def calculate_tax(amount, tax_rate) -> float:
        """
        Calculate the tax for a given amount and tax rate.

        :param amount: The amount to calculate tax on.
        :param tax_rate: The tax rate as a decimal (e.g., 0.05 for 5%).
        :return: The calculated tax.
        """
        return round(amount * (tax_rate / 100))


print(Order.calculate_tax(1000, 5))  # Output: 50.0