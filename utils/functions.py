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
        ccm.CommandProcWindow()
				Commands.cmdRef()
        swin.StatWin.statGui()


#def executionLoop():
    		#swin.StatWin.statGui()

class Commands:

    def cmdRef():
        cmdsq = var.opsMetrics.opsNum
        print('OPSCONFIG: ', cmdsq)
        try:
          cmdsq == os.environ['Black_Cathedral']
        if cmdsq == True:
            print('\n')
            print('-----Executing Order: ', cmdsq)
            print('-----CRITICAL EMERGENCY ISSUED-----')
            print('-_-_-ALL SYSTEMS COMPROMISED-_-_-')
            print('----------ALL SYSTEMS TERMINATING----------')
            print('__________WIPING ALL DATA__________')
            print(os.environ['Black_Cathedral'])
          ##else:
            #print('NOPE')
        except:
            print('ERROR')

        #except:
            #print('ERROR')
            #continue