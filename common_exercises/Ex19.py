# Description: Create a generator that takes a nested list and flattens it.
# Example Input: [[1, 2], [3, 4]]
# Example Output: 1, 2, 3, 4

def gen_flatten_nested_list(nested_list):
    for sublist in nested_list:
        for element in sublist:
            yield element

example_input = [[1, 2], [3, 4]]

for el in gen_flatten_nested_list(example_input):
    print(el, end=' ')