projects = ["RAG Assistant", "Cloud Agent"]
projects.append("Portfolio Analyzer")
projects.extend(["ML API", "Cost Predictor"])
projects.insert(1, "Log Analyzer")

print(projects[0])
print(projects[1:3])

projects.remove("ML API")
removed = projects.pop()
projects.sort()

long_names = [name for name in projects if len(name) > 10]

print("Sorted projects:", projects)
print("Removed:", removed)
print("Long names:", long_names)
