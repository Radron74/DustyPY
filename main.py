from stars import Star, Model, Dust
from dusty import Dusty

if __name__== '__main__':
    S1 = Star(Name='E1',Temperature=4000)
    S2 = Star(Name='E2',Temperature=7000)

    dust = Dust(DustSize={'amin' : 0.3, 'amax': 10}, Composition={'Mg2SiO4':0.5, 'Fe':0.5})

    mod = Model('AFGL4106', NbStar=2, Stars=[S1,S2], Dust=dust)
   
    fit = Dusty(PATH='/Users/gabriel/Documents/Stage/code/dustyV2/', Model=mod)

    print(fit.get_Model().get_Dust().get_Composition())

    fit.ChangeParameter()
    fit.PrintParam()

    #fit.test()


    #fit = Dusty(PATH = '/Users/gabriel/Documents/Stage/code/dustyV2/')

    #fit.ChangeParameter(Star=S,tau=0.2)
    #fit.PrintParam(Star=S)
    #fit.LunchDusty()