from ControlGroup import ControlGroup
from DistributorInterface import DistributorInterface


class ScoreBasedDistributor(DistributorInterface):
    groups = []
    participants = []


    # Create the distributor and provide it with preliminary data. We separate initialization from the actual algorithm because other implementations may contain random elements and require multiple runs of the distribution algorithm.
    def __init__(self, p: [], group_names: str):
        self.groups = [ControlGroup(group_names[0]), ControlGroup(group_names[1]), ControlGroup(group_names[2]),
                       ControlGroup(group_names[3])]
        self.participants = p.copy()


    # Actually distribute the initialized participants into the control groups.
    # If the amount of provided participants is not a multiple of the amount of groups, the input participant list will be stripped (participants with low scores are dropped)
    def partition(self):
        overfilled = len(self.participants) % len(self.groups)
        if not overfilled == 0:
            print("Too many participants, cannot equally divide on groups. Dropping " + str(overfilled))
            for i in range(overfilled):
                self.participants.pop()
        print("Looks good, I will now distribute " + str(len(self.participants)) + " participants on " + str(len(self.groups)) + " groups...")

        # Version 1: enhanced round robin
        direction_indicator = True
        while len(self.participants) > 0:
            if direction_indicator:
                self.groups[0].add_participant(self.participants.pop())
                self.groups[1].add_participant(self.participants.pop())
                self.groups[2].add_participant(self.participants.pop())
                self.groups[3].add_participant(self.participants.pop())
            else:
                self.groups[3].add_participant(self.participants.pop())
                self.groups[2].add_participant(self.participants.pop())
                self.groups[1].add_participant(self.participants.pop())
                self.groups[0].add_participant(self.participants.pop())
            direction_indicator = not direction_indicator

        # Then print the resulting groups:
        for i in range(4):
            print(self.groups[i])

        return self.groups

