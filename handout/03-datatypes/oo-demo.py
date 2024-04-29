
# index=0123456789
date = "29.04.2024"

index_list = []
start = 0

while(True):
    try:
        i = date.index(".", start)
        index_list.append(i)
        start = i + 1
    except:
        break

print(index_list)
