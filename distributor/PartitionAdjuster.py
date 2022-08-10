## Helper class to substitute dropped out participants of an already optimized partition by backup personnel
import SelfScoreFileParser
from Participant import Participant
from distributor import Partition, ControlGroup
from invitationgen import MetaBundleFiller
from typing import List
import itertools


def extract_codename_index(dropper: str):
    animal_name = dropper.split("-")[1]
    index = MetaBundleFiller.pseudonym_animal_list.index(animal_name.capitalize())
    return index


def extract_codename_colour(dropper: str):
    return dropper.split("-")[0]


def mark_droppers(partition: Partition, droppers: []):
    for group in partition.get_groups():
        # iterate over droppers and remove all that match in colour
        for dropper in droppers:
            if extract_codename_colour(dropper) == group.get_group_name().lower():
                group.mark_dropper(extract_codename_index(dropper))

def patch_participant_list(participants: List[Participant], backup: List[Participant]):
    # also replace droppers by backup personnel in original list
    non_droppers = []
    for participant in participants:
        if not participant.is_dropper():
            non_droppers.append(participant)
    participants.clear()
    participants.extend(non_droppers)

    for participant in backup:
        participants.append(participant)

    # sort again, so participants are in order, descending total skill
    SelfScoreFileParser.sortByTotalScore(participants)


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
    # revert to the optimum
    substitute_marked_droppers(partition, all_backup_permutations[mini_max_permutation_index])

    return None

## Flips the partition associations and code names of a pair of participants
def flip(flipper_name_1 : str, flipper_name_2 : str, partition: Partition):

    # extract target group and index for both flippers
    colour_1 = extract_codename_colour(flipper_name_1)
    index_1 = extract_codename_index(flipper_name_1)
    colour_2 = extract_codename_colour(flipper_name_2)
    index_2 = extract_codename_index(flipper_name_2)

    control_group_1 = partition.get_group_by_colour(colour_1)
    control_group_2 = partition.get_group_by_colour(colour_2)
    flipper_1 = control_group_1.get_participants()[index_1]
    flipper_2 = control_group_2.get_participants()[index_2]

    ## Reassign group members, flipped
    control_group_1.get_participants()[index_1] = flipper_2
    control_group_2.get_participants()[index_2] = flipper_1

    ## print stats of changed max_diff
    partition.update_max_skill_diff()
    max_diff = partition.get_max_diff().get_diff()
    print("Flipped colourblind participants. New max-diff is: "+str(max_diff))


# Replaces a targeted code name by a fallfallback replacer index
def singelDropperReplacer(dropper_code_name: str, index: int, partition: Partition, participants: List[Participant]):

    # extract target group and index for dropper
    dropper_colour = extract_codename_colour(dropper_code_name)
    dropper_index = extract_codename_index(dropper_code_name)

    # Import data of replacement participant
    replacement = SelfScoreFileParser.extract_participants("fallfallback")[index]
    replacement.set_dropper(True)

    # Partition and update stats:
    dropper_control_group = partition.get_group_by_colour(dropper_colour)
    real_dropper = dropper_control_group.get_participants()[dropper_index]
    dropper_control_group.get_participants()[dropper_index] = replacement
    partition.update_max_skill_diff()
    max_diff = partition.get_max_diff().get_diff()
    print("Updated partition participants after drop. New max-diff is: "+str(max_diff))



    # Effectuate replacement in global list and in partition (the sort again)
    # Global list
    participants.remove(real_dropper)
    participants.append(replacement)
    SelfScoreFileParser.sortByTotalScore(participants)
