def add_numbers(a, b):
    """
    Add two numbers and return the result.

    :param a: The first number.
    :param b: The second number.
    :return: The sum of 'a' and 'b'.
    """
    return a + b


if __name__ == "__main__":
    # Code inside this block will only run
    # when the script is executed directly,
    # not when it's imported as a module.
    num1 = 5
    num2 = 7
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")
