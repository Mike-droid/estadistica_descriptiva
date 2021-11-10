import random

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


random_numbers = [random.randint(1, 100) for _ in range(100)]

print(f'La media de {random_numbers} es {calculate_mean(random_numbers)}')