text = "python ai python aws ai python"
frequency = {}

for word in text.split():
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

scores = {"RAG": 95, "Agent": 88, "API": 78}
strong_projects = {name: score for name, score in scores.items() if score >= 85}
print(strong_projects)
