import subprocess
import glob

from stars import Model

class Dusty():

    def __init__(self, PATH='', Model=Model):
        self._dustyPath = PATH
        self._Model = Model
        self.__Check()

    def set_Model(self, Model):
        self._Model = Model
        self.__Check()

    def get_Model(self):
        return self._Model

    def set_PATH(self, Path):
        self._dustyPath = Path

    def AvailableComposition(self):
        NkFiles = [file.split('/')[-1].split('.')[0] for file in glob.glob(self._dustyPath+'/Lib_nk/*.nk')]
        #print(NkFiles)
        return NkFiles
        

    def ChangeParameter(self):
        i_T,i_tau,i_comp,i_abun= 0,0,0,0
        file = []
        line_T,line_tau, line_comp, line_abun = [],[],[],[]

        name = self._Model.get_Name()
        Stars = self._Model.get_Stars()

        T = [str(Star.get_Temperature()) for Star in Stars]
        dust = self._Model.get_Dust()

        with open(self._dustyPath+name+'.inp' , 'r') as f:
            lines = f.readlines()
            for j,lin in enumerate(lines):
                if 'Temperature' in lin and i_T == 0:
                    i_T=j
                    line_T=lin.split(' ')
                if 'tau(min)' in lin and i_tau == 0:
                    i_tau=j
                    line_tau=lin.split(' ')
                if 'Number of additional components' in lin and i_comp == 0:
                    i_comp = j
                    line_comp = lin.split(' ')
                if 'Abundances for these components' in lin and i_abun == 0:
                    i_abun = j
                    line_abun = lin.split(' ')
                
            file = lines

        line_T[-2] = f'{",".join(T)}'
        line_T = " ".join(line_T)
        file[i_T] = line_T
        
        line_tau[-10] = f'{dust.get_tau()}'
        line_tau[-13] = f'{dust.get_tau()};'
        line_tau = " ".join(line_tau)
        file[i_tau] = line_tau

        line_comp[5] = str(len(dust.get_Composition().keys()))
        line_comp[9] = ",".join(f'{comp}'+'.nk' for comp in dust.get_Composition().keys())
        line_comp = " ".join(line_comp) + '\n'
        file[i_comp] = line_comp

        print(line_abun)

        line_abun[8] = ",".join(f'{ab}' for ab in dust.get_Composition().values())
        line_abun = " ".join(line_abun)
        file[i_abun] = line_abun


        with open(self._dustyPath+name+'.inp' , 'w') as f:
            f.write("".join(file))

    def PrintParam(self):
        name = self._Model.get_Name()
        with open(self._dustyPath+name+'.inp' , 'r') as f:
            lines = f.readlines()
            for line in lines[:73]:
                print(line)

    def LunchDusty(self):
        subprocess.check_call(['./dusty'],cwd=self._dustyPath)

    def GetResults(self):
        print('Not implemented yet')
        return None

    def __Check(self):
        for species in self._Model.get_Dust().get_Composition():
            if species not in self.AvailableComposition():
                raise ValueError(f'The following species does not exist: {species}')

