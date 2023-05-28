# @author Forrest Wang
# Level 1.py
#
# Make a function that takes in a list of numbers and a natural number n as parameters and returns the same list
# but without elements that appear more than n times.

# Function(s):
def solution(data, n):
    # Variable(s):
    unique_elements = set(data)

    # Logic:
    for element in unique_elements:
        count = data.count(element)

        if count > n:
            while element in data:
                data.remove(element)

    # Output:
    return data
