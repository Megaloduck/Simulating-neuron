# Simulating-neuron
Simple Neuron Using the Leaky Integrate-and-Fire Model. Objectives to Simulate the behavior of a single neuron using the leaky integrate-and-fire (LIF) model. This project introduces basic neuroscience concepts and computational modeling.

What You'll Learn
Python basics: variables, loops, and functions.
Plotting with Matplotlib.
Using numerical libraries like NumPy.
Simple differential equations in neuroscience.
Description
The LIF model describes how the membrane potential 
𝑉
V of a neuron evolves over time, integrating inputs and "firing" (spiking) when the potential reaches a threshold. The membrane potential decays over time due to a "leak."

The governing equation is:

𝜏
𝑚
𝑑
𝑉
𝑑
𝑡
=
−
𝑉
+
𝑅
⋅
𝐼
