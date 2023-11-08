
class Counter:

    instance_count = 0

    def __init__(self):
        Counter.instance_count += 1

    @staticmethod
    def print(action):
        print(action, "instance. Count:", Counter.instance_count)

    def __del__(self):
        type(self).instance_count -= 1

if __name__ == "__main__":
    counters = []
    for i in range(4):
        counter = Counter()
        counters.append(counter)
        Counter.print("Created")
    while len(counters) > 0:
        counter = counters.pop()
        del counter
        Counter.print("Deleted")



