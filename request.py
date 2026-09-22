class Request:
    """
    Represents one incoming application request.
    """

    def __init__(self, request_id, arrival_time, service_time):
        self.request_id = request_id
        self.arrival_time = arrival_time
        self.service_time = service_time

        self.queue_entry_time = None
        self.service_start_time = None
        self.service_completion_time = None
        self.waiting_time = None
        self.status = "WAITING"

    def start_service(self, current_time):
        self.service_start_time = current_time
        self.waiting_time = (
            self.service_start_time - self.arrival_time
        )
        self.status = "PROCESSING"

    def complete_service(self):
        self.service_completion_time = (
            self.service_start_time + self.service_time
        )
        self.status = "COMPLETED"

    def __str__(self):
        return (
            f"{self.request_id} | "
            f"Arrival={self.arrival_time} | "
            f"Service={self.service_time} | "
            f"Waiting={self.waiting_time}"
        )