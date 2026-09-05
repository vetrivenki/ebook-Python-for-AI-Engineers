level = input("Python level (new/beginner/intermediate/advanced): ").lower()
knows_ml = input("Do you know machine learning basics? (yes/no): ").lower()
knows_llm = input("Have you built an LLM application? (yes/no): ").lower()

if level in ("new", "beginner"):
    focus = "Week 1: Python fundamentals"
elif level == "intermediate" and knows_ml == "no":
    focus = "Weeks 3-4: Data and machine learning"
elif knows_llm == "no":
    focus = "Weeks 5-7: Deep learning, NLP, and LLMs"
else:
    focus = "Weeks 8-12: RAG, agents, deployment, and system design"

print(f"Recommended focus: {focus}")
