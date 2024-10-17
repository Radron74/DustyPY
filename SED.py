import utils

class SED():

    def __init__(self, Flux = list, wavelength = list):
        self._Flux = Flux
        self._Wavelength = wavelength
        
    def set_Flux(self, Flux):
        self._Flux = Flux

    def set_Wavelength(self, wavelength):
        self._Wavelength = wavelength

    def PlotSED(self, kwargs={}):
        utils.ScatterPlot(self._Flux,self._Wavelength,kwargs=kwargs)

if __name__=='__main__':
    f= [1,2,3,4]
    w = [0.1,0.2,0.4,0.8]

    k = {'marker':'+', 'color':'red'}

    s = SED(Flux=f,wavelength=w)
    s.PlotSED(kwargs=k)