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
def extract_scores():
    with open("/Volumes/RestifyVolume/recruitment/arman-izadi/self-assessment.txt") as f:
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

extract_scores()