# Exports the final distirbutor result as a single csv. Only codenames appear in the csv as key, no actual participant names. The remaining columns are the skills declared per participant.
import Participant
from distributor import Partition


def export_partition_csv(partition: Partition, file_location: str):
    print("Dummy CSV export to "+file_location)


def create_header():
    return "codename, java, spring, maven, touchcore, unix, rest, singleton, reflection"


def create_participant_entry(paticipant: Participant):
    return "..."

