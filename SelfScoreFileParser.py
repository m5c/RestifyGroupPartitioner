# analyzes the mounted recruitment drive and creates a CSV / table representation of all self-assessment forms.
from pathlib import Path
from Participant import Participant

form_dir = "/Volumes/RestifyVolume/recruitment/"
form_backup_dir = "/Volumes/RestifyVolume/fallback/"
form_backup_backup_dir = "/Volumes/RestifyVolume/fallfallback/"


# Searches recursively for all self assessment submissions.
def get_all_forms(source):
    print("Scanning for forms in: " + source)
    print("Found:")
    all_form_locations = []
    for form in Path(source).rglob('*.txt'):
        print(form.absolute())
        all_form_locations.append(form.absolute())
    return all_form_locations


## Helper function to determine the human readable skill scores for a participant.
## Argument is string pointing to the the form as absolute path
## Returns an integer array
def extract_scores(form):
    with open(form) as f:
        lines = f.readlines()
        # print(lines)

        ## only keep the lines that are actual answers
        answer_lines = []
        for line in lines:
            if line.__contains__('['):
                answer_lines.append(line)
        ## first occurence of "[" is part of instructions, must be removed
        answer_lines.pop(0)
        # print(answer_lines)

        ## find the list positions of the answer lines (the lines containting '[x]')
        answers = []
        for index, answer_line in enumerate(answer_lines):
            if answer_line.__contains__('[x]'):
                answers.append(index)

        ## actual scores are always mod 5 of every entry (since there are 5 options per question)
        # print(answers)
        answers = [score % 5 + 1 for score in answers]
        print(answers)
        return answers


## argument is the form location, not the form content
def __extract_participant_line(form):
    ## extract participant name from form file location
    name = str(form).split("/")[4]

    ## extract participant skills from form file
    skills = extract_scores(form)

    ## add total score
    return Participant(name, skills)


def sortByTotalScore(participants: list[Participant]):
    # Before return, order the participants by their individual score sum
    participants.sort(reverse=True, key=participant_total_score)


def participant_total_score(participant):
    return (participant.compute_total_score())


## Build participant objects from parsed forms
## Source string must be either of "original", "fallback", "fallfallback"
def extract_participants(source: str):

    if(source == "original"):
        form_dir_string = form_dir
    elif(source == "fallback"):
        form_dir_string = form_backup_dir
    elif(source == "fallfallback"):
        form_dir_string = form_backup_backup_dir
    else:
        raise("Unknown input option: " + source)

    participants = []

    ## Add an entry for every recruitment form detected
    for form in get_all_forms(form_dir_string):
        participants.append(__extract_participant_line(form))

    sortByTotalScore(participants)

    return participants


# Verifies if the input directory exists (is an ecrypted volume that may not be mounted)
# Prints error message and stops program if not found
def verify_input_files():
    if not Path(form_dir).exists():
        print("Cannot access input files at: " + form_dir)
        print("Volume not mounted?")
        exit(-1)
