class Participant:
    # name = ""
    # skills = []

    def __init__(self, n, s):
        self.name = n
        self.skills = s
        self.dropper = False

    def set_dropper(self, status: bool):
        self.dropper = status

    def get_skills(self) -> list[int]:
        return self.skills

    def is_dropper(self):
        return self.dropper

    def compute_total_score(self):
        return sum(self.skills)

    def get_skill_amount(self):
        return len(self.skills)

    def get_name(self):
        return self.name

    def __str__(self):
        participant_str = self.name + ": ["
        for skill in self.skills:
            participant_str += str(skill) + ","
        participant_str += "]"
        return participant_str
