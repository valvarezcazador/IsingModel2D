from ising import * 

lattice = initial_random_state(5)

def simulate_ising_from_lattice(lattice, T_red, n_steps = 1e6, n_measure = 1e4):
    """
    Simula el modelo de Ising 2D a partir de una configuración inicial dada.

    Parámetros:
        lattice : np.array (N x N)
            Lattice inicial de spins (valores +1 o -1).
        T_red : float
            Temperatura reducida del sistema.
        n_total : int
            Número total de intentos de flip de spin.
        n_store : int
            Cada cuántos intentos se guardan E y M.
    
    Retorna:
        steps : list
            Lista con los pasos en que se almacenaron los datos.
        energies : list
            Energía del sistema en cada paso guardado.
        magnetizations : list
            Magnetización del sistema en cada paso guardado.
    """ 
    energies = []
    magnetizations = []
    
    for attempt in range(1, int(n_steps) + 1):
        lattice = metropolis_algorithm(lattice, T_red, 1)  
        
        if attempt % int(n_measure) == 0:
            energies.append(energy(lattice))
            magnetizations.append(magnetization(lattice))

    energies = np.array(energies)
    energies2 = np.array(energies ** 2)
    magnetizations = np.array(magnetizations)
    magnetizations_abs = np.array(np.abs(magnetizations))
    
    return np.mean(energies),  np.mean(energies2), np.mean(magnetizations), np.mean(magnetizations_abs) 

# energies, energies2, magnetizations, magnetizations_abs = simulate_ising_from_lattice(lattice, T_red, n_steps = 1e6, n_measure = 1e4)

T_red = np.linspace(1.5, 3, 10) # T_C = 2.269 
energies = []
energies2 = []
magnetizations = []
magnetizations_abs = [] 

for T in T_red:
    energy_T, energy2_T, magnetization_T, magnetization_abs_T = simulate_ising_from_lattice(lattice, T, n_steps = 1e6, n_measure = 1e4)
    energies.append(energy_T)
    energies2.append(energy2_T)
    magnetizations.append(magnetization_T)
    magnetizations_abs.append(magnetization_abs_T)

fig2, axes2 = plt.subplots(2, 2, figsize = (20, 4))  # es un array 2 x 2

energies = np.array(energies)
energies2 = np.array(energies2)
magnetizations = np.array(magnetizations)
magnetizations_abs = np.array(magnetizations_abs)

# Eje superior izquierdo: Energies
axes2[0, 0].plot(T_red, energies, marker='o', color='blue')
axes2[0, 0].set_xlabel("Temperatura reducida T*")
axes2[0, 0].set_ylabel("Energía <E>")
axes2[0, 0].set_title("Energía vs Temperatura")
axes2[0, 0].grid(True)

# Eje superior derecho: C
axes2[0, 1].plot(T_red, (energies2 - energies * energies)/(T_red ** 2), marker='o', color='red')
axes2[0, 1].set_xlabel("Temperatura reducida T*")
axes2[0, 1].set_ylabel("<E^2>")
axes2[0, 1].set_title("Energía al cuadrado vs Temperatura")
axes2[0, 1].grid(True)

# Eje inferior izquierdo: Magnetizations
axes2[1, 0].plot(T_red, magnetizations, marker='o', color='green')
axes2[1, 0].set_xlabel("Temperatura reducida T*")
axes2[1, 0].set_ylabel("Magnetización <M>")
axes2[1, 0].set_title("Magnetización vs Temperatura")
axes2[1, 0].grid(True)

# Eje inferior derecho: Magnetizations absolute
axes2[1, 1].plot(T_red, magnetizations_abs, marker='o', color='purple')
axes2[1, 1].set_xlabel("Temperatura reducida T*")
axes2[1, 1].set_ylabel("Magnetización absoluta <|M|>")
axes2[1, 1].set_title("Magnetización absoluta vs Temperatura")
axes2[1, 1].grid(True)

plt.tight_layout()
plt.show()