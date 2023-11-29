# Description: Create a generator function that mimics the built-in range function. It should accept start, stop, and step arguments.
# Example Input: custom_range(2, 10, 2)
# Example Output: 2, 4, 6, 8

def custom_range(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step

start = 2
stop = 10
step = 2

for element in custom_range(start, stop, step):
    print(element, end= ' ')