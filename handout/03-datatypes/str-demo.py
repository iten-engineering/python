words = "cheese, spam, egg, spam, bacon, spam"
sorted_words = sorted(words.split(", "))
print(sorted_words)

sorted_words = ", ".join(sorted_words)
print(sorted_words)