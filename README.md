# Neutral Atom Open Quantum System Demo

This project provides a minimal example of time-dependent quantum dynamics
for an open two-qubit neutral atom system using QuTiP.

The goal of this repository is to demonstrate:
- Use of Python packages for quantum simulation
- Clean and modular software structure
- Simulation of a time-dependent open quantum system

This code is not a full implementation of my research, but rather a small
demonstration of common techniques and software practices used in
neutral atom quantum simulations.

---

## Features

- Two-qubit neutral atom Hamiltonian
- Lindblad collapse operators for open-system dynamics
- Time-dependent Rabi drive
- Modular package structure

---

## Installation


```bash
git clone https://github.com/colin-stewart5/neutral-atom-simulation-demo.git
cd neutral-atom-simulation-demO
python3 -m venv .venv
source .venv/bin/activate

## Runing Example
python3 examples/two_qubit_rabi.py

