import threading
import time


def process_request(request_id):
    print(f"Processing request {request_id}...")
    time.sleep(2)  # Simulate a time-consuming task
    print(f"Request {request_id} processed.")


threads = []
for i in range(5):
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All requests have been processed.") 