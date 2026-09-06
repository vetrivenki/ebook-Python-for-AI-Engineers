course_name = "Python for AI Engineers"


def greet(name, message="Keep learning"):
    local_text = f"{name}: {message}"
    return local_text


def total_values(*values):
    return sum(values)


def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


projects = [
    {"name": "RAG Assistant", "impact": 85},
    {"name": "Cloud Agent", "impact": 95},
]
projects.sort(key=lambda item: item["impact"], reverse=True)

print(greet("Venkatesan"))
print(total_values(10, 20, 30))
show_profile(role="AI Platform Engineer", cloud="AWS")
print(projects)
print(course_name)
