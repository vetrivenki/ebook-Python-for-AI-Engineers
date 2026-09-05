portfolio = {
    "owner": "Venkatesan",
    "target_role": "AI Platform Engineer",
    "projects": {
        "portfolio_analyzer": {
            "name": "AI-Powered Portfolio Analyzer",
            "tech_stack": ["Python", "JSON"],
            "status": "completed",
            "impact": "Organizes and analyzes engineering projects",
        },
        "cloud_agent": {
            "name": "AWS Operations AI Agent",
            "tech_stack": ["Python", "AWS", "LLM"],
            "status": "in progress",
            "impact": "Improves incident investigation",
        },
    },
}

for project_id, project in portfolio["projects"].items():
    print(f"\nID: {project_id}")
    print(f"Name: {project['name']}")
    print(f"Technology: {', '.join(project['tech_stack'])}")
    print(f"Status: {project['status']}")
    print(f"Impact: {project['impact']}")
