from ParticipantStatTools import build_mean_skills
from distributor.MaxAverageDiff import MaxAverageDiff


# Represents a partition of the overall participant list into a given amount fo control groups. Objects of this type
# also inherently store the associated "Max" statistical data. See "compute_max_offset", which provides a metric for
# comparing partition qualities.
class Partition:

    def get_skill_amount(self):
        return self.groups[0].get_skill_amount()

    # Computes the "Max" defined as the greatest difference in average skill competences, same skill, different groups
    # In general partitions with lower Max are favourable over partitions with a higher Max.
    def compute_max_offset(self):
        # build the average skill vector, indexed by group
        group_skill_averages = []
        for group in self.groups:
            group_skill_averages.append(build_mean_skills(group.get_participants()))

        # iterate over above skill vectors and determine min and max per group. Save the greatest differences observed
        # per skill
        all_average_diffs = []
        for skill_index in range(self.get_skill_amount()):

            # build averages for ONE skill, for all groups
            skill_group_averages = []
            for group_index in range(len(self.groups)):
                skill_group_averages.append(group_skill_averages[group_index][skill_index])

            all_average_diffs.append(MaxAverageDiff(skill_group_averages, skill_index))

        # Return the actual "Max", defined as the greatest difference in skill competences, for the same skill within
        # a partition.
        return all_average_diffs

    def __init__(self, groups: []):
        self.groups = groups
        self.average_diffs = self.compute_max_offset()
        self.max_average_diff = max(self.average_diffs, key=lambda m: m.diff)

    def get_groups(self):
        return self.groups

    def get_average_diffs(self):
        return self.average_diffs

    def get_max_diff(self):
        return self.max_average_diff

    def get_group_size(self):
        return self.groups[0].get_group_size()
