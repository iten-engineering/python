import numpy as np

lotto = set()

while len(lotto) < 6:
    n = np.random.randint(1,46)
    lotto.add(n)

print("Lottozahlen:")
print(lotto)