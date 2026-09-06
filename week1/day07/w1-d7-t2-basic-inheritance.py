class Project:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Project: {self.name}"


class AIProject(Project):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

    def describe(self):
        return f"AI Project: {self.name} | Model: {self.model}"


project = AIProject("Incident Assistant", "Claude")
print(project.describe())
