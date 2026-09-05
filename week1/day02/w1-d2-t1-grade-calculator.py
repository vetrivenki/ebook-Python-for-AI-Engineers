score = float(input("Enter score (0-100): "))

if score < 0 or score > 100:
    grade = "Invalid score"
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
