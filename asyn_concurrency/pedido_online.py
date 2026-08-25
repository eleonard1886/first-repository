import asyncio
import multiprocessing
import random
import time


# Async function to check if an item is available in inventory
# Returns True if available, False otherwise
async def check_item(item) -> bool:
    print(f'Checking item {item}...')
    # Simulate checking inventory by waiting 1-5 seconds
    await asyncio.sleep(random.randint(1, 5))  # Simulate a time-consuming task
    print(f'Item {item} checked.')
    # Return random result to simulate inventory check (True: available, False: not available)
    return random.choice([True, False])  # Simulate a random check result


# Async function to process payment for an order
# Simulates communicating with a payment gateway
async def pay_service(order_id):
    print(f'Processing payment for order {order_id}...')
    # Simulate payment processing delay
    await asyncio.sleep(random.randint(1, 5))  # Simulate a time-consuming task
    print(f'Payment for order {order_id} processed.')
    return True

# Synchronous function to calculate the total price of all items in an order
# Uses multiprocessing for CPU-intensive operations
def calcaulate_total(items):
    print(f'calculating total for item {len(items)}...')
    # Simulate CPU-intensive calculation with a 5-second delay
    time.sleep(5)  # Simulate a time-consuming task
    total = sum(item['price'] for item in items)
    print(f'Total for order calculated: {total}')
    return total

# Async function to orchestrate the entire order processing workflow
# Performs inventory checks, total calculation, and payment processing
async def process_order(order_id, items):
    print(f'Processing order {order_id}...')
    # Run inventory checks for all items concurrently using asyncio.gather
    # This allows multiple items to be checked simultaneously
    inventory_checks = await asyncio.gather(*(check_item(item) for item in items))
    # Verify all items are in stock before proceeding
    if not all(inventory_checks):
        print(f'Order {order_id} cannot be processed due to inventory issues.')
    # Use multiprocessing pool to run the CPU-intensive total calculation
    # This offloads blocking work to a separate process
    with multiprocessing.Pool() as pool:
        total = pool.apply(calcaulate_total, (items,))
    # Process payment asynchronously after calculating the total
    payment_result = await pay_service(order_id)
    # Confirm successful order completion if payment succeeded
    if payment_result:
        print(f'Order {order_id} processed successfully.{total}')
    else:
        print(f'Order {order_id} failed during payment processing.')

# Main async function that coordinates processing multiple orders concurrently
async def main():
    # Sample order data with order IDs and items with prices
    orders = [
        {'order_id': 1, 'items': [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}]},
        {'order_id': 2, 'items': [{'name': 'item3', 'price': 15}, {'name': 'item4', 'price': 25}]},
        {'order_id': 3, 'items': [{'name': 'item5', 'price': 30}, {'name': 'item6', 'price': 40}]}
    ]

    # Create async tasks for each order to be processed
    tasks = [process_order(order['order_id'], order['items']) for order in orders]
    # Run all order processing tasks concurrently
    # asyncio.gather waits for all tasks to complete before proceeding
    await asyncio.gather(*tasks)


# Standard Python entry point - ensures main() only runs when script is executed directly
if __name__ == "__main__":
    # Run the main async function using asyncio.run()
    asyncio.run(main())