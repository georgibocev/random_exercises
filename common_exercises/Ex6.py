# Write a generator function that yields prime numbers up to numbers up to n
# Input: 10
# Output: 2, 3, 5, 7

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generator_prime(n):
    num = 2
    while num <= n:
        if is_prime(num):
            yield num
        num += 1

num_input = 10
output_num = list(generator_prime(num_input))
print("Output:", ", ".join(map(str, output_num)))