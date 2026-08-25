from enum import Enum


class OrderStatus(Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELED = "canceled"

def check_order_status(status: OrderStatus) -> str:

    if status == OrderStatus.PENDING:
        return "The order is pending."
    elif status == OrderStatus.SHIPPED:
        return "The order has been shipped."
    elif status == OrderStatus.DELIVERED:
        return "The order has been delivered."
    elif status == OrderStatus.CANCELED:
        return "The order has been canceled."


print(check_order_status(OrderStatus.PENDING))