# @author Forrest Wang
# Level 1.py
#
# The solution to level 1 of Google Foobar.

# Function(s):
def solution(data, n):
    # Variable(s):
    unique_elements = set(data)
    unwanted_elements = []

    # Logic:
    for element in unique_elements:
        count = data.count(element)

        if count > n:
            while element in data:
                data.remove(element)

    # Output:
    return data
