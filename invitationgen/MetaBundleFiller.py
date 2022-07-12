# analyzes the mounted recruitment drive and creates a CSV / table representation of all self-assessment forms.
from pathlib import Path
from Participant import Participant
from distributor import Partition
from invitationgen.MetaBundle import MetaBundle

email_file_location = "/Volumes/RestifyVolume/email.txt"


# Helper function that adds to every element in meta_info bundle additional personal information that is derived from
# the partition layout.
def complete_with_partition_info(meta_bundles: [], partition: Partition):
    # We iterate partition wise, because individual participants in the meta_info_bundle are easily found
    for group in partition.groups:
        group_name = group.get_group_name().lower()
        for participant in group.get_participants():
            meta_bundle = meta_bundles[participant.get_name()]
            meta_bundle.set_group_name(group_name)
            meta_bundle.set_pseudonym("toto")
            meta_bundle.set_upload_location("toto")
    # return the full dictionary
    return meta_bundles


# Parses the email text file and returns a map from the kebab-name-notation to object with all meta info
def parse_all_emails():
    # Prepare target map
    meta_info = {}

    # Open file for interpretation
    email_file = open(email_file_location, 'r')
    lines = email_file.readlines()

    # parse every line and fill name-to-email map.
    for line in lines:
        words = line.split()
        name = words[0]
        email = words[1]
        meta_info[name] = MetaBundle(name, email)

    # return the map
    return meta_info
