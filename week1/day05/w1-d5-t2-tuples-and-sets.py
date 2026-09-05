project_score = ("RAG Assistant", 95)
project_name, score = project_score
print(project_name, score)

cloud_skills = {"AWS", "Python", "Kubernetes"}
ai_skills = {"Python", "PyTorch", "RAG"}

print("All skills:", cloud_skills | ai_skills)
print("Common skills:", cloud_skills & ai_skills)
print("Cloud-only skills:", cloud_skills - ai_skills)

skills_with_duplicates = ["Python", "AWS", "Python", "RAG"]
unique_skills = sorted(set(skills_with_duplicates))
print("Unique skills:", unique_skills)
