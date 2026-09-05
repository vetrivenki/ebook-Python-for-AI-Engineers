import csv
import json

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Week 1 completed successfully.\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())

project = {
    "name": "AI Portfolio Analyzer",
    "status": "completed",
}
with open("single_project.json", "w", encoding="utf-8") as file:
    json.dump(project, file, indent=2)

with open("projects.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "status"])
    writer.writerow(["AI Portfolio Analyzer", "completed"])

print("Text, JSON, and CSV files created.")
