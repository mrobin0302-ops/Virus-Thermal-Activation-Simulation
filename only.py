import numpy as np
import matplotlib.pyplot as plt

# --- Paramètres du modèle ---
T_inf = 37          # température d'équilibre (°C)
T0 = 3              # température initiale (°C)
k = 0.48            # constante (h⁻¹)
T_target = 36.9     # température à atteindre (°C)

# --- Données expérimentales ---
t_exp = np.array([0, 1, 2, 3, 4])
T_exp = np.array([3, 16, 24, 28.5, 30])

# --- Modèle exponentiel ---
def T(t):
    return T_inf - (T_inf - T0) * np.exp(-k * t) - 100/(1+np.exp(-5*(t-28)))

# --- Calcul du temps pour atteindre 36.9 °C ---
t_target = -np.log((T_inf - T_target) / (T_inf - T0)) / k
print(f"Temps pour atteindre {T_target} °C : {t_target:.2f} heures")

# --- Simulation sur un intervalle de 0 à 13 h ---
t_vals = np.linspace(0, 13, 300)
T_vals = T(t_vals)

# --- Tracé ---
plt.figure(figsize=(8,5))

# Courbe du modèle (pointillé)
plt.plot(t_vals, T_vals, '--', color='darkblue', linewidth=2, label="Modèle : 37 - 34·exp(-0.48t)")

# Points expérimentaux
plt.scatter(t_exp, T_exp, color='orange', s=60, zorder=5, label="Mesures expérimentales")

# Ligne et point cible
plt.axhline(y=T_target, color='red', linestyle='--', label=f"{T_target} °C")
plt.axvline(x=t_target, color='green', linestyle='--', label=f"t = {t_target:.2f} h")
plt.scatter([t_target], [T_target], color='purple', zorder=6)

# Point de départ
plt.scatter([0], [T0], color='black', zorder=6)
plt.text(0.3, T0 + 0.4, "Départ", fontsize=9, color='black')

# Mise en forme
plt.title("Échauffement du virus (modèle exponentiel vs données expérimentales)")
plt.xlabel("Temps (heures)")
plt.ylabel("Température (°C)")
plt.xlim(-0.2, 13)
plt.ylim(0, 38)
plt.legend()
plt.grid(True)
plt.show()
