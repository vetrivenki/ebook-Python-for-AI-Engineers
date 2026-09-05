def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def positive_number(prompt):
    while True:
        value = float(input(prompt))
        if value >= 0:
            return value
        print("Please enter zero or a positive number.")

temperature = fahrenheit_to_celsius(86)
hours = positive_number("Study hours: ")

print(f"Temperature: {temperature:.1f} C")
print(f"Study hours: {hours:.1f}")
