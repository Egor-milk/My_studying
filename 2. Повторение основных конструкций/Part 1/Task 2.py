def same_parity(numbers):
    if len(numbers) > 0:
        parity = numbers[0] % 2
        return list(filter(lambda x: x % 2 == parity, numbers))
    else:
        return []


print(same_parity([-1, 1248234832443, 8]))
