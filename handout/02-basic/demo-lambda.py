
def apply(values, f):
    results = []
    for value in values:
        result = f(value)
        results.append(result)
    return results

values = [12, -14, 20]
print(values)

results = apply(values, lambda v: 2 * v)
print(results)

results = apply(values, lambda v: v-10)
print(results)

results = apply(values, abs)
print(results)
