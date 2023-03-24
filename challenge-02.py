
input_value = input()
words = input_value.split(" ")

sentence = ""

for word in words:
    it = 0
    while True:
        if it > len(word) - 1:
            break

        letter = ""
        if word[it] in ["3", "4", "5", "6", "7", "8", "9"]:
            letter = word[it:it + 2]
            it += 2
        else:
            letter = word[it:it + 3]
            it += 3

        sentence += chr(int(letter))

    sentence += " "

print(sentence)
