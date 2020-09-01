import numpy as np
import matplotlib.pyplot as plt
#------------------------------------------------------------------------
def neighbors(i, j, grid_size):	
	list=[]
	if ((j + grid_size - 1) % grid_size) <= j: #an to swmatidio den brisketai sthn deksia 
		list.append([i,(j + grid_size - 1) % grid_size])#to ekxoroume sthn lissta
	if ((j + 1) % grid_size) >= j:#upologizoume an to swmatidio den vriskete sta akra kai sugkekrimena sto aristero meros
		list.append([i,(j + 1) % grid_size])
	if ((i + grid_size - 1) % grid_size) <= i:#upologizoume an to swmatidio den vriskete sta akra kai sugkekrimena sto katw meros
		list.append([(i + grid_size - 1) % grid_size, j])            #dhlwsh sunarthsh
	if ((i + 1) % grid_size)>= i:#upologizoume an to swmatidio den vriskete sta akra kai sugkekrimena sto panw meros
		list.append ([(i + 1) % grid_size, j])	
	arr1 = np.array(list)
	return (arr1)
	
def count_neighbors(i, j, grid):
	idx = neighbors(i, j, grid.shape[0])
	return np.sum(grid[idx[:, 0], idx[:, 1]])
#-----------------------------------------------------------------------------
# Define the grid size
grid_size = 50

# Create a square grid of empty sites
grid = np.full((grid_size , grid_size), 0) 

# Find all empty sites
#arxikopohsh tou can_move wste na mporei na mpei sth while kai kanei epanalipseis me vash an mporoun na kounithon ta swmathdia
empty_sites_idx = np.argwhere(grid==0)                                       


# Select randomly an empty site 
new_empty_site = empty_sites_idx[np.random.randint(empty_sites_idx.shape[0])]

# Convert indices to tuple
new_empty_site = tuple(new_empty_site)

# Place a new particle
grid[new_empty_site] = 3 
idx = np.argwhere(grid==3)
can_move = idx[[count_neighbors(x[0], x[1], grid) == 0 for x in idx]]
#-----------------------------------------------------------------------------------

