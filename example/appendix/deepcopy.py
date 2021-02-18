import copy

print("# Copy with: =")
old = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new = old

new[2][2] = 9

print('Old list:', old, "with ID", id(old) )
print('New list:', old, "with ID", id(new) )

print()
print("# Copy with: copy")
old = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new = copy.copy(old)

new[2][2] = 9

print('Old list:', old, "with ID", id(old) )
print('New list:', old, "with ID", id(new) )

print()
print("# Copy with: deepcopy")
old = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new = copy.deepcopy(old)

new[2][2] = 9

print('Old list:', old, "with ID", id(old) )
print('New list:', old, "with ID", id(new) )
