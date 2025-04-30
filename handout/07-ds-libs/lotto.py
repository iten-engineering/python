import numpy as np

lotto_numbers = set()

while len(lotto_numbers) < 6:
    number = np.random.randint(1,46)
    lotto_numbers.add(number)

print(lotto_numbers)