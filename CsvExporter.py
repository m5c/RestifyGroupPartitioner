# Exports the final distirbutor result as a single csv. Only codenames appear in the csv as key, no actual participant
# names. The remaining columns are the skills declared per participant.
import os

import Participant
from distributor import Partition
from invitationgen import MetaBundleFiller


def export_partition_csv(partition: Partition, participants: list[Participant], file_location: str):

    # remove previous legacy versions of file if it already exists
    if os.path.exists(file_location):
        os.remove(file_location)

    print("Dummy CSV export to " + file_location)
    csvfile = open(file_location, "a")

    # Append header
    csvfile.write(create_header())

    # Append CSV line for every participant (key is codename)
    for group in partition.get_groups():

        for index in range(len(group.get_participants())):
            pseudonym = MetaBundleFiller.build_pseudonym(group, index)

            # replace space by dash so it matches codename in other CSV files.
            pseudonym = pseudonym.replace(' ', '-')
            csvfile.write("\n")
            csvfile.write(create_participant_entry(pseudonym, group.get_participants()[index]))

    # Actually write to disk.
    csvfile.close()


def create_header() -> str:
    return "codename, java, spring, maven, touchcore, unix, rest, singleton, reflection"


def create_participant_entry(codename: str, participant: Participant) -> str:
    csvline = codename + ", "
    for skill in participant.get_skills():
        csvline += str(skill) + ", "
    # remove last trailing character
    csvline = csvline.strip(csvline[-1])
    csvline = csvline.strip(csvline[-1])
    return csvline
