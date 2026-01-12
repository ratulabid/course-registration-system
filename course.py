class Course:
    def __init__(self, title, code, credits, prerequisite):
        self.title = title
        self.code = code
        self.credits = int(credits)
        self.prerequisite = prerequisite.strip()

    def __str__(self):
        pre = self.prerequisite if self.prerequisite else "None"
        return f"{self.code} | {self.title} | Credits: {self.credits} | Prerequisite: {pre}"
