"""Convert numeric strings to int and float."""

age_text = "45"
hours_text = "2.5"

age = int(age_text)
daily_hours = float(hours_text)

print("Age:", age, type(age))
print("90-day hours:", daily_hours * 90)
