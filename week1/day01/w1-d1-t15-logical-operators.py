"""Combine conditions with and, or, and not."""

python_installed = True
environment_active = True
lesson_completed = False

print("Ready to code:", python_installed and environment_active)
print("Can continue:", environment_active or lesson_completed)
print("Lesson still pending:", not lesson_completed)
