experience = int(input("Years of technical experience: "))
likes_data = input("Do you like data work? (yes/no): ").lower() == "yes"
likes_cloud = input("Do you like cloud platforms? (yes/no): ").lower() == "yes"

if experience >= 5 and likes_cloud:
    role = "AI Platform Engineer"
elif likes_data:
    role = "Machine Learning Engineer"
else:
    role = "Python AI Application Developer"

print(f"Recommended role: {role}")
