import random

def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> list[int]:
    """Generate a list of unique random numbers within a specified range."""
    if min_val < 1:
        return []

    if max_val > 1000:
        return []

    if min_val > max_val:
        return []

    if quantity < 1:
        return []
    range_size = max_val - min_val + 1
    if quantity <= range_size:
        sample_list = random.sample(range(min_val, max_val + 1), quantity)
        return sorted(sample_list)
    else:
        return []
    
print("Ваші лотерейні числа:", get_numbers_ticket(1, 49, 6))
print("Ваші лотерейні числа:", get_numbers_ticket(1, 49, 6))
print("Ваші лотерейні числа:", get_numbers_ticket(0, 49, 6))
print("Ваші лотерейні числа:", get_numbers_ticket(1, 1001, 6))
print("Ваші лотерейні числа:", get_numbers_ticket(1, 5, 6))
print("Ваші лотерейні числа:", get_numbers_ticket(5, 5, 1))
print("Ваші лотерейні числа:", get_numbers_ticket(1, 49, 0))