while can_move.size:
	#45-74 einai gia topothetisi X
	_r=np.random.rand()
	if _r <0.15:
		continue
	empty_sites_idx = np.argwhere(grid==0) # Find all empty sites
	# Select randomly an empty site 
	new_empty_site = empty_sites_idx[np.random.randint(empty_sites_idx.shape[0])]
	# Convert indices to tuple
	new_empty_site = tuple(new_empty_site)
	# Place a new particle
	grid[new_empty_site] = 3 	
	# Find the indices of all particles that can move
	idx = np.argwhere(grid==3)
	can_move = idx[[count_neighbors(x[0], x[1], grid) == 0 for x in idx]]
	q = 0.5
	for i_j in can_move:
		if np.random.rand() > q:
			continue
		i, j = tuple(i_j)
		# Select a random movement
		_r = np.random.rand()
		if _r < 0.25:
			grid[i, (j + grid_size - 1) % grid_size] = 3 #up
		elif _r < 0.50:
			grid[i, (j + 1) % grid_size] = 3 #down
		elif _r < 0.75:
			grid[(i + grid_size - 1) % grid_size , j] = 3 #left
		else:
			grid[(i + 1) % grid_size,j] = 3 #right
		grid[i, j] = 0
		
	#75-106 einai gia aporofisi O2(=p1)
	if _r<0.3:
		continue
	empty_sites_idx = np.argwhere(grid==0) # Find all empty sites
	# Select randomly an empty site 
	new_empty_site = empty_sites_idx[np.random.randint(empty_sites_idx.shape[0])]
	# Convert indices to tuple
	new_empty_site = tuple(new_empty_site)
	# Place a new particle
	grid[new_empty_site] = 5 	
	# Find the indices of all particles that can move
	idx = np.argwhere(grid==5)
	can_move = idx[[count_neighbors(x[0], x[1], grid) == 0 for x in idx]]
	q = 0.5
	for i_j in can_move:
		if np.random.rand() > q:
			continue
		i, j = tuple(i_j)
		# Select a random movement
		_r = np.random.rand()
		if _r < 0.25:
			grid[i, (j + grid_size - 1) % grid_size] = 5 #up
		elif _r < 0.50:
			grid[i, (j + 1) % grid_size] = 5 #down
		elif _r < 0.75:
			grid[(i + grid_size - 1) % grid_size , j] = 5 #left
		else:
			grid[(i + 1) % grid_size,j] = 5 #right
		grid[i, j] = 4
		
	#107-137 einai gia apobolh O2(=p2)
	if _r<0.45:
		continue
	empty_sites_idx = np.argwhere(grid==0) # Find all Oxygen sites
	# Select randomly an empty site 
	new_empty_site = empty_sites_idx[np.random.randint(empty_sites_idx.shape[0])]
	# Convert indices to tuple
	new_empty_site = tuple(new_empty_site)
	# Place a new particle
	grid[new_empty_site] = 4 	
	# Find the indices of all particles that can move
	idx = np.argwhere(grid==4)
	can_move = idx[[count_neighbors(x[0], x[1], grid) == 0 for x in idx]]
	q = 0.5
	for i_j in can_move:
		if np.random.rand() > q:
			continue
		i, j = tuple(i_j)
		# Select a random movement
		_r = np.random.rand()
		if _r < 0.25:
			grid[i, (j + grid_size - 1) % grid_size] = 4 #up
		elif _r < 0.50:
			grid[i, (j + 1) % grid_size] = 4 #down
		elif _r < 0.75:
			grid[(i + grid_size - 1) % grid_size , j] = 4 #left
		else:
			grid[(i + 1) % grid_size,j] = 4 #right	
		grid[i, j] = 3
	
	#107-137 einai gia apobolh O2 kai dhmiourgia duo energwn thesewn(=p3)	
	if _r<0.6:
		continue
	empty_sites_idx = np.argwhere(grid==0) # Find all Oxygen sites
	# Select randomly an empty site 
	new_empty_site = empty_sites_idx[np.random.randint(empty_sites_idx.shape[0])]
	# Convert indices to tuple
	new_empty_site = tuple(new_empty_site)
	# Place a new particle
	grid[new_empty_site] = 2 	
	# Find the indices of all particles that can move
	idx = np.argwhere(grid==2)
	can_move = idx[[count_neighbors(x[0], x[1], grid) == 0 for x in idx]]
	q = 0.5
	for i_j in can_move:
		if np.random.rand() > q:
			continue
		i, j = tuple(i_j)
		# Select a random movement
		_r = np.random.rand()
		if _r < 0.25:
			grid[i, (j + grid_size - 1) % grid_size] = 2 #up
		elif _r < 0.50:
			grid[i, (j + 1) % grid_size] = 2 #down
		elif _r < 0.75:
			grid[(i + grid_size - 1) % grid_size , j] = 2 #left
		else:
			grid[(i + 1) % grid_size,j] = 2 #right	
		grid[i, j] = 2
		
	#166-194 einai gia emfanish CO	
	if _r<0.75:
		continue
	empty_sites_idx = np.argwhere(grid==0) # Find all Oxygen sites
	# Select randomly an empty site 
	new_empty_site = empty_sites_idx[np.random.randint(empty_sites_idx.shape[0])]
	# Convert indices to tuple
	new_empty_site = tuple(new_empty_site)
	# Place a new particle
	grid[new_empty_site] = 7 	
	# Find the indices of all particles that can move
	idx = np.argwhere(grid==7)
	can_move = idx[[count_neighbors(x[0], x[1], grid) == 0 for x in idx]]
	q = 0.5
	for i_j in can_move:
		if np.random.rand() > q:
			continue
		i, j = tuple(i_j)
		# Select a random movement
		_r = np.random.rand()
		if _r < 0.25:
			grid[i, (j + grid_size - 1) % grid_size] = 7 #up
		elif _r < 0.50:
			grid[i, (j + 1) % grid_size] = 7 #down
		elif _r < 0.75:
			grid[(i + grid_size - 1) % grid_size , j] = 7 #left
		else:
			grid[(i + 1) % grid_size,j] = 7 #right	
		grid[i, j] = 0
	
	#196-224 einai gia dhmiourgia CO2	
	if _r<0.9:
		continue
	empty_sites_idx = np.argwhere(grid==7) # Find all Oxygen sites
	# Select randomly an empty site 
	new_empty_site = empty_sites_idx[np.random.randint(empty_sites_idx.shape[0])]
	# Convert indices to tuple
	new_empty_site = tuple(new_empty_site)
	# Place a new particle
	grid[new_empty_site] = 6 	
	# Find the indices of all particles that can move
	idx = np.argwhere(grid==6)
	can_move = idx[[count_neighbors(x[0], x[1], grid) == 0 for x in idx]]
	q = 0.5
	for i_j in can_move:
		if np.random.rand() > q:
			continue
		i, j = tuple(i_j)
		# Select a random movement
		_r = np.random.rand()
		if _r < 0.25:
			grid[i, (j + grid_size - 1) % grid_size] = 6 #up
		elif _r < 0.50:
			grid[i, (j + 1) % grid_size] = 6 #down
		elif _r < 0.75:
			grid[(i + grid_size - 1) % grid_size , j] = 6 #left
		else:
			grid[(i + 1) % grid_size,j] = 6 #right	
		grid[i, j] = 0	
		
	#196-224 einai gia apobolh CO2	
	if _r<0.9:
		continue
	empty_sites_idx = np.argwhere(grid==6) # Find all Oxygen sites
	# Select randomly an empty site 
	new_empty_site = empty_sites_idx[np.random.randint(empty_sites_idx.shape[0])]
	# Convert indices to tuple
	new_empty_site = tuple(new_empty_site)
	# Place a new particle
	grid[new_empty_site] = 8 	
	# Find the indices of all particles that can move
	idx = np.argwhere(grid==8)
	can_move = idx[[count_neighbors(x[0], x[1], grid) == 0 for x in idx]]
	q = 0.5
	for i_j in can_move:
		if np.random.rand() > q:
			continue
		i, j = tuple(i_j)
		# Select a random movement
		_r = np.random.rand()
		if _r < 0.25:
			grid[i, (j + grid_size - 1) % grid_size] = 8 #up
		elif _r < 0.50:
			grid[i, (j + 1) % grid_size] = 8 #down
		elif _r < 0.75:
			grid[(i + grid_size - 1) % grid_size , j] = 8 #left
		else:
			grid[(i + 1) % grid_size,j] = 8 #right	
		grid[i, j] = 3		
