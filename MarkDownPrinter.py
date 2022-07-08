import numpy

from ParticipantStatTools import build_mean_skills, build_normalized_skills, build_standard_deviation_skills, \
    extract_skill_values_by_index
from Plotter import plot_gaussian, plot_box
from distributor.Partition import Partition

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

    # Min
    text_file.write("| **Min.** |")
    for index in range(len(participants[0].skills)):
        text_file.write(str(int(numpy.min(extract_skill_values_by_index(index, participants)))) + " |")
    text_file.write("\n")

    # Max
    text_file.write("| **Max.** |")
    for index in range(len(participants[0].skills)):
        text_file.write(str(int(numpy.max(extract_skill_values_by_index(index, participants)))) + " |")
    text_file.write("\n")

    # Median
    text_file.write("| **Median** |")
    for index in range(len(participants[0].skills)):
        text_file.write(str(int(numpy.median(extract_skill_values_by_index(index, participants)))) + " |")
    text_file.write("\n")

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

    # Generate Gaussian Plot to file
    for index in range(len(participants[0].skills)):
        plot_gaussian(mean_scores[index], stddev_scores[index], palette[index])
    text_file.write("\n\n![gaussians](/tmp/gaussians.png)")

    # Generate Box Plot to file
    skills = []
    for index in range(len(participants[0].skills)):
        skills.append(extract_skill_values_by_index(index, participants))
    plot_box(skills, palette, 1, "/tmp/box.png")
    text_file.write("\n\n![box](box.png)")

    # Total participant count:
    text_file.write("\n\n")
    text_file.write("**Total Participants**: ```" + str(len(participants)) + "```\n\n")


# Build participant recruitment scores
def print_participant_details(preamble, text_file, participants):
    if preamble:
        markdown_participant_preamble = "## Skill Matrix\n\nBelow scores are auto extracted from the self-assessment forms.  \nRecruitment answers range from 1-5 where 5 indicates the highest experience.\n\n"
        text_file.write(markdown_participant_preamble)

    text_file.write("| **Name** | " + coloured_skill_cells + " *Total* |\n|---|---|---|---|---|---|---|---|---|---|\n")
    for participant in participants:
        text_file.write(build_participant_scores_line(participant))


# Similar to call to box plotter in print_global_stats, but creates 4 boxplots next to another, representing the individual groups.
def build_fused_stats(partition: Partition):
    # lists all individual skills, but with interleaving groups
    interleaved_skills = []
    for skill_index in range(partition.get_skill_amount()):
        groups = partition.groups
        for group_index in range(len(groups)):
            interleaved_skills.append(
                extract_skill_values_by_index(skill_index, groups[group_index].get_participants()))
    plot_box(interleaved_skills, palette, len(groups), "/tmp/fused-stats.png")


# Helper function to print information about a given partition and the individual control groups.
def print_distribution(text_file, partition):
    build_fused_stats(partition)

    # build and print fused plot
    markdown_distribution_preamble = "## Distribution\n\nFused Stats: (skill stats for all groups and all skills)\n\n![fusedstats](fused-stats.png)\n\n"
    text_file.write(markdown_distribution_preamble)

    # print meta information about partition (grid with all skills on x axis, min group average, max group average, diff. Mark column with greates diff (Max) in bold.
    markdown_distribution_meta_preamble = "\n\nSkill inter-group variability: (represented as squares in above chart)\n\n| \ | " + coloured_skill_cells + "\n|---|---|---|---|---|---|---|---|---|\n"
    text_file.write(markdown_distribution_meta_preamble)
    # print AVG max
    text_file.write("| AVG max |")
    for skill_index in range(partition.get_skill_amount()):
        text_file.write(str(round(partition.get_average_diffs()[skill_index].get_max(), 1)) + "|")
    text_file.write("\n")
    # print AVG min
    text_file.write("| AVG min |")
    for skill_index in range(partition.get_skill_amount()):
        text_file.write(str(round(partition.get_average_diffs()[skill_index].get_min(), 1)) + "|")
    text_file.write("\n")
    # print AVG  diff
    text_file.write("| AVG diff |")
    for skill_index in range(partition.get_skill_amount()):
        if skill_index == partition.get_max_diff().get_skill_index():
            text_file.write("**" + str(round(partition.get_average_diffs()[skill_index].get_diff(), 1)) + "** |")
        else:
            text_file.write(str(round(partition.get_average_diffs()[skill_index].get_diff(), 1)) + "|")
    text_file.write("\n")

    # TODO: highlight greatest diff.
    # print max diff, textually.

    for control_group in partition.groups:
        text_file.write("### " + control_group.get_group_name() + "\n\nTotal Score: " + str(
            control_group.get_group_score()) + "\n\n#### Participants\n\n")
        print_participant_details(False, text_file, control_group.get_participants())
        # text_file.write("\n\n#### Stats\n\n")


def build_markdown(participants: []):
    build_markdown_with_partition(participants, [])


def build_markdown_with_partition(participants: [], partition: Partition):
    text_file = open("/tmp/recruitment.md", 'w')

    print_preamble(text_file)
    print_participant_details(True, text_file, participants)
    print_global_stats(text_file, participants)

    # Only append partition stats if there is somethign to print (not empty)
    if partition:
        print_distribution(text_file, partition)

    text_file.close()
