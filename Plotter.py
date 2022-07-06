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


def plot_box(values, palette, partitions, filename):
    # reset figure, to have separate drawings
    plt.clf()

    # define frame size
    # figure((8, 6), 80)
    plt.rcParams["figure.figsize"] = (14, 4)

    # plot the boxes
    for index in range(len(values)):
        plotter_colour = palette[int(index/partitions)]
        plt.boxplot(values[index], positions=[index + 1], notch=False, patch_artist=True, showfliers=True,
                    boxprops=dict(facecolor=plotter_colour, color="#FFFFFF"),
                    capprops=dict(color=plotter_colour),
                    whiskerprops=dict(color=plotter_colour),
                    flierprops=dict(color=plotter_colour, markeredgecolor=plotter_colour),
                    medianprops=dict(color='#000000'), showmeans=True, meanprops={"marker":"s","markerfacecolor":"white", "markeredgecolor":plotter_colour})
    plt.xticks([1 * partitions, 2  * partitions, 3  * partitions, 4  * partitions, 5  * partitions, 6  * partitions, 7  * partitions, 8  * partitions], ['Java', 'Spring', 'MVN', 'T.CORE', 'UNIX', 'REST', 'Singl.', 'Refl.'])
    plt.savefig(filename)
