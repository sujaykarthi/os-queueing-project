from inputs import generate_inputs
from mm1 import calculate_mm1
from queue_fcfs import FCFSQueue
from request import Request


def main():

    # -----------------------------------------
    # M/M/1 PARAMETERS
    # -----------------------------------------

    lambda_rate, mu_rate, n = generate_inputs()

    results = calculate_mm1(
        lambda_rate,
        mu_rate,
        n
    )

    print("\n========== M/M/1 MODEL ==========")
    print(f"Arrival rate (λ) : {lambda_rate}")
    print(f"Service rate (μ) : {mu_rate}")
    print(f"Number (n)       : {n}")
    print("---------------------------------")

    if not results["stable"]:
        print("Queue status     : UNSTABLE")
        print(f"ρ                : {results['rho']:.6f}")
        print("=================================\n")
        return

    print("Queue status     : STABLE")
    print(f"ρ                : {results['rho']:.6f}")
    print(f"P0               : {results['P0']:.6f}")
    print(f"Pn               : {results['Pn']:.6f}")
    print(f"L                : {results['L']:.6f}")
    print(f"Lq               : {results['Lq']:.6f}")
    print(f"W                : {results['W']:.6f}")
    print(f"Wq               : {results['Wq']:.6f}")

    # -----------------------------------------
    # FCFS QUEUE
    # -----------------------------------------

    queue = FCFSQueue()

    requests = [
        Request("R1", 0, 3),
        Request("R2", 1, 2),
        Request("R3", 2, 4),
        Request("R4", 3, 1),
        Request("R5", 4, 2)
    ]

    # Add requests to FCFS queue
    for request in requests:
        request.queue_entry_time = request.arrival_time
        queue.enqueue(request)

    print("\n========== FCFS QUEUE ==========")

    current_time = 0

    while not queue.is_empty():

        request = queue.dequeue()

        # Server waits if necessary
        if current_time < request.arrival_time:
            current_time = request.arrival_time

        # Start processing
        request.start_service(current_time)

        # Complete processing
        request.complete_service()

        current_time = request.service_completion_time

        print(
            f"{request.request_id}: "
            f"Arrival={request.arrival_time}, "
            f"Service={request.service_time}, "
            f"Start={request.service_start_time}, "
            f"Completion={request.service_completion_time}, "
            f"Waiting={request.waiting_time}, "
            f"Status={request.status}"
        )

    print("=================================\n")


if __name__ == "__main__":
    main()