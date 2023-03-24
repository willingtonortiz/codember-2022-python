from sys import stdin


valid_users = 0
user = {}
users = set()
valid_keys = ["usr", "eme", "psw", "age", "loc", "fll"]
last_user = {}


def is_valid_user(user):
    for valid_key in valid_keys:
        if valid_key not in user:
            return False
    return True


for line in stdin:
    if line == '':
        break

    props = line.split(" ")
    if props[0] == "\n":
        is_valid = is_valid_user(user)
        username = user["usr"]
        if is_valid:
            users.add(username)
            valid_users += 1

        last_user = user
        user = {}
        continue

    for prop in props:
        key, value = prop.split(":")
        user[key] = value

# print(valid_users, users)
print(f"{valid_users}{last_user['usr']}")
