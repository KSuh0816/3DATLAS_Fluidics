
from Fluidics import *
from Fluidics import Fluidics


class LightSheetFluidics(Fluidics):
    def __init__(self,gui=False):
        super().__init__()  # call __init__ method of the super class
        self.verbose = True
        Protocol = getattr(importlib.import_module('SyringeProtocol'), 'SyringeProtocol')
        Pump = getattr(importlib.import_module('SyringePump_v2'), 'SyringePump_v2')
        Valve = getattr(importlib.import_module('ViciValve'), 'ViciValve')
        self.Protocol = Protocol(gui=gui)
        self.Pump = Pump('COM3',gui=gui)
        self.Valve = Valve('COM10',gui=gui)
        self.device = self.__class__.__name__
        self.Protocol.device = self.device
        self.Pump.device = self.device
        self.Valve.device = self.device
        self.Pump.wait_factor = 1/2
        self.Pump.speed_conversion = 0.446*(5/4) #s/mL
        self.Protocol.speed = 1
        self.Protocol.closed_speed = 0.25
        self.Protocol.wait_factor = self.Pump.wait_factor
        self.Protocol.speed_conversion = self.Pump.speed_conversion
        self.Protocol.vacuum_time=45
        self.Valve_Commands = {
                                'A':{'valve':1,'port':1},
                                'B':{'valve':1,'port':2},
                                'C':{'valve':1,'port':3},
                                'D':{'valve':1,'port':4},
                                'Water':{'valve':1,'port':5},
                                'Valve2':{'valve':1,'port':8},

                                'Waste':{'valve':2,'port':1},
                                'TBS':{'valve':2,'port':6},
                                'WBuffer':{'valve':2,'port':7},
                                'TCEP':{'valve':2,'port':8},
                                'StripTBS':{'valve':2,'port':9},
                                'Valve3':{'valve':2,'port':10},


                                'Hybe1':{'valve':3,'port':1},
                                'Hybe2':{'valve':3,'port':2},
                                'Hybe3':{'valve':3,'port':3},
                                'Hybe4':{'valve':3,'port':4},
                                'Hybe5':{'valve':3,'port':5},
                                'Hybe6':{'valve':3,'port':6},
                                'Hybe7':{'valve':3,'port':7},
                                'Hybe8':{'valve':3,'port':8},
                                'Hybe9':{'valve':3,'port':9},
                                'Hybe10':{'valve':3,'port':10},
                                'Hybe11':{'valve':3,'port':11},
                                'Hybe12':{'valve':3,'port':12},
                                'Hybe13':{'valve':3,'port':13},
                                'Hybe14':{'valve':3,'port':14},
                                'Hybe15':{'valve':3,'port':15},
                                'Hybe16':{'valve':3,'port':16},
                                'Hybe17':{'valve':3,'port':17},
                                'Hybe18':{'valve':3,'port':18},
                                'Hybe19':{'valve':3,'port':19},
                                'Hybe20':{'valve':3,'port':20},
                                'Hybe21':{'valve':3,'port':21},
                                'Hybe22':{'valve':3,'port':22},
                                'Hybe23':{'valve':3,'port':23},
                                'Hybe24':{'valve':3,'port':24},
                                'Valve3':{'valve':3,'port':10},

                                'Vacuum_A':{'valve':4,'port':1},
                                'Vacuum_B':{'valve':4,'port':2},
                                'Vacuum_C':{'valve':4,'port':3},
                                'Vacuum_D':{'valve':4,'port':4},
                                'Vacuum_Waster':{'valve':4,'port':9},
                            }
    