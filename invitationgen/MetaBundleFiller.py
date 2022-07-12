# analyzes the mounted recruitment drive and creates a CSV / table representation of all self-assessment forms.
import string
from pathlib import Path
from Participant import Participant
from distributor import Partition, ControlGroup
from invitationgen.MetaBundle import MetaBundle

# location on encrypted drive where emails of all participants are stored
email_file_location = "/Volumes/RestifyVolume/email.txt"


# location on encrypted drive where upload lcoations of all participants are stored
upload_url_file_location = "/Volumes/RestifyVolume/upload-locations.txt"


# file:///Users/schieder/Code/phd-meeting-logs/logs/2022-04-01.md#onedrive
pseudonym_animal_list = ["Squid", "Raccoon", "Zebra", "Fox", "Unicorn", "Turtle", "Koala", "Lion", "Giraffe", "Emu"]


def build_pseudonym(group: ControlGroup, index_in_group : int):
    return group.get_group_name() + " " + pseudonym_animal_list[index_in_group]


# Resolves a pseudonym to the corresponding upload location
def resolve_upload_location(pseudonym : string, upload_urls):
    pseudonym = pseudonym.lower()
    pseudonym = pseudonym.replace(" ", "-")
    return upload_urls.get(pseudonym)


# Helper function that adds to every element in meta_info bundle additional personal information that is derived from
# the partition layout.
def complete_with_partition_info(meta_bundles: [], partition: Partition, upload_urls):
    # We iterate partition wise, because individual participants in the meta_info_bundle are easily found
    for group in partition.groups:
        group_name = group.get_group_name().lower()
        index_in_group = 0
        for participant in group.get_participants():
            meta_bundle = meta_bundles[participant.get_name()]
            meta_bundle.set_group_name(group_name)
            meta_bundle.set_pseudonym(build_pseudonym(group, index_in_group))
            index_in_group += 1
            meta_bundle.set_upload_location(resolve_upload_location(meta_bundle.get_pseudonym(), upload_urls))
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
