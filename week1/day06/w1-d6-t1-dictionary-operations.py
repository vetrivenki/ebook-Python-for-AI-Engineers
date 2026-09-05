project = {
    "name": "AI Portfolio Analyzer",
    "status": "in progress",
    "impact": 90,
}

print(project["name"])
print(project.get("owner", "Not assigned"))

project["owner"] = "Venkatesan"
project["status"] = "completed"
del project["impact"]

print("Keys:", list(project.keys()))
print("Values:", list(project.values()))

for key, value in project.items():
    print(f"{key}: {value}")
