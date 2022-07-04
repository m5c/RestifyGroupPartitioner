import numpy as np


# compute the actual average of participant skills
def build_average_skills(participants):
    return [number / len(participants) for number in build_summed_skills(participants)]


# compute the normalized vector of participant skills
def build_normalized_skills(participants):
    summed_skills = build_summed_skills(participants)
    return summed_skills / np.sqrt(np.sum(summed_skills ** 2))


# computes a summed vector of all participant skills
def build_summed_skills(participants):
    # sum of all participant skills
    summed_skills = [0, 0, 0, 0, 0, 0, 0, 0]
    for participant in participants:
        summed_skills = np.add(summed_skills, participant.skills)
    return summed_skills
