import distributor.ControlGroup
from distributor.Partition import Partition


# Optimizer that takes an input a given partition and searches for anternative with a lower MinniMax (worst average
# skill difference for any pair of groups on the same skill). Candidate set are all permutations where two
# participants of the groups with currently highest Max are flipped.
def optimize(partition: Partition):
    # extract indexes of target groups:
    target_group_a = partition.groups[partition.get_max_diff().get_min_index()]
    target_group_b = partition.groups[partition.get_max_diff().get_max_index()]

    # build all permutations where exactly one team member is flipped
    for flipper_a in range(target_group_a.get_group_size()):
        for flipper_b in range(target_group_b.get_group_size()):
            # build permutation where flipper a and b are inverted
            permutation_group_a = target_group_a
            permutation_group_b = target_group_b

    return partition