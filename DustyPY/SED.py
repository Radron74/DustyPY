from . import utils as utils

class SED():
    """
    Class representing a Spectral Energy Distribution (SED).

    Attributes:
    _Flux (list): The fluxes of the SED.
    _Wavelength (list): The wavelengths of the SED.
    """

    def __init__(self, Flux=list, wavelength=list) -> None:
        """
        Initializes an instance of the SED class.

        Parameters:
        Flux (list, optional): The fluxes of the SED. Defaults to an empty list.
        wavelength (list, optional): The wavelengths of the SED. Defaults to an empty list.
        """
        self._Flux = Flux
        self._Wavelength = wavelength
        
    def set_Flux(self, Flux) -> None:
        """
        Sets the fluxes of the SED.

        Parameters:
        Flux (list): The fluxes of the SED.
        """
        self._Flux = Flux

    def set_Wavelength(self, wavelength) -> None:
        """
        Sets the wavelengths of the SED.

        Parameters:
        wavelength (list): The wavelengths of the SED.
        """
        self._Wavelength = wavelength

    def get_Flux(self) -> list:
        """
        Returns the fluxes of the SED.

        Returns:
        list: The fluxes of the SED.
        """
        return self._Flux
    
    def get_Wavelength(self) -> list:
        """
        Returns the wavelengths of the SED.

        Returns:
        list: The wavelengths of the SED.
        """
        return self._Wavelength

    def PlotSED(self, unit=None, xlim=None, ylim=None, ax=None, scale='linear', kwargs=None) -> None:
        """
        Plots the SED using the fluxes and wavelengths.

        Parameters:
        unit (str, optional): The unit of the axes. Defaults to None.
        xlim (tuple, optional): The limits of the x-axis. Defaults to None.
        ylim (tuple, optional): The limits of the y-axis. Defaults to None.
        ax (matplotlib.axes.Axes, optional): The axis on which to plot. Defaults to None.
        scale (str, optional): The scale of the axes ('linear' or 'log'). Defaults to 'linear'.
        kwargs (dict, optional): Additional arguments for the plot function. Defaults to None.
        """
        utils.Plot(self._Flux, self._Wavelength, unit=unit, xlim=xlim, ylim=ylim, ax=ax, scale=scale, kwargs=kwargs)

if __name__ == '__main__':
    f = [1, 2, 3, 4]
    w = [0.1, 0.2, 0.4, 0.8]

    k = {'marker': '+', 'color': 'red'}

    s = SED(Flux=f, wavelength=w)
    s.PlotSED(kwargs=k)