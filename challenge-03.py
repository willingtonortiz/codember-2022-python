
array = input()

items = list(map(lambda x: x[1:-1], array[1:-1].split(", ")))

longest = 2
size = 2
left = items[0]
right = items[1]
last_right = right

if left == right:
    longest = 1
    size = 1

for item in items[2:]:
    # blue, red, red
    if right == item:
        if size > longest:
            longest = size
            last_right = right
        size = 1
        left = right
        right = item
        continue

    # blue, red, blue
    if item == left:
        size += 1
        left = right
        right = item

    # blue, red, green
    else:
        if size > longest:
            longest = size
            last_right = right

        size = 2
        left = right
        right = item

if size > longest:
    longest = size
    last_right = right

print(longest, last_right)
