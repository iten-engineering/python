import numpy as np

print("Lotto:")
lotto = set()

while len(lotto) < 7:
    n = np.random.randint(1,46)
    lotto.add(n)

print(lotto)
