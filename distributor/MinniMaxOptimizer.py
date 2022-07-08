from distributor.ControlGroup import ControlGroup
from distributor.Partition import Partition


# Optimizer that takes an input a given partition and searches for anternative with a lower MinniMax (worst average
# skill difference for any pair of groups on the same skill). Candidate set are all permutations where two
# participants of the groups with currently highest Max are flipped.
def optimize_once(partition: Partition):
    # extract indexes of target groups:
    target_group_a_index = partition.get_max_diff().get_min_index()
    target_group_b_index = partition.get_max_diff().get_max_index()
    target_group_a = partition.groups[target_group_a_index]
    target_group_b = partition.groups[target_group_b_index]

    # current partition might already be better than all future permutations, so we store it in the target collection.
    permutations = []
    permutations.append(partition)

    # build all permutations where exactly one team member is flipped
    for flipper_a_index in range(target_group_a.get_group_size()):
        for flipper_b_index in range(target_group_b.get_group_size()):
            # build permutation where flipper a and b are inverted
            # remove what is to be removed
            permutation_group_a = target_group_a.get_participants().copy()
            flipper_a = permutation_group_a[flipper_a_index]
            del permutation_group_a[flipper_a_index]
            permutation_group_b = target_group_b.get_participants().copy()
            flipper_b = permutation_group_b[flipper_b_index]
            del permutation_group_b[flipper_b_index]

            # add again to the other group, mutually
            permutation_group_a.append(flipper_b)
            permutation_group_b.append(flipper_a)

            # finally, create a new partition, based on the new permutations.
            permutation_groups = []
            permutation_groups.append(
                ControlGroup(partition.get_groups()[target_group_a_index].get_group_name(), permutation_group_a))
            permutation_groups.append(
                ControlGroup(partition.get_groups()[target_group_b_index].get_group_name(), permutation_group_b))
            remaining_groups = [0, 1, 2, 3]
            remaining_groups.remove(target_group_a_index)
            remaining_groups.remove(target_group_b_index)
            for index in remaining_groups:
                permutation_groups.append(ControlGroup(partition.get_groups()[index].get_group_name(),
                                                       partition.groups[index].get_participants().copy()))

            # Create an actual new partition for these groups
            permutations.append(Partition(permutation_groups))

    # find the one permutation that is considered best (use MiniMax criteria here)
    miniMax = min(permutations, key=lambda m: m.get_max_diff().get_diff())
    return miniMax


def optimize(partition):
    stable = False
    print("Optimizing partitions. Current Max: "+str(partition.get_max_diff().get_diff()))
    while not stable:
        optimized = optimize_once(partition)
        stable = optimized == partition
        partition = optimized
        print("Searched for a better partition testing permutations for MiniMax. Current Max now: "+str(partition.get_max_diff().get_diff()))
    print("Last search for better permutation did not lead to an improvement. Stopping search for optimization.")
    return partition
