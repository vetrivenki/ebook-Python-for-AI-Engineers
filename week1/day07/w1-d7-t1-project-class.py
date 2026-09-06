class Project:
    def __init__(self, name, technologies, status, impact_score):
        self.name = name
        self.technologies = technologies
        self.status = status
        self.impact_score = impact_score

    def is_completed(self):
        return self.status.lower() == "completed"

    def summary(self):
        tech_text = ", ".join(self.technologies)
        return f"{self.name} | {tech_text} | {self.status}"


project = Project(
    "AI Portfolio Analyzer",
    ["Python", "JSON"],
    "completed",
    90,
)

print(project.summary())
print("Completed:", project.is_completed())
