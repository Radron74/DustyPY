import matplotlib.pyplot as plt
import numpy as np
import subprocess
import glob

def ScatterPlot(Flux, Wavelength, unit = {'x':'Wavelength', 'y': 'Flux'}, scale='linear',kwargs={}):
    fig,ax = plt.subplots()

    ax.scatter(Wavelength,Flux,**kwargs)
    ax.set_xlabel(f'{unit['x']}')
    ax.set_ylabel(f'{unit['y']}')

    ax.set_yscale(scale)

    plt.show()

def PrintFile(file, stop=-1):
    with open(file , 'r') as f:
            lines = f.readlines()
            for line in lines[:stop]:
                print(line)
