# 17.Function to Sort Variable Number of Lists
# Write a function that takes a variable number of lists and returns a single list containing all the elements, sorted.
# Input: [3, 1], [5, 2], [4, 0]
# Output: [0, 1, 2, 3, 4, 5]


def sort_multiple_lists(*lists):
    entire_list = []
    for lst in lists:
        entire_list.extend(lst)
    return sorted(entire_list)


input_lists = [
    [3, 1],
    [5, 2],
    [4, 0]
]

outputList = sort_multiple_lists(*input_lists)
print("Output:", outputList)