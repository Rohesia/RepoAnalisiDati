# utils.py

import numpy as np
import os

# --- Lettura di un CSV numerico ---
def read_csv(path):
    
    if not os.path.exists(path):
        return None

    data = np.genfromtxt(path, delimiter=',', dtype=float)
    if data.ndim == 1:
        data = data.reshape(-1, 1) 
    return data

# --- Salvataggio dell'array ---
def save_csv(array, filename):
    
    np.savetxt(filename + ".csv", array, delimiter=',', fmt='%.4f')
