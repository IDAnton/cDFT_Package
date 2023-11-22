import os
import time
import numpy as np
import cDFT.minimisation as minimise
import cDFT.measures as measure
from multiprocessing import Pool


def calculate(bulk_density):
    DFT = minimise.DFT(bulk_density=bulk_density,
                       temperature=1.0,
                       fluid_type='HS', functional='WB')
    planar = minimise.planar(DFT,
                             wall_type='HW', ng=1000, alpha=0.001)
    planar.minimise()
    planar.pressure()
    measure.adsorption(planar, fout=True)


if __name__ == '__main__':
    bulk_density = [0.304665, 0.700782, 0.856918]
    with Pool() as pool:
        print(pool.map(calculate, bulk_density))
