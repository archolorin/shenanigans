from utils import CommandChoiceMenu as ccm
from utils import StatusWindow as swin
from utils import var


def mainLoop():

    while True:
         #Starts running clock
        var.running_time = (var.time.time() - var.commandvals.start_time)
        var.commandvals.run_time = var.running_time
         #Begins seed generation function
        var.rngSeed()
        var.rng()
         #Main GUI window
        ccm.CommandMenu.CCGUI()
         #converts Command Sequence into useable order
        var.cmdRef()
         #Displays user input command sequence for verification
        ccm.execstats()
         #Loading screen to wait for command sequence to be issued
        ##ccm.CommandProcWindow()
         #Displays operational monitoring and status
        swin.StatWin.statGui()