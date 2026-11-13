from ising import * 

# 1.Setting up the equilibrium time / n_iter so that the lattice has lost all the initial information 

# lattice = np.zeros(shape = (20, 20)) - 1 # generating our lattice with n = 20, all spins lined up
# T_red = 1e1 # T = 0 

# n_iter = 10 ** np.arange(0, 6, 1) # trying out 

# magnets = []

# fig1, axes1 = plt.subplots(1, len(n_iter), figsize = (20, 4))  

# for i in range(len(n_iter)):
#     lattice_n = metropolis_algorithm(lattice, T_red, int(n_iter[i]))
#     m_n = np.sum(lattice_n)/lattice_n.size 
#     magnets.append(m_n)
#     axes1[i].imshow(lattice_n, cmap = 'bwr', interpolation = 'nearest', extent = [0, 20, 0, 20])
#     axes1[i].set_title(f'n_iter = {n_iter[i]:.0f}')

# plt.show() # Not sure how to compute the relaxation time 


def estimate_relaxation_time(lattice_initial, T_red, n_steps = 100000, measure_every = 1000, tolerance = 0.02, plot = True):
    """
    Estima el tiempo de relajación (t_relax) de un lattice para el modelo de Ising 2D.

    Parámetros:
        lattice_initial : np.array
            Lattice inicial (N x N) de spins (+1 o -1).
        T_red : float
            Temperatura reducida del sistema.
        n_steps : int
            Número total de intentos de flip.
        measure_every : int
            Cada cuántos intentos de flip se mide la magnetización.
        tolerance : float
            Tolerancia para definir equilibrio (por ejemplo 0.02 = 2%).
        plot : bool
            Si True, grafica magnetización vs pasos.

    Retorna:
        t_relax : int
            Tiempo de relajación en número de intentos de flip.
        mag_history : np.array
            Magnetización registrada en cada medición.
        steps_recorded : np.array
            Pasos correspondientes a cada medición.
    """
    lattice = lattice_initial.copy()
    mag_history = []

    # Simulación midiendo cada measure_every flips
    for step in range(0, n_steps, measure_every):
        lattice = metropolis_algorithm(lattice, T_red, measure_every)
        mag_history.append(magnetization(lattice))

    mag_history = np.array(mag_history)
    steps_recorded = np.arange(0, n_steps, measure_every)

    # Estimar valor de equilibrio como promedio de últimos 10%
    equilibrium_mag = np.mean(mag_history[-int(len(mag_history)*0.1):])

    # Encontrar primer paso dentro de la tolerancia
    t_relax = steps_recorded[-1]  # default por si no se encuentra antes
    for idx, mag in enumerate(mag_history):
        if np.abs(mag - equilibrium_mag) < tolerance:
            t_relax = steps_recorded[idx]
            break

    # Graficar si se desea
    if plot:
        plt.figure(figsize = (8,5))
        plt.plot(steps_recorded, mag_history, label = "Magnetización")
        plt.axhline(equilibrium_mag, color = 'red', linestyle = '--', label = "Valor equilibrio")
        plt.axvline(t_relax, color = 'green', linestyle='--', label=f"t_relax ≈ {t_relax}")
        plt.xlabel("Intentos de flip")
        plt.ylabel("Magnetización")
        plt.title(f"Tiempo de relajación a T*={T_red}")
        plt.legend()
        plt.grid(True)
        plt.show()

    return t_relax, mag_history, steps_recorded

n = 2 # length 
lattice_initial = initial_random_state(n) # estado ordenado
T_red = 1

t_relax, mag_history, steps = estimate_relaxation_time(lattice_initial, T_red,
                                                      n_steps = 10000000,
                                                      measure_every = 100,
                                                      tolerance = 0.01 ,
                                                      plot = True)

print(f"Tiempo de relajación aproximado: {t_relax} pasos de flip")