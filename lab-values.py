#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import math


# 2g, 3g, 4g, ... 6g
trials = {
    "LiCl": [1.9, 2.4, 4.1, 4.9, 5.3],
    "KCl": [-0.7, -0.9, -1.2, -1.4, -1.7],
    "(NH4)2CO3": [-1.1, -1.3, -2.4, -2.4, -2.5],
    "NH4NO3": [-1.0, -1.4, -1.6, -2.3, -2.5],
    "NH4Cl": [-1.0, -1.1, -1.4, -1.9, -2.2]
}

# main
for trial in trials:
    plt.grid()
    plt.ylabel("change in temperature (degC)")
    plt.xlabel(f"mass of {trial} (g)")
    plt.xticks(np.arange(0, 7, 1))
    plt.yticks(np.arange(-5, 6, 0.5))
    plt.plot([0, 2, 3, 4, 5, 6], [0] + trials[trial], scalex = False, scaley = True)
    plt.show()
