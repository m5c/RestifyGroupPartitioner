class Participant:
    name = ""
    skills = []

    def __init__(self, n, s):
        self.name = n
        self.skills = s

    def compute_total_score(self):
        return sum(self.skills)
