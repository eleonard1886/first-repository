from collections import deque


def manage_delivery_queue(orders: list[str]) -> deque:
    # Crea una cola de entrega utilizando deque
    delivery_queue = deque(["order_1", "order_2", "order_3", "order_4", "order_5"])
    delivery_queue.append("order_6")  # Agrega un nuevo pedido al final de la cola
    delivery_queue.appendleft("order_0")  # Agrega un nuevo pedido al inicio de la cola
    delivery_queue.pop()  # Elimina el último pedido de la cola
    delivery_queue.popleft()  # Elimina el primer pedido de la cola
    return delivery_queue
    