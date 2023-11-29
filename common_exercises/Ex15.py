# 15.Generator for Geometric Progression
# Write a generator function that yields a geometric progression with a given start, ratio, and length.
# Input: 2, 3, 4
# Output: 2, 6, 18, 54

def geometric_progression_gen(start, ratio, length):
    current = start
    counter = 0
    while counter < length:
        yield current
        current *= ratio
        counter += 1

geo_sequence = list(geometric_progression_gen(2, 3, 4))
print("Output:", ", ".join(map(str, geo_sequence)))