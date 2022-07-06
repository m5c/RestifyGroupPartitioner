class Participant:
    # name = ""
    # skills = []

    def __init__(self, n, s):
        self.name = n
        self.skills = s

    def compute_total_score(self):
        return sum(self.skills)

    def __str__(self):
        participant_str = self.name + ": ["
        for skill in self.skills:
            participant_str += str(skill) + ","
        participant_str += "]"
        return participant_str
