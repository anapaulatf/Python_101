#using python built in documentation


def maximum (num1, num2):
    """
    Inputs:
    num1 - number
    num2 - number

    Output:
        Returns the larger number of num1 or num2
    """

    if num1 > num2:
        return num1
    else:
        return num2

print(maximum(3,4))

# built in function max

print(max(3,4))

def maximum2 (numbers):
    """
    Inputs:
    numbers - List of numbers

    Output:
        Returns the largest number in numbers
    """

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


### PYGAL

import pygal
import lxml

pygal.Bar()(1, 3, 3, 7)(1, 6, 6, 4).render_to_file("pygal_test.svg")
pygal.Bar()(1, 3, 3, 7)(1, 6, 6, 4).render_in_browser()
