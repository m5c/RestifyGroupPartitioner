from ParticipantStatTools import build_mean_skills
from MaxAverageDiff import MiniMaxAverage


class Partition:

    def get_skill_amount(self):
        return self.groups[0].get_skill_amount()


    def compute_max_offset(self):
        # build the average skill vector, indexed by group
        group_skill_averages = []
        for group in self.groups:
            group_skill_averages.append(build_mean_skills(group.get_participants()))

        # iterate over above skill vectors and determine min and max per group. Save the difference
        max_offset = 0.0
        for skill_index in range(self.get_skill_amount()):

            # build averages for ONE skill, for all groups
            skill_group_averages = []
            for group_index in range(len(self.groups)):
                skill_group_averages.append(group_skill_averages[group_index][skill_index])

            MaxAverage(skill_group_averages)
        return max_offset

    def __init__(self, groups: []):
        self.groups = groups
        self.max_offset = self.compute_max_offset()

    def get_groups(self):
        return self.groups

    def get_max_offset(self):
        return self.max_offset
