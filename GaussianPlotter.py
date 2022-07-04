# See https://stackoverflow.com/a/10138308

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
from matplotlib.pyplot import figure


def plot_gaussian(mean, stddev, colour):
    # define frame size
    # figure((8, 6), 80)
    plt.rcParams["figure.figsize"] = (14, 4)

    # actually plot the gaussian distributions
    sigma = math.sqrt(stddev)
    x = np.linspace(mean - 3 * sigma, mean + 3 * sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mean, sigma), colour)
    plt.savefig("/tmp/gaussians.png")
