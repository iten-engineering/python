
def plot(values, title="Values"):
    print(title)
    print(values)

values = [1,5,77,99]
plot(values)
plot(values, title="Lotto Numbers:")


def calculations(values):
    """Calculate sum and mean of the given values.
    Args:
        values (list of numbers)
    Return:
        sum - The sum of all values
        mean - The mean of all list values
    """
    res_sum = sum(values)
    res_mean = res_sum / len(values)
    return res_sum, res_mean

res_sum, res_mean = calculations(values)
print(res_sum)
print(res_mean)

