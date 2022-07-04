from ParticipantStatTools import build_mean_skills, build_normalized_skills, build_standard_deviation_skills
from GaussianPlotter import plot_gaussian

# https://colorspectrum.design/generator.html
palette = ["#8d8d8d", "#5ce7cb", "#5ca6e7", "#7a5ce7", "#d75ce7", "#e75c90", "#e7865c", "#747474"]
coloured_skill_cells = "<span style=\"color:" + palette[0] + "\">Java</span> | <span style=\"color:" + palette[
    1] + "\">Spring</span> | <span style=\"color:" + palette[2] + "\">MVN</span> | <span style=\"color:" + palette[
                           3] + "\">T.CORE</span> | <span style=\"color:" + palette[
                           4] + "\">UNIX</span> | <span style=\"color:" + palette[
                           5] + "\">REST</span> | <span style=\"color:" + palette[
                           6] + "\">Singl.</span> | <span style=\"color:" + palette[7] + "\">Refl.</span> |"


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
    markdown_stats_preamble = '## Statistics\n\nBelow grid shows statistical information about participants and their skills.  \nRecruitment answers range from 1-5 where 5 indicates the highest experience.\n\n| \ | ' + coloured_skill_cells + '\n|---|---|---|---|---|---|---|---|---|\n'
    text_file.write(markdown_stats_preamble)
    # Average
    text_file.write("| **Average** |")
    mean_scores = build_mean_skills(participants)
    for mean_score in mean_scores:
        text_file.write(str(round(mean_score, 2)) + " |")
    text_file.write("\n")

    # Standard Deviation
    text_file.write("| **Std. Dev.** |")
    stddev_scores = build_standard_deviation_skills(participants)
    for stddev_score in stddev_scores:
        text_file.write(str(round(stddev_score, 2)) + " |")
    text_file.write("\n")

    # Normalized Vector
    text_file.write("| **Normalized** |")
    for normalized_score in build_normalized_skills(participants):
        text_file.write(str(round(normalized_score, 2)) + " |")

    # Generate Plot to file
    for index in range(len(participants[0].skills)):
        plot_gaussian(mean_scores[index], stddev_scores[index], palette[index])
    text_file.write("\n\n![gaussians](/tmp/gaussians.png)")

    # Total participant count:
    text_file.write("\n\n")
    text_file.write("**Total Participants**: ```" + str(len(participants)) + "```\n\n")


# Build participant recruitment scores
def print_participant_details(text_file, participants):
    markdown_participant_preamble = "## Skill Matrix\n\nBelow scores are auto extraced from the self-assessment forms.  \nRecruitment answers range from 1-5 where 5 indicates the highest experience.\n\n| **Name** | " + coloured_skill_cells + " *Total* |\n|---|---|---|---|---|---|---|---|---|---|\n"
    text_file.write(markdown_participant_preamble)
    for participant in participants:
        text_file.write(build_participant_scores_line(participant))


# Build distribution
def print_distribution(text_file, participants):
    markdown_distribution_preamble = "## Distribution\n\nSuggested distribution into four control groups with maximized skill similarity per group.  \nSimiliarity is defined as *close **mean** and **standard deviation** values between groups, for all skills*, where lower distance for more skills is preferred over higher distance for few skills."
    text_file.write(markdown_distribution_preamble)


def build_markdown(participants):
    text_file = open("/tmp/recruitment.md", 'w')

    print_preamble(text_file)
    print_participant_details(text_file, participants)
    print_global_stats(text_file, participants)
    print_distribution(text_file, participants)

    text_file.close()
