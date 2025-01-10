# Simulating-neuron
Simple Neuron visualization using the Leaky Integrate-and-Fire Model. Objectives to Simulate the behavior of a single neuron using the leaky integrate-and-fire (LIF) model. This project introduces basic neuroscience concepts and computational modeling.

## What You'll required
- Python basics: variables, loops, and functions.
- Plotting with **Matplotlib**.
- Using numerical libraries like **NumPy**.
- Simple differential equations in neuroscience.

Description
The LIF model describes how the membrane potential 

V of a neuron evolves over time, integrating inputs and "firing" (spiking) when the potential reaches a threshold. The membrane potential decays over time due to a "leak."

## Description
The LIF model describes how the membrane potential (𝑉) of a neuron evolves over time, integrating inputs and "firing" (spiking) when the potential reaches a threshold. The membrane potential decays over time due to a "leak."

The governing equation is:

\[
\tau_m \frac{dV}{dt} = -V + R \cdot I
\]

Where:
- \( V \): Membrane potential (mV)
- \( \tau_m \): Membrane time constant (ms)
- \( R \): Membrane resistance (\( \Omega \))
- \( I \): Input current (\( \mu A \))
- Threshold (\( V_{th} \)): When \( V \geq V_{th} \), the neuron "spikes."

## Steps

### 1. Set Up the Environment
Install Python and required libraries:
```bash
pip install numpy matplotlib
```
### 2. Execute the Simulation
Write the Python script to simulate  over time, given constant or varying input current. Use Euler's method for numerical integration.
### 3. Visualize Results
Plot the membrane potential over time to see spiking behavior.
### 4. Experiment with Parameters
Explore how changing , , or  affects the neuron’s firing.
