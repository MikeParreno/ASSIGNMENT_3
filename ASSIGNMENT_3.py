import numpy as np
# NO. 1 - Saving, Writing using Numpy
# Save to a text file:
A = np.array([[13, 4, 3 ],[1, 2, 0]])
np.savetxt('array1.txt', A)
# Load from a text file:
load_A = np.loadtxt('array1.txt')
print(f'TEXT FILE: \n{load_A}')
print()
# Save to a Binary File:
B = np.array([[11, 12, 13], [14, 15, 16]])
np.save("data.npy", B)
# Load the data from the NumPy binary file:
load_data = np.load("data.npy")
print(f'BINARY FILE: \n{load_data}')
print()
# Save data to Npz file:
C = np.array([[1,2,3,4]])
D = np. array([[4,3,2,1]])
E = np.array([[5,6,7,8]])
F = np.array([[8,7,6,5]])
G = np. array([[9,10,11,12]])
H = np.array([[12,11,10,9]])
#save array to binary file
np.savez('data.npz', C=C, D=D, E=E, F=F, G=G,H=H,)
# load from an npz file
load_data = np.load('data.npz')
print('NPZ FILE: ')
print(C[0])
print(D[0])
print()
print(E[0])
print(F[0])
print()
print(G[0])
print(H[0])