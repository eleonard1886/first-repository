import asyncio


async def process_request(request_id):
    print(f"Processing request {request_id}...")
    await asyncio.sleep(6)  # Simulate a time-consuming task
    print(f"Request {request_id} processed.")

async def main():
    print("Starting concurrent processing of requests...")
    result = await process_request(1)
    print(f"Final result: {result}")

asyncio.run(main())