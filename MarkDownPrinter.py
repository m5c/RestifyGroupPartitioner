from ParticipantStatTools import build_average_skills, build_normalized_skills

def print_preamble(text_file):
    markdown_title = "# Recruitment\n"
    markdown_preamble = "This generated file lists:\n * a [participant skill matrix](#skill-matrix)\n * extracted [statistical data](#statistics)\n * a [suggested control group distribution](#distribution)\n\n"
    text_file.write(markdown_title)
    text_file.write(markdown_preamble)


# builds a markdown table line for a given participant
def build_participant_scores_line(participant):
    line = "|"
    # name
    line = line + "*" + participant.name + "* |"

    # all scores
    for skill in participant.skills:
        line = line + str(skill) + "|"

    # total score
    line = line + str(participant.compute_total_score()) + "|\n"
    return line

# Build stat recruitment grid
def print_global_stats(text_file, participants):
    markdown_stats_preamble = '## Statistics\n\nBelow grid shows statistical information about participants and their skills.  \nRecruitment answers range from 1-5 where 5 indicates the highest experience.\n\n| \ | Java | Spring | Maven | T.CORE | UNIX | REST | Singl. | Refl. |\n|---|---|---|---|---|---|---|---|---|\n'
    text_file.write(markdown_stats_preamble)
    # Average
    text_file.write("| **Average** |")
    for average_score in build_average_skills(participants):
        text_file.write(str(round(average_score, 2)) + " |")
    text_file.write("\n")
    # Normalized Vector
    text_file.write("| **Normalized** |")
    for normalized_score in build_normalized_skills(participants):
        text_file.write(str(round(normalized_score, 2)) + " |")
    text_file.write("\n\n")
    text_file.write("**Total Participants**: ```"+str(len(participants))+"```\n\n")


# Build participant recruitment scores
def print_participant_details(text_file, participants):
    markdown_participant_preamble = "## Skill Matrix\n\nBelow scores are auto extraced from the self-assessment forms.  \nRecruitment answers range from 1-5 where 5 indicates the highest experience.\n\n| **Name** | Java | Spring | MVN | T-CORE | UNIX | REST | Singl. | Refl. | *Total* |\n|---|---|---|---|---|---|---|---|---|---|\n"
    text_file.write(markdown_participant_preamble)
    for participant in participants:
        text_file.write(build_participant_scores_line(participant))


# Build distribution
def print_distribution(text_file, participants):
    markdown_distribution_preamble = "## Distribution\n\nSuggested distribution into four control groups with maximized skill similarity per group:\n"
    text_file.write(markdown_distribution_preamble)


def build_markdown(participants):

    text_file = open("/tmp/recruitment.md", 'w')

    print_preamble(text_file)
    print_participant_details(text_file, participants)
    print_global_stats(text_file, participants)
    print_distribution(text_file, participants)


    text_file.close()

