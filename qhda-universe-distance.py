/******************************************************************************
 * Project:        QHDALabs-Universe (Relational Cosmology & Emergent Time)
 * Module:         Cosmic Distance Bias Simulator with Qiskit
 * File:           qhda-universe-distance.py
 * Prototype:      Prototype 01: Cosmic Distance Bias Simulator
 *
 * Description:
 * ----------------------------------------------------------------------------
 * This module implements components of a quantum coherence control framework
 * specifically applied to the Cosmic Distance Bias Simulator.
 *
 * Primary Research Objectives:
 * ----------------------------------------------------------------------------
 * - Evaluate observed vs. idealized cosmological distances.
 * - Analyze propagation effects: medium density fluctuations, gravitational path delay.
 * - Mitigate decoherence in hybrid classical-quantum simulation pipelines.
 * - Model emergent local time modulation and observer relational offset.
 *
 * Key Responsibilities:
 * ----------------------------------------------------------------------------
 * - <responsibility_1>
 * - <responsibility_2>
 * - <responsibility_3>
 *
 * Dependencies:
 * ----------------------------------------------------------------------------
 * - Qiskit / Qiskit Aer / Python (NumPy, SciPy)
 *
 * Author:         Krzysztof W. Banasiewicz
 * Created:        2026
 * Last Modified:  11.04.2026
 *
 * License:
 * ----------------------------------------------------------------------------
 * Research-Centric Source-Available License (RCSAL) v2.0
 * See: krzyshtof.com/licences
 *
 * Notes:
 * ----------------------------------------------------------------------------
 * - This is a research sandbox for hypothesis testing; it is NOT a replacement
 * for standard cosmology.
 * - This file may be part of experimental or unstable research code.
 * - Results should be validated before production use.
 *
 ******************************************************************************/

import numpy as np
import matplotlib.pyplot as plt

# Optional quantum layer
try:
    from qiskit import QuantumCircuit
    from qiskit.quantum_info import Statevector
    QISKIT_AVAILABLE = True
except Exception:
    QISKIT_AVAILABLE = False


# ==========================================================
# Constants
# ==========================================================

C = 299792.458  # km/s
H0 = 70.0       # km/s/Mpc


# ==========================================================
# Standard Cosmology (simplified linear Hubble model)
# ==========================================================

def standard_distance_from_redshift(z):
    """
    Very simplified approximation:
    D ≈ c*z/H0   [Mpc]

    Valid only for small-to-moderate z as toy model.
    """
    return (C * z) / H0


# ==========================================================
# Quantum Correlation Engine (Emergent Time Layer)
# ==========================================================

def quantum_time_factor():
    """
    Uses a tiny quantum state to generate
    a correlation-inspired modulation factor.
    """

    if not QISKIT_AVAILABLE:
        return np.random.uniform(-0.01, 0.01)

    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)

    state = Statevector.from_instruction(qc)
    probs = state.probabilities()

    # Entanglement-inspired asymmetry
    factor = (probs[0] + probs[3]) - (probs[1] + probs[2])

    return 0.01 * factor


# ==========================================================
# Path Effects Model
# ==========================================================

def path_effects(z):
    """
    Simulates cumulative propagation bias.
    """

    # Medium density perturbation
    delta_medium = np.random.normal(0, 0.02 * z)

    # Gravitational delay / lensing randomness
    delta_gravity = np.random.normal(0, 0.015 * z)

    # Emergent local time factor
    delta_time = quantum_time_factor() * z

    # Observer relational offset
    delta_observer = np.random.normal(0, 0.005)

    total = delta_medium + delta_gravity + delta_time + delta_observer

    return total


# ==========================================================
# Real Distance Estimator
# ==========================================================

def corrected_distance(z):
    """
    D_real = D_measured * (1 + total_bias)
    """

    d_measured = standard_distance_from_redshift(z)
    bias = path_effects(z)

    d_real = d_measured * (1.0 + bias)

    return d_measured, d_real, bias


# ==========================================================
# Simulation
# ==========================================================

def run_simulation(n=100):

    redshifts = np.linspace(0.01, 2.0, n)

    measured = []
    corrected = []
    biases = []

    for z in redshifts:
        dm, dr, b = corrected_distance(z)

        measured.append(dm)
        corrected.append(dr)
        biases.append(b)

    return redshifts, np.array(measured), np.array(corrected), np.array(biases)


# ==========================================================
# Visualization
# ==========================================================

def plot_results(z, measured, corrected, biases):

    plt.figure(figsize=(12, 6))
    plt.plot(z, measured, label="Standard Distance")
    plt.plot(z, corrected, label="Relational Corrected Distance")
    plt.xlabel("Redshift z")
    plt.ylabel("Distance [Mpc]")
    plt.title("QHDALabs Universe - Distance Reinterpretation")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(12, 4))
    plt.plot(z, biases)
    plt.axhline(0, linestyle="--")
    plt.xlabel("Redshift z")
    plt.ylabel("Bias Factor")
    plt.title("Propagation / Emergent Time Bias")
    plt.grid(True)
    plt.show()


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    z, measured, corrected, biases = run_simulation(200)

    print("QHDALabs-Universe Prototype")
    print("Average bias:", np.mean(biases))
    print("Max bias:", np.max(biases))
    print("Min bias:", np.min(biases))

    plot_results(z, measured, corrected, biases)
