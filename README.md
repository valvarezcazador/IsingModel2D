# The 2D Ising Model: Monte Carlo Simulations

This repository contains a Python implementation of the **two-dimensional Ising model**, a fundamental model in statistical mechanics used to study collective phenomena, magnetic systems, and phase transitions.

The project explores the numerical simulation of interacting spins on a square lattice using the **Metropolis Monte Carlo algorithm**. It focuses on the evolution of the system towards thermal equilibrium and the behaviour of macroscopic observables, particularly magnetization and energy.

The implementation was developed in the context of Statistical Physics teaching activities, with the aim of providing a computational approach to understanding the microscopic dynamics underlying macroscopic phase transitions.

---

## 1. Theoretical Background

The Ising model describes a system of interacting spins arranged on a lattice. In the two-dimensional version considered here, each lattice site contains a spin variable

\[
s_{i,j}\in\{-1,+1\}.
\]

The system is described by the Hamiltonian

\[
\mathcal{H}
=
-J\sum_{\langle i,j\rangle}s_i s_j
-h\sum_i s_i,
\]

where:

- \(J\) is the nearest-neighbour coupling constant.
- \(h\) is an external magnetic field.
- \(s_i\) denotes the spin at lattice site \(i\).
- The first sum runs over nearest-neighbour pairs.

For a ferromagnetic system, \(J>0\), neighbouring spins tend to align with each other.

The competition between thermal fluctuations and spin interactions leads to a phase transition between an ordered ferromagnetic phase and a disordered paramagnetic phase.

### Relevant Observables

Two important quantities characterise the macroscopic behaviour of the system.

**Magnetization**

The magnetization per spin is defined as

\[
m=\frac{1}{N}\sum_i s_i,
\]

where \(N=L^2\) is the total number of lattice sites.

It measures the degree of magnetic ordering of the system.

**Energy**

The energy per spin is given by

\[
e=\frac{\mathcal{H}}{N}.
\]

It provides information about the energetic configuration of the lattice.

---

## 2. Numerical Method: The Metropolis Algorithm

The evolution of the spin configuration is simulated using the Metropolis Monte Carlo algorithm.

The algorithm generates configurations according to the Boltzmann distribution,

\[
P(\mathcal{C})\propto
\exp\left(-\frac{\mathcal{H}(\mathcal{C})}{k_B T}\right),
\]

where \(T\) is the temperature and \(k_B\) is Boltzmann's constant.

At each Monte Carlo step:

1. A spin is selected randomly from the lattice.
2. Its orientation is proposed to be reversed.
3. The corresponding energy variation is calculated:

\[
\Delta E=E_{\mathrm{new}}-E_{\mathrm{old}}.
\]

4. The proposed transition is accepted according to the Metropolis criterion:

\[
P_{\mathrm{accept}}
=
\min\left(1,e^{-\Delta E/(k_B T)}\right).
\]

Consequently, energy-decreasing transitions are always accepted, whereas energy-increasing transitions are accepted with a temperature-dependent probability.

This procedure allows the system to explore its configuration space while reproducing the equilibrium Boltzmann distribution under the appropriate sampling conditions.

### Boundary Conditions

Periodic boundary conditions are used to minimise finite-size boundary effects. The lattice is therefore treated as a periodic system, effectively wrapping around its edges.

---

## 3. Repository Structure

```text
IsingModel2D/
│
├── README.md
│
├── ising.py
│
├── FirstThings.py
├── CodeImprovement.py
├── testing_the_code.py
├── Animation_m_vs_step.py
│
├── ISING.pdf
│
├── pyproject.toml
└── uv.lock
```

### Main Files

| File | Description |
|:---|:---|
| `ising.py` | Main implementation of the Ising model and its numerical dynamics. |
| `FirstThings.py` | Initial implementation and exploration of the model. |
| `CodeImprovement.py` | Improved implementation and exploration of the simulation. |
| `testing_the_code.py` | Tests and numerical checks of the implementation. |
| `Animation_m_vs_step.py` | Visualisation of magnetization as a function of Monte Carlo steps. |
| `ISING.pdf` | Reference document provided by the course instructor. |

---

## 4. Numerical Experiments and Visualisation

The project includes numerical experiments designed to investigate the behaviour of the Ising model.

### Magnetization Dynamics

The evolution of magnetization is studied as a function of Monte Carlo steps.

This provides insight into how the system approaches thermal equilibrium from an initial spin configuration.

The animation script `Animation_m_vs_step.py` provides a visual representation of this evolution.

### Thermal Behaviour and Phase Transitions

The two-dimensional Ising model exhibits a second-order phase transition at the critical temperature

\[
k_B T_c =
\frac{2J}{\ln(1+\sqrt{2})}.
\]

For \(J=k_B=1\),

\[
T_c\approx 2.269.
\]

Below the critical temperature, the system exhibits spontaneous magnetic ordering in the thermodynamic limit. Above it, thermal fluctuations destroy long-range magnetic order.

The numerical simulation provides a framework for exploring these phenomena and understanding the relationship between microscopic spin interactions and macroscopic behaviour.

---

## 5. Installation and Usage

The project uses Python and scientific computing libraries, with `uv` for dependency management.

### Requirements

- Python 3.13
- [uv](https://docs.astral.sh/uv/)

### Installation

Clone the repository:

```bash
git clone https://github.com/valvarezcazador/IsingModel2D.git

cd IsingModel2D
```

Install the project dependencies:

```bash
uv sync
```

### Running the Simulation

To run the main implementation:

```bash
uv run python ising.py
```

To explore the magnetization dynamics:

```bash
uv run python Animation_m_vs_step.py
```

Additional scripts are available in the repository for testing and exploring the implementation.

---

## 6. References

- Onsager, L. (1944). *Crystal Statistics. I. A Two-Dimensional Model with an Order-Disorder Transition*. Physical Review, 65, 117–149.
- Metropolis, N., Rosenbluth, A. W., Rosenbluth, M. N., Teller, A. H., & Teller, E. (1953). *Equation of State Calculations by Fast Computing Machines*. The Journal of Chemical Physics, 21, 1087–1092.
- Course material: `ISING.pdf`, provided by the Statistical Physics course instructor.

---

## 7. Project Scope

This project is an educational and computational exploration of the two-dimensional Ising model.

It aims to connect the theoretical foundations of statistical mechanics with numerical methods, illustrating how Monte Carlo simulations can be used to investigate emergent macroscopic phenomena from simple microscopic interactions.

The implementation and experiments provide a starting point for further investigations into finite-size effects, critical phenomena, thermal fluctuations, and statistical properties of interacting systems.

---

*Developed as part of computational work associated with Statistical Physics teaching activities.*