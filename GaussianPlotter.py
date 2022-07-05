# See https://stackoverflow.com/a/10138308

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
from matplotlib.pyplot import figure


def plot_gaussian(mean, stddev, colour):
    # reset figure, to have separate drawings
    # plt.clf()

    # define frame size
    # figure((8, 6), 80)
    plt.rcParams["figure.figsize"] = (14, 4)

    # actually plot the gaussian distributions
    sigma = math.sqrt(stddev)
    x = np.linspace(mean - 3 * sigma, mean + 3 * sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mean, sigma), colour)
    plt.savefig("/tmp/gaussians.png")


def plot_box(values, palette):
    # reset figure, to have separate drawings
    plt.clf()

    # define frame size
    # figure((8, 6), 80)
    plt.rcParams["figure.figsize"] = (14, 4)

    # plot the boxes
    for index in range(len(values)):
        plt.boxplot(values[index], positions=[index + 1], notch=False, patch_artist=True, showfliers=True,
                    boxprops=dict(facecolor=palette[index], color="#FFFFFF"),
                    capprops=dict(color=palette[index]),
                    whiskerprops=dict(color=palette[index]),
                    flierprops=dict(color=palette[index], markeredgecolor=palette[index]),
                    medianprops=dict(color='#000000'))
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8], ['Java', 'Spring', 'MVN', 'T.CORE', 'UNIX', 'REST', 'Singl.', 'Refl.'])
    plt.savefig("/tmp/box.png")
