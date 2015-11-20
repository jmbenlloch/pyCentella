
from ROOT import TFile, TTree
from Centella.AAlgo import AAlgo
from Centella.physical_constants import *

from array import *

class algo_example(AAlgo):

    def __init__(self,param=False,level = 1,label="",**kargs):

        """
        
        Deal here with your parameters in param and kargs.
        If param is an instace of ParamManager, parameters
        will be set as algorithm parameters by AAlgo.
            
        """
        
        self.name='algo_example'
        AAlgo.__init__(self,param,level,self.name,0,label,kargs)

        # your stuff here...


    def initialize(self):

        """

        You can use here:

            self.hman     -----> histoManager instance
            self.tman     -----> treeManager instance
            self.logman   -----> logManager instance
            self.autoDoc  -----> latex_gen instance
        
        """
        
        self.m.log(1,'+++Init method of algo_example algorithm+++')

        self.hman.h1("petalo","petalo",100,0,1000)

        return

    def execute(self,event=""):

        """
        
        You can also use here:

            self.event ----> current event from the input data 
            
        """
          
        self.hman.fill("petalo",event.GetID());
                 
        return True

    def finalize(self):


        self.m.log(1,'+++End method of algo_example algorithm+++')

        return

    
