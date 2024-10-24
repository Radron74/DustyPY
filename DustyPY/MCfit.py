import pymcmcstat
import pymcmcstat.MCMC
from . import utils as utils
from . import Data as Data
import numpy as np


class Fit():
    """
    Class representing a fitting procedure using MCMC.

    Attributes:
    _Model (pymcmcstat.MCMC.MCMC): The MCMC model.
    _Data (Data): The data to fit.
    _ParamFit (dict): The fitting parameters.
    _Param (dict): The model parameters.
    _Results (dict): The results of the fitting procedure.
    """

    def __init__(self, Data=Data.Data(), Model=pymcmcstat.MCMC.MCMC(), ParamFit=None, Param=None):
        """
        Initializes an instance of the Fit class.

        Parameters:
        Data (Data, optional): The data to fit. Defaults to an instance of Data.
        Model (pymcmcstat.MCMC.MCMC, optional): The MCMC model. Defaults to an instance of pymcmcstat.MCMC.MCMC.
        ParamFit (dict, optional): The fitting parameters. Defaults to a predefined dictionary.
        Param (dict, optional): The model parameters. Defaults to an empty dictionary.
        """
        if ParamFit is None:
            ParamFit = {
                        'nsimu': 10000,
                        'updatesigma': True,
                        'method': 'dram',
                        'adaptint': 100,
                        'verbosity': 0,
                        'waitbar': True,
                    }
        if Param is None:
            Param = {}

        self._Model = Model
        self._Data = Data
        self._ParamFit = ParamFit
        self._Param = Param
        self._Results = {}

    def set_Data(self, Data=None):
        """
        Sets the data to fit.

        Parameters:
        Data (Data, optional): The data to fit. Defaults to None.
        """
        if Data is None:
            Data = Data.Data()
        self._Data = Data

    def get_Data(self):
        """
        Returns the data to fit.

        Returns:
        Data: The data to fit.
        """
        return self._Data

    def set_Model(self):
        """
        Sets the MCMC model parameters and simulation options.

        Utilizes the utility function `SetMCMCParam` to set the model parameters and
        defines the simulation options using the fitting parameters.
        """
        utils.SetMCMCParam(self._Model, self._Param)
        self._Model.simulation_options.define_simulation_options(**self._ParamFit)

    def set_ParamFit(self, ParamFit):
        """
        Sets the fitting parameters for the MCMC model.

        Parameters:
        ParamFit (dict, optional): A dictionary containing the fitting parameters. If None, defaults to a predefined dictionary:
        {
            'nsimu': 10000,
            'updatesigma': True,
            'method': 'dram',
            'adaptint': 100,
            'verbosity': 0,
            'waitbar': True,
        }
        """
        if ParamFit is None:
            ParamFit = {
                        'nsimu': 10000,
                        'updatesigma': True,
                        'method': 'dram',
                        'adaptint': 100,
                        'verbosity': 0,
                        'waitbar': True,
                    }
        self._ParamFit = ParamFit

    def get_ParamFit(self):
        """
        Returns the fitting parameters for the MCMC model.

        Returns:
        dict: The fitting parameters.
        """
        return self._ParamFit
        
    def set_Param(self, Param):
        """
        Sets the model parameters for the MCMC model.

        Parameters:
        Param (dict): A dictionary containing the model parameters.
        """
        self._Param = Param

    def get_Param(self):
        """
        Returns the model parameters for the MCMC model.

        Returns:
        dict: The model parameters.
        """
        return self._Param

    def set_Chi2Func(self, func):
        """
        Sets the chi-squared function for the MCMC model.

        Parameters:
        func (function): The chi-squared function to be used by the MCMC model.
        """
        self._Model.model_settings.define_model_settings(sos_function=func)

    def get_Results(self):
        """
        Returns the results of the fitting procedure.

        Returns:
        dict: The results of the fitting procedure.
        """
        return self._Results

    def Fit(self, Chi2=utils.Chi2):
        """
        Performs the fitting procedure using the provided chi-squared function.

        Parameters:
        Chi2 (function, optional): The chi-squared function to be used for the fitting procedure. Defaults to utils.Chi2.
        """
        y = self._Data.get_ydata()
        x = self._Data.get_xdata()
        self._Model.data.add_data_set(x, y)
        self.set_Model()

        self.set_Chi2Func(Chi2)
        self._Model.run_simulation()

        results = {}
        results = self._Model.simulation_results.results.copy()

        self._Results = results

    def PrintResults(self):
        """
        Prints the results of the fitting procedure, including chain statistics.
        """
        chain = self._Results['chain']
        burnin = int(self._Results['nsimu'] / 2)
        self._Model.chainstats(chain[burnin:, :], self._Results)

    def PredictionModel(self):
        """
        Sets up the prediction model for calculating prediction intervals.
        """
        nds = len(self._Data.get_xdata())
        print(nds)

        def pred_modelfun(preddata, theta):
            return utils.model(theta[:2], preddata.xdata[0], preddata.ydata[0]).reshape(nds,)

        self._Model.PI.setup_prediction_interval_calculation(pred_modelfun)
    

if __name__=='__main__':
    dat = Data.Data(xdata=[0,1,2,3,4,5,6,7,8,9,10],ydata=[0,1,2,3,4,5,6,7,8,9,10])

    ParamFit = {
        'nsimu': 10000,
        'updatesigma': True,
        'method': 'dram',
        'adaptint': 100,
        'verbosity': 0,
        'waitbar': True,
    }

    f = Fit(Param={'I':{'theta0':1,'minimum':0,'maximum':2}},Data=dat)

    f.Fit()
    f.PrintResults()
    result = f.get_Results()['theta'][0]
    x = np.linspace(0,10,100)
    y = utils.model(q=result,x=dat.get_xdata(),y=dat.get_ydata())

    utils.Plot(y,dat.get_xdata())