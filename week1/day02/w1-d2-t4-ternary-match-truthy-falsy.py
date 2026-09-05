hours = 2
message = "On track" if hours >= 2 else "Add more practice"
print(message)

level = "beginner"
match level:
    case "beginner":
        print("Start with Week 1")
    case "intermediate":
        print("Review Weeks 1-3")
    case "advanced":
        print("Focus on projects")
    case _:
        print("Enter a valid level")

projects = []
if not projects:
    print("The projects list is empty and therefore falsy")
