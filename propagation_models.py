import numpy as np
import matplotlib.pyplot as plt
import os

c = 3e8
f = 900e6
Pt = 1.0
Gt = Gr = 1.0

lam = c / f
k = 2 * np.pi / lam
d = np.logspace(1, np.log10(5000), 4000)

os.makedirs("figures", exist_ok=True)


def to_dBm(power):
    return 10 * np.log10(power) + 30


def models(ht, hr):
    Pr_fs = Pt * Gt * Gr * (lam / (4 * np.pi * d))**2
    Pr_2ray = Pt * Gt * Gr * (ht**2 * hr**2) / d**4

    d_break = 4 * np.pi * ht * hr / lam

    d1 = np.sqrt(d**2 + (ht - hr)**2)
    d2 = np.sqrt(d**2 + (ht + hr)**2)

    E = np.exp(-1j * k * d1) / d1 - np.exp(-1j * k * d2) / d2
    Pr_full = Pt * Gt * Gr * (lam / (4 * np.pi))**2 * np.abs(E)**2

    return Pr_fs, Pr_2ray, Pr_full, d_break


print(f"Wavelength = {lam:.4f} m")

ht, hr = 20.0, 2.0
fs, tr, full, db = models(ht, hr)

print(f"\nTransmitter height = {ht} m")
print(f"Receiver height = {hr} m")
print(f"Breakpoint distance = {db:.2f} m")

# Free-space and two-ray comparison
plt.figure(figsize=(8, 5))
plt.semilogx(d, to_dBm(fs), label="Free-space")
plt.semilogx(d, to_dBm(tr), "--", label="Two-ray asymptotic")
plt.semilogx(d, to_dBm(full), label="Full two-ray")
plt.axvline(db, color="black", linestyle=":", label=f"Breakpoint = {db:.0f} m")
plt.xlabel("Distance (m)")
plt.ylabel("Received Power (dBm)")
plt.title("Free-space vs. Two-ray Propagation")
plt.ylim(-130, 40)
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig("figures/model_comparison.png", dpi=300, bbox_inches="tight")

# Decay trend comparison
mask = d > 1.5 * db
s_fs = np.polyfit(np.log10(d[mask]), 10 * np.log10(fs[mask]), 1)[0]
s_2r = np.polyfit(np.log10(d[mask]), 10 * np.log10(tr[mask]), 1)[0]

print("\n--- Decay Trend Comparison ---")
print(f"Free-space slope = {s_fs:.1f} dB/decade")
print(f"Two-ray slope = {s_2r:.1f} dB/decade")

# Antenna height variation
combos = [(10, 2), (20, 2), (50, 2), (10, 1.5)]

plt.figure(figsize=(8, 5))
plt.semilogx(d, to_dBm(fs), "k", label="Free-space")

print("\n--- Antenna Height Comparison ---")
print(" ht (m) | hr (m) | Breakpoint (m) | Power at 5 km (dBm)")

for ht_, hr_ in combos:
    fs_, tr_, full_, db_ = models(ht_, hr_)
    plt.semilogx(d, to_dBm(tr_), "--", label=f"ht={ht_}, hr={hr_}")
    print(f"{ht_:7.1f} | {hr_:6.1f} | {db_:14.1f} | {to_dBm(tr_[-1]):17.1f}")

plt.xlabel("Distance (m)")
plt.ylabel("Received Power (dBm)")
plt.title("Effect of Antenna Heights on Two-ray Power")
plt.ylim(-140, 40)
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig("figures/antenna_height.png", dpi=300, bbox_inches="tight")

# Full two-ray interference behavior
plt.figure(figsize=(8, 5))
plt.semilogx(d, to_dBm(fs), label="Free-space")
plt.semilogx(d, to_dBm(tr), "--", label="Two-ray asymptotic")
plt.semilogx(d, to_dBm(full), label="Full two-ray model")
plt.xlabel("Distance (m)")
plt.ylabel("Received Power (dBm)")
plt.title("Interference Behavior in Full Two-ray Model")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig("figures/interference_behavior.png", dpi=300, bbox_inches="tight")

print("\n--- Full Model Interpretation ---")
print("Direct and reflected signals combine at the receiver.")
print("Constructive interference increases received power.")
print("Destructive interference reduces received power.")
print("This produces fluctuations in the full two-ray model.")

plt.show()
