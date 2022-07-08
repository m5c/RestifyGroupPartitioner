# Helper class to define the Max distance observed between all groups, for one skill-specific array off average
# competence values. Each value represents one group. This is not the "Max" (defined as greatest MaxAverageDiff of ALL
# skills).
class MaxAverageDiff:

    def __init__(self, averages, skill_index):
        self.skill_index = skill_index
        self.min = min(averages)
        self.max = max(averages)
        self.diff = self.max - self.min

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max

    def get_diff(self):
        return self.diff

    def get_skill_index(self):
        return self.skill_index
