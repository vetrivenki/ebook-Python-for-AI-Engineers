study_hours = []

for day in range(1, 8):
    hours = float(input(f"Study hours for Day {day}: "))
    study_hours.append(hours)

total_hours = sum(study_hours)
average_hours = total_hours / len(study_hours)
best_day = study_hours.index(max(study_hours)) + 1

print("\n--- Weekly Study Report ---")
print(f"Total hours: {total_hours:.1f}")
print(f"Average per day: {average_hours:.1f}")
print(f"Best study day: Day {best_day}")
print(f"Target met: {total_hours >= 14}")
