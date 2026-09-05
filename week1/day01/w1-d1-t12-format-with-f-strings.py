"""Format readable output using f-strings."""

name = "Venkatesan"
daily_hours = 2.5
study_days = 90
total_hours = daily_hours * study_days

print(f"{name} will study {daily_hours:.1f} hours per day.")
print(f"Total study time: {total_hours:.1f} hours")
