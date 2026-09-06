def calculate_total_value(values):
    """Return the total value of all portfolio items."""
    return sum(values)


def percentage_change(old_value, new_value):
    """Return percentage change from old value to new value."""
    if old_value == 0:
        return 0.0
    return ((new_value - old_value) / old_value) * 100


def completion_rate(projects):
    """Return the percentage of completed projects."""
    if not projects:
        return 0.0
    completed = sum(project["status"] == "completed" for project in projects)
    return (completed / len(projects)) * 100


project_values = [80, 95, 70]
projects = [
    {"name": "RAG Assistant", "status": "completed"},
    {"name": "AI Agent", "status": "in progress"},
]

print(f"Total value: {calculate_total_value(project_values)}")
print(f"Growth: {percentage_change(80, 95):.1f}%")
print(f"Completion: {completion_rate(projects):.1f}%")
