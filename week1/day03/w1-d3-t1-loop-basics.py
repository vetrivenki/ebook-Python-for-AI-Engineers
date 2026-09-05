print("Numbers 1 to 5")
for number in range(1, 6):
    print(number)

skills = ["Python", "AWS", "Kubernetes"]
for skill in skills:
    print(f"Learning: {skill}")

total = 0
for number in range(1, 11):
    total += number
print(f"Sum: {total}")

for number in range(5, 0, -1):
    print(number)
print("Start learning!")

for row in range(1, 4):
    for column in range(1, 4):
        print(f"({row}, {column})", end=" ")
    print()
