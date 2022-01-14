from Numerical import Integration
from Numerical import Read
from Numerical import Interpolation
import numpy as np

mat,x_coords,z_coords = Read.get_data('F100',0.505,1.611)

inter_data=mat[:,0]

matrix_abcd = Interpolation.find_interpolants(z_coords,inter_data)
integration = Integration.Analytical_Int_1D(matrix_abcd,z_coords).integrator()
print(integration)
mini_mat = np.array([0,0,0,5])
matrix = np.array([mini_mat for i in range(10)])
coords = np.array([0,1,2,3,4,5,6,7,8,9,10])
#print(Numerical_Integration.Analytical_Int_1D(matrix,coords).quad_integrator())