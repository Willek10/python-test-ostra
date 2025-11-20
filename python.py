import random

letters = "0123456789abcdef"
hexColor = ["#"]

for i in range(6):
    hexColor.append(letters[random.randint(0,15)])

print(f"Hex colour: {"".join(hexColor)}")