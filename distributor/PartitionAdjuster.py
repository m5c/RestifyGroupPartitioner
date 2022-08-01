## Helper class to substitute dropped out participants of an already optimized partition by backup personnel
from Participant import Participant
from distributor import Partition, ControlGroup
from invitationgen import MetaBundleFiller
from typing import List
import itertools


def extract_dropper_index(dropper: str):
    animal_name = dropper.split("-")[1]
    index = MetaBundleFiller.pseudonym_animal_list.index(animal_name.capitalize())
    return index


def extract_dropper_colour(dropper: str):
    return dropper.split("-")[0]


def mark_droppers(participants: List[Participant], partition: Partition, droppers: []):
    for group in partition.get_groups():
        # iterate over droppers and remove all that match in colour
        for dropper in droppers:
            if extract_dropper_colour(dropper) == group.get_group_name().lower():
                group.mark_dropper(extract_dropper_index(dropper))


# Replaces all participants of  a partition that carry a dropper marker by a given tuple of backup participants. Keeps
# the dropper markers for these positions, so the process can be repeated on the outcome for further permutations.
def substitute_marked_droppers(partition: Partition, permutation: tuple[Participant]):
    ## convert permutation tuple to list for conveniencet
    permutation_list = list(permutation)
    print("Current Permutation List: ")
    for participant in permutation_list:
        print(participant)

    ## iterate over partition groups
    for group in partition.get_groups():

        ## iterate over group participants
        for participant_index in range(len(group.get_participants())):

            if group.get_participants()[participant_index].is_dropper():
                group.get_participants()[participant_index] = permutation_list.pop()
                print(group.get_group_name() + "-"+str(participant_index) + " -> "+group.get_participants()[participant_index].get_name())
                group.get_participants()[participant_index].set_dropper(True)

    ## update the minimax value of the paritition (has changed, since we modified the partition configuration)
    partition.update_max_skill_diff()


# Tests all permutations where droppers have been replaced by backup partiticapants and identifies the one that
# corresponds to the MiniMax.
# That is to say it finds the one partition where all droppers have been replaced by backup personnel, that of all
# those possible ways to replace showcases the lowest diverage in average competences between groups (groups are best comparable)
def findBestBackupPermutation(partition, backup_participants):
    # First step, create all permutations
    # (See: https://stackoverflow.com/a/104436 )
    all_backup_permutations = list(itertools.permutations(backup_participants))
    print("Permutations computed!")

    # Second step, for every permutation generate partition that results of 1:1 replacement of droppers in order of iteration. Of minimax is better (lower) than previous best value, replace result partition by this one.
    mini_max_diff = 99999999
    mini_max_permutation_index = -1

    for permutation_index in range(len(all_backup_permutations)):

        # replace marked droppers by backup participants in order of current permutation
        substitute_marked_droppers(partition, all_backup_permutations[permutation_index])

        # remember this one if it is better (lower, we are looking for the MiniMax) than anything we've seen before
        partition_max_diff = partition.get_max_diff().get_diff()
        print(partition_max_diff)
        if partition_max_diff < mini_max_diff:
            mini_max_diff = partition_max_diff
            mini_max_permutation_index = permutation_index
            print("Found a better permutation: "+str(mini_max_permutation_index)+", MiniMax: "+str(mini_max_diff))

    # Third step, select the permutation with the best minimax value, replace marked participants for good, remove droppout markers.
    print("Done searching for MiniMax permutation. Best one is at index "+str(mini_max_permutation_index)+ " has MiniMax: "+str(mini_max_diff))
    return None
