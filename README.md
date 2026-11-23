# Two-Ray Ground Reflection Propagation Analysis

A Python simulation comparing free-space propagation with the two-ray ground reflection model. The project investigates received power, breakpoint distance, path-loss decay, antenna-height variation, and constructive/destructive interference between direct and reflected signals.

## Objectives

- Calculate the wavelength at a selected carrier frequency.
- Calculate the breakpoint distance for different antenna heights.
- Compare free-space, asymptotic two-ray, and full two-ray received power.
- Compare the power-decay trends of the propagation models.
- Study how transmitter and receiver antenna heights affect received power and breakpoint distance.
- Observe interference fluctuations caused by combining direct and reflected signal paths.

## Tools and Libraries

- Python 3
- NumPy
- Matplotlib
- Python `os` standard-library module

## Simulation Parameters

| Parameter | Value |
|---|---:|
| Carrier frequency | 900 MHz |
| Speed of light | \(3 \times 10^8\) m/s |
| Transmitted power | 1 W |
| Transmitter gain | 1 |
| Receiver gain | 1 |
| Main transmitter height | 20 m |
| Main receiver height | 2 m |
| Distance range | 10 m to 5000 m |
| Height comparison | 10 m, 20 m, 50 m |

## Theory

### 1. Wavelength

\[
\lambda = \frac{c}{f}
\]

Where \(c\) is the speed of light and \(f\) is the carrier frequency.

### 2. Free-space received power

Using the Friis transmission equation:

\[
P_r = P_t G_t G_r \left(\frac{\lambda}{4\pi d}\right)^2
\]

### 3. Two-ray asymptotic model

At sufficiently large distances, the two-ray ground-reflection model can be approximated by:

\[
P_r = P_t G_t G_r \frac{h_t^2 h_r^2}{d^4}
\]

### 4. Breakpoint distance

\[
d_{\text{break}} = \frac{4\pi h_t h_r}{\lambda}
\]

The breakpoint indicates the approximate transition between the free-space-like and two-ray asymptotic propagation regions.

### 5. Full two-ray model

The full model adds the direct and ground-reflected electric-field contributions:

\[
E = \frac{e^{-jkd_1}}{d_1} - \frac{e^{-jkd_2}}{d_2}
\]

\[
P_r = P_tG_tG_r\left(\frac{\lambda}{4\pi}\right)^2 |E|^2
\]

where \(k=2\pi/\lambda\), \(d_1\) is the direct-path length, and \(d_2\) is the reflected-path length. The phase difference between the two paths produces constructive and destructive interference.

## Repository Structure

```text
Two-Ray-Propagation-Analysis/
├── propagation_models.py
├── transmitter_height.py
├── requirements.txt
├── README.md
└── figures/
    ├── model_comparison.png
    ├── antenna_height.png
    ├── interference_behavior.png
    └── transmitter_height_comparison.png
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Two-Ray-Propagation-Analysis.git
cd Two-Ray-Propagation-Analysis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the simulations

```bash
python propagation_models.py
```

```bash
python transmitter_height.py
```

The scripts display the plots and save image files in the `figures/` directory. Run the commands from the project root directory.

## Expected Results

At 900 MHz:

- Wavelength: approximately **0.3333 m**
- For \(h_t=20\) m and \(h_r=2\) m, breakpoint distance: approximately **1508 m**
- Free-space power decay: approximately **20 dB per decade**
- Two-ray asymptotic power decay: approximately **40 dB per decade**

### Breakpoint distance for different transmitter heights

For a receiver height of 2 m:

| Transmitter height | Receiver height | Breakpoint distance |
|---:|---:|---:|
| 10 m | 2 m | 754 m |
| 20 m | 2 m | 1508 m |
| 50 m | 2 m | 3770 m |

Increasing transmitter height increases the breakpoint distance. It also increases the received power predicted by the asymptotic two-ray model at a fixed distance.

## Generated Figures

### Free-space vs. Two-ray Propagation

![Model comparison](figures/model_comparison.png)

### Effect of Antenna Heights

![Antenna height comparison](figures/antenna_height.png)

### Interference Behavior in the Full Two-ray Model

![Interference behavior](figures/interference_behavior.png)

### Transmitter Height Comparison

![Transmitter height comparison](figures/transmitter_height_comparison.png)

## Key Observations

1. Free-space received power decreases approximately as \(1/d^2\).
2. The asymptotic two-ray received power decreases approximately as \(1/d^4\).
3. The breakpoint distance increases when either antenna height increases.
4. The full two-ray model shows fluctuations because the direct and reflected signals combine with different phases.
5. Constructive interference increases received power, while destructive interference reduces it.
6. Antenna height affects both the breakpoint distance and the received power predicted by the two-ray model.

## Conclusion

The simulation demonstrates how ground reflection changes radio-wave propagation compared with free-space propagation. The asymptotic two-ray model predicts a faster power decay at large distances, while the full two-ray model reveals interference fluctuations caused by the direct and reflected paths.

The results also show that increasing antenna height increases the breakpoint distance and changes the received power. These concepts are important in understanding practical terrestrial wireless communication channels.

---

**Topic:** Free-space and Two-ray Ground Reflection Propagation  
**Programming Language:** Python  
 
 course title: Mobile and Wireless Communication
 
name:samin afzal fuad

id-T241002

dept:electronics and telecommunication engineering

international islamic university chittagong 

semester:6th
