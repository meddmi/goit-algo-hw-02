from dataclasses import dataclass
from itertools import count
from queue import Queue
from random import randint
from time import sleep


@dataclass
class Request:
    request_id: str


request_queue = Queue()
request_counter = count(1)


def generate_request() -> None:
    request_number = next(request_counter)
    request = Request(
        request_id=f"REQ-{request_number:03}"
    )
    request_queue.put(request)
    print(
        f"Created request {request.request_id}. "
        f"Queue size: {request_queue.qsize()}"
    )


def generate_requests_batch() -> None:
    requests_to_add = randint(1, 4)
    print(f"\nNew incoming requests: {requests_to_add}")

    for _ in range(requests_to_add):
        generate_request()


def process_request() -> None:
    if request_queue.empty():
        print("Queue is empty. No requests to process.")
        return

    request = request_queue.get()
    print(
        f"Processed request {request.request_id}. "
        f"Queue size: {request_queue.qsize()}"
    )


def main() -> None:
    print("Service center simulation started. Press Ctrl+C to stop.")

    try:
        while True:
            generate_requests_batch()
            requests_for_processing = randint(1, request_queue.qsize())
            for _ in range(requests_for_processing):
                process_request()
            sleep(1)
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")


if __name__ == "__main__":
    main()
