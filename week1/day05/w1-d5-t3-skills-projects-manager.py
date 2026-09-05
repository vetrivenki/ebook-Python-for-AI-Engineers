skills = []
projects = []

skills.extend(["Python", "AWS", "RAG", "Python"])
projects.extend([
    ("AI Portfolio Analyzer", "in progress"),
    ("Cloud Operations Agent", "planned"),
    ("Log Analyzer", "completed"),
])

unique_skills = sorted(set(skills))
completed_projects = [
    name for name, status in projects if status == "completed"
]

print("--- Skills ---")
for skill in unique_skills:
    print(skill)

print("\n--- Projects ---")
for name, status in projects:
    print(f"{name}: {status}")

print("\nCompleted projects:", completed_projects)
