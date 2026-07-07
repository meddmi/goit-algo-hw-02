from collections import deque


def normalize_string(text: str) -> str:
    return "".join(text.lower().split())


def is_palindrome(s: str) -> bool:
    normalized_string = normalize_string(s)
    char_queue = deque(normalized_string)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True


def main() -> None:
    test_strings = [
        "Never odd or even",
        "Test",
        "Able was I ere I saw Elba",
        "A Toyota",
        "No lemons no melon",
        "Hello world",
        "Python programming"
    ]

    for test in test_strings:
        result = is_palindrome(test)
        print(f"\n'{test}' -> palindrome: {result}")


if __name__ == "__main__":
    main()
