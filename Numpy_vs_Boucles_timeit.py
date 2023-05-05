from timeit import timeit
N = 300
setup = """
import numpy as np
n = int(1e5)
"""
code_boucle = """
np.sum([1. / i for i in range(1, n)]) - np.log(n)
"""
time_boucle=timeit(code_boucle,setup=setup,number=N)

code_numpy = """
np.sum(1. / np.arange(1, n)) - np.log(n)
"""
time_numpy=timeit(code_numpy,setup=setup,number=N) 

print("Facteur : {}".format(time_boucle/time_numpy))