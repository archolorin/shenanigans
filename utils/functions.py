from utils import CommandChoiceMenu as ccm
from utils import StatusWindow as swin
from utils import var
import os


def mainLoop():

    while True:
        var.running_time = (var.time.time() - var.commandvals.start_time)
        var.commandvals.run_time = var.running_time
        var.rngSeed()
        var.rng()
        ccm.CommandMenu.CCGUI()
        #print('Commands Issued')
        ccm.execstats()
        #ccm.CommandProcWindow()
        #var.cmdRef()
        swin.StatWin.statGui()


#def executionLoop():
#swin.StatWin.statGui()
