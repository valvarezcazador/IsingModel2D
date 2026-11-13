from ising import * 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.axes_grid1 import make_axes_locatable

# 1. Plotting the evolution of of the system at a given temperature 

n = 20 # size of the lattice
lattice = initial_random_state(n) #our initial state
steps = 1000000 # number of iterations
T_red = 2 # reduced temperature (2.269 is the critical temperature)

# Storing the 
mag_data = []

# Generating the figure
fig, (ax1, ax2) = plt.subplots(1, 2) #, figsize=(10, 5))

im = ax1.imshow(lattice, cmap = 'coolwarm', vmin = -1, vmax = 1, interpolation = 'nearest', extent = [0, n, 0, n])
ax1.set_title(f'Lattice (n = {n}, $T_r$ = {T_red})')

divider = make_axes_locatable(ax1)
cax = divider.append_axes('right', size = '5%', pad = 0.05)
cbar = fig.colorbar(im, cax = cax, ticks = [-1, 1])
cbar.ax.set_yticklabels(['-1', '+1'])  # opcional, más claro

line, = ax2.plot([], [], color = 'blue', marker = '.')
ax2.set_xlim(0, 1)
ax2.set_ylim(-1, 1)
ax2.set_xlabel('step')
ax2.set_ylabel('m')
ax2.set_title('m vs step')


def animate(frame):
    global lattice
    lattice = metropolis_algorithm(lattice, T_red, n**2)
    mag = magnetization(lattice)
    mag_data.append(mag)
    
    # Actualizar lattice
    im.set_data(lattice)
    
    # Actualizar curva de magnetización
    line.set_data(range(len(mag_data)), mag_data)
    
    # Ajustar eje x para que vaya de 0 al step actual
    ax2.set_xlim(0, frame + 1)
    
    return im, line

anim = FuncAnimation(fig, animate, frames = steps, interval = 5, blit = False, repeat = False)
plt.show()