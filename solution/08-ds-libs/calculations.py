import numpy as np

# Part I - Berechnungen
a = np.array([20,30,40,50])
b = np.array([10,15,10,75])
c = np.array([17,12,-3,52])

x = a - b
y = x + c

print("Berechnungen:")
print("x:", x)
print("y:", y)


# Part II - 6er Reihen
r6 = np.array(range(6,66,6))
print("\n6er Reihe:", r6)

print("Minimum:",np.min(r6))
print("Maximum:",np.max(r6))
print("Mittelwert:",np.mean(r6))
print("Standardabweichung:",np.std(r6))


# Part III - Lottozahlen
print("\nLottozahlen:")
lotto = set()

while len(lotto) < 6:
    n = np.random.randint(1, 46)
    lotto.add(n)

print(lotto)

