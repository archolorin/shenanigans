from utils import CommandChoiceMenu as ccm
from utils import var
from utils import functions as fnc


 #Starts the running clock
var.opsClock()
 #Initial loading screen
ccm.CustomMeter()
 #Launches the main program after loaded
fnc.mainLoop()