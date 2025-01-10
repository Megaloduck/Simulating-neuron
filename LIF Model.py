import numpy as np
import matplotlib.pyplot as plt

# Parameters
tau_m = 20  # Membrane time constant (ms)
R = 10      # Membrane resistance (MΩ)
V_th = -50  # Firing threshold (mV)
V_reset = -70  # Reset potential (mV)
I = 1.5     # Input current (μA)
dt = 0.1    # Time step (ms)
T = 200     # Total time (ms)

# Initialization
time = np.arange(0, T, dt)
V = np.zeros_like(time)
V[0] = -65  # Resting potential (mV)

# Simulation
for t in range(1, len(time)):
    dV = (-V[t-1] + R * I) / tau_m
    V[t] = V[t-1] + dV * dt
    if V[t] >= V_th:  # Check for spike
        V[t] = V_reset

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(time, V, label="Membrane Potential (V)")
plt.axhline(V_th, color='r', linestyle='--', label="Threshold")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential (mV)")
plt.title("Leaky Integrate-and-Fire Neuron Simulation")
plt.legend()
plt.show()
