# Description: Implement a generator that behaves like the built-in zip function, taking two or more iterables and returning tuples.
# Example Input: [1, 2], [3, 4]
# Example Output: (1, 3), (2, 4)

def custom_zip(*iterables):
    iterators = [iter(it) for it in iterables]
    while iterators:
        try:
            yield tuple(next(it) for it in iterators)
        except StopIteration:
            break


list1 = [1, 2]
list2 = [3, 4]

for element in custom_zip(list1, list2):
    print(element)