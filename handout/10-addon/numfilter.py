
def numfilter(input_list):
    """Filter mit Hilfe von isinstance."""
    return [x for x in input_list if isinstance(x, (int, float)) and not isinstance(x, bool)]


def numfilter2(input_list):
    """Filter mit Hilfe von Cast, nimmt auch Texte die Nummern darstellen, wie z.B. '100'."""
    numbers = []
    for x in input_list:
        try:
            number = float(x)
            numbers.append(number)
        except:
            continue
    return numbers


# Example usage
input_list = [10, "hello", None, 25.5, "n/a", 42, False, "100", 0, float('nan')]

# Apply the filter
filtered_list = numfilter(input_list)
print("Filtered list 1:", filtered_list)

filtered_list = numfilter2(input_list)
print("Filtered list 2:", filtered_list)

# Filter mit cast
#

