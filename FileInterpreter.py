# analyzes the mounted recruitment drive and creates a CSV / table representation of all self-assessment forms.
from pathlib import Path


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
def build_participant_line(form):

    line = "|"

    ## extract participant name from form file location
    participant_name = str(form).split("/")[4]
    line = line + "*"+participant_name + "* |"

    ## extract participant skills from form file
    participant_skills = extract_scores(form)
    for skill in participant_skills:
        line = line + str(skill) + "|"

    ## add total score
    line = line + str(sum(participant_skills))+"|\n"
    return line


def build_markdown_grid():
    markdown = "# Recruitment\nBelow scores are auto extraced from the self-assessment forms. Recruitment answers range from 1-5 where 5 indicates the highest experience.\n\n| **Name** | Java | Spring | MVN | T-CORE | UNIX | REST | Singl. | Refl. | *Total* |\n|---|---|---|---|---|---|---|---|---|---|\n"
    text_file = open("/tmp/recruitment.md", 'w')
    text_file.write(markdown)

    ## Add an entry for every recruitment form detected
    for form in get_all_forms():
        text_file.write(build_participant_line(form))

    text_file.close()

build_markdown_grid()