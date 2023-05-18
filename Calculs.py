from Maths import Maths
import numpy as np
from matplotlib import pyplot as plt

def trouver_angle(droites):
    models = []
    for i in range(len(droites[0])):
        try:
            models.append(mod(droites[0][i], droites[1][i]))
        except:
            models.append([])
    for i in range(len(models)):
        try:
            if models[i][0][1][0] is True:
                param = list(models[i][0][2])
                plt.plot(droites[0][i],[models[i][0][3](j,*param) for j in droites[0][i]])
        except:
            pass
    plt.show()
    max = 0

def mod(x, y):
    return Maths.mod.fit(x, y)

def get_angle(d1, d2):
    v1, v2 = [d1[0][1] - d1[0][0], d1[1][1] - d1[1][0]], [d2[0][1] - d2[0][0], d2[1][1] - d2[1][0]]
    prod_scal = np.dot(v1, v2)
    return np.arccos(prod_scal/(np.sqrt(v1[0]**2 + v1[1]**2)*np.sqrt(v2[0]**2 + v2[1]**2)))