import matplotlib.pyplot as plt
from numpy.random import random
aux = np.argwhere(grid == 3)
count=0# mia metavlith gia na vlepoume posa stoixeia exoun mpei 
for k in aux:
	count+=1
x, y = aux.T
count=0# mia metavlith gia na vlepoume posa stoixeia exoun mpei 
aux2 = np.argwhere(grid == 5)
for k in aux2:
	count+=1
x2, y2 = aux2.T
count=0# mia metavlith gia na vlepoume posa stoixeia exoun mpei 
aux3 = np.argwhere(grid == 4)
for k in aux3:
	count+=1
x3, y3 = aux3.T
count=0# mia metavlith gia na vlepoume posa stoixeia exoun mpei 
aux4 = np.argwhere(grid == 2)
for k in aux4:
	count+=1
x4, y4 = aux4.T
count=0# mia metavlith gia na vlepoume posa stoixeia exoun mpei 
aux5 = np.argwhere(grid == 7)
for k in aux5:
	count+=1
x5, y5 = aux5.T
count=0# mia metavlith gia na vlepoume posa stoixeia exoun mpei 
aux6 = np.argwhere(grid == 6)
for k in aux6:
	count+=1
x6, y6 = aux6.T
count=0# mia metavlith gia na vlepoume posa stoixeia exoun mpei
aux7 = np.argwhere(grid == 8)
for k in aux7:
	count+=1
x7, y7 = aux7.T
colors = ['b','r','g','y','c','m','k']
Energy = plt.scatter(x,y, color=colors[0])
Not_energy = plt.scatter(x2,y2, color=colors[1])
energy=plt.scatter(x3,y3, color=colors[2])
energy2=plt.scatter(x4,y4,color=colors[3])
energy7=plt.scatter(x5,y5,color=colors[4])
energy6=plt.scatter(x6,y6,color=colors[5])
energy8=plt.scatter(x7,y7,color=colors[6])
plt.legend((Energy,Not_energy,energy,energy2,energy7,energy6,energy8),
           ('Ενεργές Θέσεις', ' Απορόφηση Οξυγόνου','Αποβολή Οξυγόνου', 'Δύο ενεργές θέσεις με οξυγόνο','Μονοξείδιο του άνθρακα','Διοξείδιο του Άνθρακα','Αποβολή Διοξειδίου Ανθρακα'),
           scatterpoints=1,
           loc='upper left',
           ncol=10,
           fontsize=6)

plt.show()
plt.pause(1e+9)
plt.clf()
plt.ion()
