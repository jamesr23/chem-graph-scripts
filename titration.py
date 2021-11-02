#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import math

SYM_ACID = ""
SYM_BASE = "NaOH"

MOLARITY_ACID = 0.2
MOLARITY_BASE = 0.5

KA = 1.8e-5
KB = 1e-14 / KA

VOLUME_ACID = 0.02

N_ACID = MOLARITY_ACID * VOLUME_ACID

base_volumes = [i/1000 for i in range(21)]

pH_values = []
pH_measured_values = [2.51, 3.6, 3.93, 4.23, 4.48, 4.78, 5.1, 5.78, 12.04, 12.34, 12.6, 12.71, 12.76, 12.81, 12.85, 12.88, 12.91, 12.93, 12.95, 12.97, 13]

# main
for base_volume in base_volumes:

    volume = VOLUME_ACID + base_volume
    n_acid = MOLARITY_ACID * VOLUME_ACID
    n_base = MOLARITY_BASE * base_volume
    n_rem = abs(n_acid - n_base)
    m_ion = min(n_acid, n_base) / volume
    m_rem = n_rem / volume

    pH = -1
    if n_acid > n_base:
        if m_ion == 0:
            m_h30 = math.sqrt(KA * m_rem)
        else:
            m_h30 = KA * m_rem / m_ion
        pH = -math.log10(m_h30)
    elif n_acid < n_base:
        m_oh = KB * m_ion / m_rem
        pOH = -math.log10(m_rem + m_oh)
        pH = 14 - pOH
    else:
        m_oh = math.sqrt(KB * m_ion)
        pOH = -math.log10(m_oh)
        pH = 14 - pOH

    pH_values.append(pH)

plt.suptitle("weak acid strong base titration lab")
plt.ylabel("pH of solution")
plt.xlabel("mL of NaOH")
plt.grid()

plt.plot(pH_values, 'r', label='calculated pH values', scalex=False, scaley=False)
plt.plot(pH_measured_values, 'b', label='measured pH values', scalex=False, scaley=False)

plt.xticks(range(21))
plt.yticks(range(15))

plt.legend(loc=2)

plt.show()
