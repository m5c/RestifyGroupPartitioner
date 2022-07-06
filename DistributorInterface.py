import Participant


class DistributorInterface:

    def partition(self, participants: list[Participant], amount_control_groups: int) -> list[Participant]:
        """Load in a list of participants and the amount of control groups to run a distribution."""
        pass
