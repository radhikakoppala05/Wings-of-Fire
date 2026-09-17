

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Road-width measurements along a 20 km road
km = np.array([0, 5, 8, 10, 15, 17, 20])
width = np.array([5.2, 4.9, 4.2, 5.8, 5.1, 4.3, 5.0])

df = pd.DataFrame({
    "Distance (km)": km,
    "Road Width (m)": width
})

plt.figure(figsize=(10, 5.5))

# Step graph
plt.step(
    df["Distance (km)"],
    df["Road Width (m)"],
    where="post",
    linewidth=2.8,
    label="Road Width"
)

# Measurement points
plt.scatter(
    df["Distance (km)"],
    df["Road Width (m)"],
    s=75,
    edgecolor="white",
    linewidth=1.5,
    zorder=3
)

# Value labels
for x, y in zip(km, width):
    plt.annotate(
        f"{y:.1f} m",
        (x, y),
        xytext=(0, 10),
        textcoords="offset points",
        ha="center",
        fontsize=9
    )

plt.title(
    "Road Width Analysis Along 20 km Road",
    fontsize=16,
    fontweight="bold",
    pad=15
)

plt.xlabel("Distance Along Road (km)", fontsize=11)
plt.ylabel("Road Width (m)", fontsize=11)

plt.xlim(0, 20)
plt.ylim(3, 7)

plt.xticks(np.arange(0, 21, 2))
plt.yticks(np.arange(3, 7.1, 0.5))

plt.grid(True, linestyle="--", linewidth=0.7, alpha=0.3)

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.legend(frameon=False, loc="upper right")

plt.tight_layout()
plt.show()