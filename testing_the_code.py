from ising import * 

n = 10 # the lattice side lenght (could be added as an input)
N = n * n # the number of total spins


# First : plotting the initial stae 

# lattice = initial_random_state(n) # we could generate a state with all 1's pr -1's if we wanted. Check np_zeros_like(n) (+-1)
# plt.imshow(lattice, cmap = 'bwr', interpolation = 'nearest', extent = [0, n, 0, n]) #extent ensures that the positions are correct 
# cbar = plt.colorbar()
# cbar.set_ticks([-1, 1])
# cbar.set_label('Spin')
# plt.title('Lattice initial state')
# plt.show()

# Second : trying out the energy function 

# bound_state = np.zeros((n, n)) - 1 # bound state 

# print('The value that we compute for the energy is ', energy(bound_state))
# print('The real value of the energy is ', -2 * n**2)

# Third : first neighbours 