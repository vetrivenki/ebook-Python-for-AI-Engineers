"""AI-Powered Portfolio Analyzer: Week 1 standalone final project."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Project:
    name: str
    technologies: list[str]
    status: str
    impact_score: int


class Portfolio:
    def __init__(self, owner: str, projects: list[Project] | None = None) -> None:
        self.owner = owner
        self.projects = projects or []

    def add_project(self, project: Project) -> None:
        self.projects.append(project)

    def technologies(self) -> list[str]:
        return sorted({tech for project in self.projects for tech in project.technologies})

    def completion_rate(self) -> float:
        if not self.projects:
            return 0.0
        completed = sum(project.status.lower() == "completed" for project in self.projects)
        return completed / len(self.projects) * 100

    def recommendation(self) -> str:
        if len(self.technologies()) < 3:
            return "Add projects that demonstrate more technologies."
        if self.completion_rate() < 60:
            return "Complete more in-progress projects before adding new ones."
        return "Strong portfolio: add measurable business outcomes to every project."

    def save(self, file_path: Path) -> None:
        data = {"owner": self.owner, "projects": [asdict(item) for item in self.projects]}
        file_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, file_path: Path) -> "Portfolio":
        data = json.loads(file_path.read_text(encoding="utf-8"))
        projects = [Project(**item) for item in data.get("projects", [])]
        return cls(data.get("owner", "Unknown"), projects)

    def print_report(self) -> None:
        print("\nAI-POWERED PORTFOLIO ANALYZER")
        print("Owner:", self.owner)
        print("Total projects:", len(self.projects))
        print("Technologies:", ", ".join(self.technologies()))
        print(f"Completion rate: {self.completion_rate():.1f}%")
        print("Recommendation:", self.recommendation())


def main() -> None:
    data_file = Path(__file__).with_name("portfolio-data.json")
    portfolio = Portfolio("Venkatesan")
    portfolio.add_project(Project("Cloud Log Analyzer", ["Python", "AWS"], "Completed", 8))
    portfolio.add_project(Project("Secure RAG Assistant", ["Python", "RAG", "AWS"], "In Progress", 9))
    portfolio.add_project(Project("EKS Operations Agent", ["Python", "Kubernetes", "AI"], "Completed", 10))
    portfolio.save(data_file)

    loaded_portfolio = Portfolio.load(data_file)
    loaded_portfolio.print_report()
    print(f"Saved data: {data_file.name}")


if __name__ == "__main__":
    main()
