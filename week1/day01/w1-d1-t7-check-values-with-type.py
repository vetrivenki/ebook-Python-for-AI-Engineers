"""Use type() to inspect values."""

values = ["Venkatesan", 20, 2.5, True]

for value in values:
    print(f"{value!r} -> {type(value).__name__}")
