from queue_fcfs import FCFSQueue


def main():
    queue = FCFSQueue()

    # Incoming requests
    requests = ["R1", "R2", "R3", "R4"]

    print("\n========== FCFS QUEUE ==========")

    # Add requests
    for request in requests:
        queue.enqueue(request)
        print(f"Added: {request}")

    print("---------------------------------")
    print(f"Queue size: {queue.size()}")
    print(f"Next request: {queue.peek()}")

    print("---------------------------------")
    print("Processing order:")

    while not queue.is_empty():
        request = queue.dequeue()
        print(f"Processing: {request}")

    print("---------------------------------")
    print(f"Queue size: {queue.size()}")
    print("=================================\n")


if __name__ == "__main__":
    main()