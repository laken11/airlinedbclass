def prompt_for_valid_input(prompt: str, check):
    while True:
        entry = input(prompt)
        if check(entry):
            break
    return entry


def prompt_for_valid_integer_input(prompt: str) -> int:
    return int(prompt_for_valid_input(prompt, __check_valid_integer))


def prompt_for_non_empty_string_input(prompt: str) -> str:
    return prompt_for_valid_input(prompt, __check_non_empty_string)


def __check_valid_integer(obj):
    try:
        int(obj)
        return True
    except ValueError:
        return False


def __check_non_empty_string(obj):
    return len(str(obj).strip()) != 0


def __check_within_range(obj, min: int, max: int):
    if not __check_valid_integer(obj):
        return False

    value = int(obj)
    return min < value < max
