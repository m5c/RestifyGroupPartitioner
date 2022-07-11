# analyzes the mounted recruitment drive and creates a CSV / table representation of all self-assessment forms.
from pathlib import Path
from Participant import Participant

email_file_location = "/Volumes/RestifyVolume/email.txt"


# Parses the email text file and returns a map from the kebab-name-notation to the participant-email string
def get_all_emails():

    # Prepare target map
    emails = {}

    # Open file for interpretation
    email_file = open(email_file_location, 'r')
    lines = email_file.readlines()

    # parse every line and fill name-to-email map.
    for line in lines:
        words = line.split()
        name = words[0]
        email = words[1]
        emails.
