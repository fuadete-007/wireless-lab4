import numpy as np
import matplotlib.pyplot as plt
import os

c = 3e8
f = 900e6
Pt = 1.0
Gt = Gr = 1.0
hr = 2.0

lam = c / f
d = np.logspace(1, np.log10(5000), 4000)
heights = [10, 20, 50]

os.makedirs("figures", exist_ok=True)

print(f"Wavelength = {lam:.4f} m")
print("\nTransmitter Height Comparison")
print(" ht (m) | hr (m) | Breakpoint (m)")
print("-" * 35)

plt.figure(figsize=(8, 5))

for ht in heights:
    d_break = 4 * np.pi * ht * hr / lam
    Pr = Pt * Gt * Gr * (ht**2 * hr**2) / d**4
    Pr_dBm = 10 * np.log10(Pr) + 30

    plt.semilogx(d, Pr_dBm, label=f"ht = {ht} m")
    print(f"{ht:7.1f} | {hr:6.1f} | {d_break:14.2f}")
    plt.axvline(d_break, linestyle="--", alpha=0.5)

plt.xlabel("Distance (m)")
plt.ylabel("Received Power (dBm)")
plt.title("Effect of Transmitter Height on Two-ray Propagation")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig(
    "figures/transmitter_height_comparison.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
