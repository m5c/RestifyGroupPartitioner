from distributor.ControlGroup import ControlGroup
from distributor.DistributorInterface import DistributorInterface


# Adds one batch of participants to the target groups
# Removes them from the received list.
# Since participants are sorted, the function first orders the target groups by their current total score, to give the
# most powerful user to the currenlty weakest target group and so on.
from distributor.Partition import Partition


def distibute_batch(participants, groups):
    groups = sorted(groups, key=lambda g: g.get_group_score(), reverse=True)
    groups[0].add_participant(participants.pop())
    groups[1].add_participant(participants.pop())
    groups[2].add_participant(participants.pop())
    groups[3].add_participant(participants.pop())


# This class distributes participants into control groups using the following algorithm
# * Only the total score of a participant / group is taken into consideration
# * Participants are ordered by their total score
# * If the amount of participants is not a multiple of the amount of target groups, the weakest participants are removed until this holds
# * Participants are distributed batch wise: each batch has as many participants as their are groups
# * The target groups are sorted based on their current total skill
# Reason: The later participants per batch are always stronger than the earlier ones. By arangeing the target groups inversely, the strong participants always end up where they are needed the most.
class ScoreBasedDistributor(DistributorInterface):

    # Create the distributor and provide it with preliminary data. We separate initialization from the actual algorithm because other implementations may contain random elements and require multiple runs of the distribution algorithm.
    def __init__(self, p: [], group_names: str):
        self.groups = [ControlGroup(group_names[0], []), ControlGroup(group_names[1], []), ControlGroup(group_names[2], []),
                       ControlGroup(group_names[3], [])]
        self.participants = p.copy()

    # Actually distribute the initialized participants into the control groups.
    # If the amount of provided participants is not a multiple of the amount of groups, the input participant list will be stripped (participants with low scores are dropped)
    def partition(self):
        overfilled = len(self.participants) % len(self.groups)
        if not overfilled == 0:
            print("Too many participants, cannot equally divide on groups. Dropping " + str(overfilled))
            for i in range(overfilled):
                self.participants.pop()
        print("Looks good, I will now distribute " + str(len(self.participants)) + " participants on " + str(
            len(self.groups)) + " groups...")

        # Version 1: enhanced round robin
        # direction_indicator = True
        while len(self.participants) > 0:
            distibute_batch(self.participants, self.groups)

        # Then print the resulting groups:
        for i in range(4):
            print(self.groups[i])

        return Partition(self.groups)
