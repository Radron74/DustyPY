import matplotlib.pyplot as plt
import numpy as np
import subprocess
import glob
import pandas as pd
import astropy

def ScatterPlot(Flux, Wavelength, unit = {'x':'Wavelength', 'y': 'Flux'}, scale='linear',kwargs={}):
    """Create a scatter plot

    Args:
        Flux (array): Flux 
        Wavelength (array): Wavelength
        unit (dict, optional): Description of what is show on each axes. Defaults to {'x':'Wavelength', 'y': 'Flux'}.
        scale (str, optional): Y axe scale. Defaults to 'linear'.
        kwargs (dict, optional): matplolib.pyplot kwargs. Defaults to {}.
    """
    fig,ax = plt.subplots()

    ax.scatter(Wavelength,Flux,**kwargs)
    ax.set_xlabel(f'{unit['x']}')
    ax.set_ylabel(f'{unit['y']}')

    ax.set_yscale(scale)

    plt.show()

def PrintFile(file, stop=-1):
    """Print a file

    Args:
        file (string): Path to the file
        stop (int, optional): line where to stop printing. Defaults to -1.
    """
    with open(file , 'r') as f:
            lines = f.readlines()
            for line in lines[:stop]:
                print(line)

def LoadFile(file):
    """Load a file in an array

    Args:
        file (string): Path to the file 

    Returns:
        array: array containing the lines of the file
    """

    with open(file , 'r') as f:
        lines = f.readlines()
        return lines
    
def LoadCSV(file, sep=','):
    """Load a csv file

    Args:
        file (string): Path to the file 

    Returns:
        Dataframe: dataframe containing the csv file
    """
    return pd.read_csv(file, sep=sep)

def LoadFits(file):
    """Load a fits file

    Args:
        file (string): Path to the file 

    Returns:
        array: array containing the file
    """
    return astropy.io.fits.open(file)[0].data 

def SearchLine(f,line):
     for i,lines in enumerate(f):
        if line in lines:
            return i 

if __name__=="__main__":
     
     f = LoadFile('/Users/gabriel/Documents/SFit/AFGL4106.inp')
     i = SearchLine(f, 'Number of additional components')
     print(f[i])