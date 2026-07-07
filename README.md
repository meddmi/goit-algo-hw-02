# goit-algo-hw-02

Homework assignment on working with queues in Python.

## Project Structure

- `task1.py` - a simulation of request processing in a service center using `Queue` from the `queue` module.
- `task2.py` - a palindrome checker using `deque` from the `collections` module.

## Task 1

The program simulates the work of a service center:

- automatically creates new requests;
- adds them to a queue;
- processes requests in the order they arrive;
- displays the current queue size;
- stops after pressing `Ctrl+C`.

Each request gets a unique identifier in the format `REQ-001`, `REQ-002`, and so on.

### Run

```bash
python3 task1.py
```

## Task 2

The program contains the `is_palindrome()` function, which:

- takes a string as input;
- converts it to lowercase;
- ignores spaces;
- adds the characters to a double-ended queue `deque`;
- compares characters from both ends of the queue;
- determines whether the string is a palindrome.

The solution works correctly for both even- and odd-length strings.

### Run

```bash
python3 task2.py
```

## Requirements

- Python 3.x
- Standard Python modules: `queue`, `collections`, `dataclasses`, `itertools`, `time`
