# analyzes the mounted recruitment drive and creates a CSV / table representation of all self-assessment forms.
from pathlib import Path

import numpy.linalg

from Participant import Participant
import numpy as np


# Searches recursively for all self assessment submissions.
def get_all_forms():
    form_dir = "/Volumes/RestifyVolume/recruitment/"
    print("Scanning for forms in: " + form_dir)
    print("Found:")
    all_form_locations = []
    for form in Path(form_dir).rglob('*.txt'):
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
def extract_participant_line(form):
    ## extract participant name from form file location
    name = str(form).split("/")[4]

    ## extract participant skills from form file
    skills = extract_scores(form)

    ## add total score
    return Participant(name, skills)


## builds a markdon table line for a given participant
def build_participant_line(participant):
    line = "|"
    # name
    line = line + "*" + participant.name + "* |"

    # all scores
    for skill in participant.skills:
        line = line + str(skill) + "|"

    # total score
    line = line + str(participant.compute_total_score()) + "|\n"
    return line


## Build participant objects from parsed forms
def extract_participants():
    participants = []

    ## Add an entry for every recruitment form detected
    for form in get_all_forms():
        participants.append(extract_participant_line(form))

    return participants


## compute the actual average of participant skills
def build_average_skills(participants):
    return [number / len(participants) for number in build_summed_skills(participants)]


## compute the noramlized vector of participant skills
def build_normalized_skills(participants):
    summed_skills = build_summed_skills(participants)
    return summed_skills / numpy.sqrt(np.sum(summed_skills**2))


## computes a summed vector of all participant skills
def build_summed_skills(participants):
    # sum of all participant skills
    summed_skills = [0,0,0,0,0,0,0,0]
    for participant in participants:
        summed_skills = np.add(summed_skills, participant.skills)
    return summed_skills


def build_markdown_grid():
    participants = extract_participants()

    text_file = open("/tmp/recruitment.md", 'w')

    markdown_title = "# Recruitment\n"
    text_file.write(markdown_title)

    ## Build stat recruitment grid
    markdown_stats_preamble = '## Stats\n\nBelow grid shows statistical information about participant skills.  \nRecruitment answers range from 1-5 where 5 indicates the highest experience.\n\n| \ | Java | Spring | MVN | T-CORE | UNIX | REST | Singl. | Refl. |\n|---|---|---|---|---|---|---|---|---|\n'
    text_file.write(markdown_stats_preamble)
    # Average
    text_file.write("| **Average** |")
    for average_score in build_average_skills(participants):
        text_file.write(str(round(average_score,2)) + " |")
    text_file.write("\n")
    # Normalized Vector
    text_file.write("| **Normalized** |")
    for normalized_score in build_normalized_skills(participants):
        text_file.write(str(round(normalized_score,2)) + " |")
    text_file.write("\n")

    ## Build participant recruitment scores
    markdown_participant_preamble = "## Participants\n\nBelow scores are auto extraced from the self-assessment forms.  \nRecruitment answers range from 1-5 where 5 indicates the highest experience.\n\n| **Name** | Java | Spring | MVN | T-CORE | UNIX | REST | Singl. | Refl. | *Total* |\n|---|---|---|---|---|---|---|---|---|---|\n"
    text_file.write(markdown_participant_preamble)
    for participant in participants:
        text_file.write(build_participant_line(participant))

    text_file.close()

build_markdown_grid()
