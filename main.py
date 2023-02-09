import os
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text: str) -> int:
    opening_brackets_stack: list = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            if len(opening_brackets_stack) != 0:
                if are_matching(opening_brackets_stack[-1], next):
                    opening_brackets_stack.pop()
                else:
                    return i + 1
            else:
                return i + 1
            pass

    return 0


def main():
    method: str = input("Input method I - manual input, F - files: ")[0]
    match method:
        case "I":
            text: str = input("Input text: ")
            mismatch: int = find_mismatch(text)
            print(mismatch if mismatch != 0 else "Success")
        case "F":
            file_path: str = "test/"
            i: int = 0
            while os.path.isfile(file_path + str(i)):
                with open(file_path + str(i), 'r') as file:
                    text = file.read().rstrip()
                    result: str = find_mismatch(text) if find_mismatch(text) != 0 else "Success"
                with open(file_path + str(i) + ".a", 'r') as file:
                    answer: str = file.read().rstrip()
                if str(result) == str(answer):
                    print(f"-> Test {i} passed")
                else:
                    print(f"-> Test {i} failed: expected {answer}, result {result}")

                i += 1


if __name__ == "__main__":
    main()
