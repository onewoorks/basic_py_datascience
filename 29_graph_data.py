import numpy as np 

G_dense = np.array([
    [0,2,1],
    [2,0,0],
    [1,0,0]
])

G_masked = np.ma.masked_values(G_dense, 0)

from scipy.sparse import csr_matrix

G_sparse = csr_matrix(G_dense)
print(G_sparse.data)

print('\n')

from scipy.sparse.csgraph import csgraph_from_dense
G2_data = np.array([
    [np.inf, 2,0],
    [2, np.inf, np.inf],
    [0, np.inf, np.inf]
])

G2_sparse = csgraph_from_dense(G2_data, null_value=np.inf)
print(G2_data)