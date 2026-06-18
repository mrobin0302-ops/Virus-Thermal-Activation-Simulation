# Personnal project

This repository contains a concise numerical study focusing on data fitting and predictive modeling for the thermal activation (heating process) of a viral sample under laboratory conditions.

## Project Overview

The project aims to evaluate how closely an exponential thermal Newton-like heating model fits a set of discrete experimental data points, and to predict the exact time required for the biological sample to reach a critical target temperature.

### Modeled System & Equations
The temperature evolution $T(t)$ over time $h$ (in hours) is modeled using an exponential convergence towards an equilibrium environment temperature $T_{\infty}$, adjusted by an empirical logistic attenuation component:

$$T(t) = T_{\infty} - (T_{\infty} - T_0)e^{-kt} - \frac{100}{1 + e^{-5(t-28)}}$$

Where:
* $T_{\infty} = 37^\circ\text{C}$: Ambient equilibrium temperature.
* $T_0 = 3^\circ\text{C}$: Initial storage temperature of the virus.
* $k = 0.48\text{ h}^{-1}$: Thermal conductivity/reaction coefficient.

The ideal time $t_{\text{target}}$ to hit a specific threshold $T_{\text{target}} = 36.9^\circ\text{C}$ is analytically derived by solving the primary exponential decay equation:

$$t_{\text{target}} = -\frac{1}{k} \ln\left(\frac{T_{\infty} - T_{\text{target}}}{T_{\infty} - T_0}\right)$$

---

## Experimental Data vs. Model

The script overlays $5$ key telemetry dataset points collected during the early hours of the experiment against a continuous 13-hour numerical simulation to visually check the model's validity and asymptotic behavior.

### Prerequisites
The script requires standard scientific Python libraries:
```bash
pip install numpy matplotlib
