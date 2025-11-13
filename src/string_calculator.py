import re


def add(numbers: str) -> int:
    if numbers == "":
        return 0
    if numbers.isdigit():
        return int(numbers)

    check_for_separators = re.split("[,\n]+", numbers)
    separators = find_separators(check_for_separators)

    strings_of_numbers = re.split("[" + separators + "]+", numbers.replace("//", "")
                                  .replace("[", "").replace("]", ""))
    strings_without_separators = (
        filter(lambda y: not y.startswith("//") and y not in separators, strings_of_numbers))
    numbers = list(filter(lambda z: z <= 1000, map(lambda x: int(x), strings_without_separators)))

    negative_numbers = list(filter(lambda n: n < 0, numbers))
    if len(negative_numbers) > 0:
        message = "String contains negative numbers: " + str(negative_numbers[0])
        for n in negative_numbers:
            if n != negative_numbers[0]:
                message = message + ", " + str(n)
        raise ValueError(message)

    return sum(numbers)


def find_separators(check_for_separators: list[str]) -> str:
    separators = ",\n"
    for s in check_for_separators:
        if s.startswith("//"):
            separators = separators + s.replace("//", "").replace("[", "").replace("]", "")
    return separators
