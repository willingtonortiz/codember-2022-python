
start = 11098
end = 98123

def has_two_fives(num):
    num_str = str(num)
    return num_str.count("5") >= 2

def has_ascencing_digits(num):
    num_str = str(num)
    for i in range(len(num_str) - 1):
        if num_str[i] > num_str[i + 1]:
            return False
    return True

def is_valid(num):
    return has_two_fives(num) and has_ascencing_digits(num)

counter = 0
number_56 = 0
for num in range(start, end + 1):
    if is_valid(num):
        counter += 1
        if counter == 56:
            number_56 = num

print(f"{counter}-{number_56}")
