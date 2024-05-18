

def number_to_word(number:int)-> str:
    """
    Function converts an integer into words.

    :param int num: The number to be converted to words.
    :return: The word representation of the number.
    :rtype: str
    >>> number_to_word(257)
    Two Hundred Fifty Seven
    >>> number_to_word(600000)
    Six Hundred Thousand
    >>> number_to_word(1000000)
    One Million
    """

    # If the number is less than 20, use direct mapping.
    if number < 20:
        return UNDER_20[number]
    
    # If the number is less than 100, calculate tens and ones separately.
    elif number < 100:
        n1 = number % 10
        return TENS[(number // 10) - 2] + ("" if n1 == 0 else " " + UNDER_20[n1])
    
    # For numbers 100 and above, calculate words recursively.
    else:

        pivot = [key for key in ABOVE_100 if key<=number][-1]
        p1 = number_to_word(number // pivot)
        p2 = ABOVE_100[pivot]
        if number % pivot == 0:
            return f'{p1} {p2}'
        p3 = number_to_word(number % pivot)
        return f'{p1} {p2} {p3}'

UNDER_20 = [
    "Zero", "One", "Two", "Three", "Four",
    "Five", "Six", "Seven", "Eight", "Nine",
    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
    "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen",
]

TENS = [
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety",
]

ABOVE_100 = {
    100: "Hundred",
    1000: "Thousand",
    1000000: "Million",
    1000000000: "Billion",
}


if __name__ == "__main__":
    # Get number from user.
    number = int(input("Enter a Number: "))
    # Check if number is in acceptable range.
    if number >= 0 and number <= 999_999_999_999:
        # Print number in words.
        print(number_to_word(number))
    else:
        print("Number out of range")
