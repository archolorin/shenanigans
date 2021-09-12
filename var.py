from random import seed
from random import randint
from random import sample
from random import choice
#from random import random
#from datetime import datetime
import PySimpleGUI as sg
import CommandChoiceMenu
import time



class commandvals:
    V0 = None
    V1 = 0
    V2 = 0
    V3 = 0
    V4 = 0
    V5 = 0
    V6 = 0
    V7 = None
    #OPTIONS
    V8 = False
    V9 = False
    V10 = False
    V11 = False
    V12 = False
    V13 = False
    V14 = False
    V15 = False
    V16 = False
    V17 = False
    V18 = False
    #AUGMENTATIONS
    V19 = False
    V20 = False
    V21 = False
    V22 = False
    V23 = False
    V24 = False
    V25 = False
    V26 = False
    V27 = False

    rvalue = 100
    rseed = 0

    order = 0
    category = 0
    edict = 0
    priority = 0
    protocol = 0
    auth = 0
    stage = 0
    alarm = None

    run_time = 0
    start_time = None
    
    OS0 = False
    OS1 = False
    OS2 = False
    OS3 = False
    OS4 = False
    OS5 = False
    OS6 = False
    OS7 = False
    

def mainLoop():

    while True:
        running_time = (time.time() - commandvals.start_time)
        commandvals.run_time = running_time
        rngSeed()
        rng()
        CommandChoiceMenu.CommandMenu.CCGUI()
        #print('Commands Issued')
        CommandChoiceMenu.execstats()
        CommandChoiceMenu.CommandProcWindow()

def valueprinter():
    if commandvals.V0 != None:
      commandvals.order = commandvals.V0
      print('Order: ', commandvals.V0) 
    if commandvals.V1 > 0:
      commandvals.category = commandvals.V1
      print('Category: ', commandvals.V1) 
    if commandvals.V2 > 0:
      commandvals.edict = commandvals.V2
      print('Edict: ', commandvals.V2)
    if commandvals.V3 > 0:
      commandvals.priority = commandvals.V3
      print('Priority: ', commandvals.V3)
    if commandvals.V4 > 0:
      commandvals.protocol = commandvals.V4
      print('Protocol: ', commandvals.V4)
    if commandvals.V5 != 0:
      commandvals.auth = commandvals.V5
      print('Auth: ', commandvals.V5)
    if commandvals.V6 != 0:
      commandvals.stage = commandvals.V6
      print('Stage: ', commandvals.V6)
    if commandvals.V7 != None:
      commandvals.alarm = commandvals.V7
      print('Alarm Status: ', commandvals.V7)
    #else:
      #print('No Commands Executed')



#def ComExec():
    #ComExecVal = commandvals.V0, commandvals.V1, commandvals.V2, commandvals.V3, commandvals.V4, commandvals.V5, commandvals.V6, commandvals.V7
    #print(ComExecVal) 

def rng():
    seed(commandvals.rseed)
    for _ in range(1):
        rvalue = randint(100, 2000)
        commandvals.rvalue = rvalue
        #print('RValue: ', commandvals.rvalue)

def rngSeed():
    seed()
    sequence = [i for i in range(100000)]
    subset = sample(sequence, 100)
    for _ in range(1):
        selection = choice(subset)

    commandvals.rseed = commandvals.rseed + selection
    #print('\nSeed: ', selection)

def opsClock():
    start_time = time.time()
    commandvals.start_time = start_time
    #mainLoop()
    print("--- %s seconds ---" % (time.time() - start_time))
    running_time = (time.time() - start_time)
    time.strftime("%H:%M:%S", time.gmtime(running_time))
    commandvals.run_time = running_time
    print(time.strftime("%H:%M:%S", time.gmtime(running_time)))

def ClockPrint():
    time.strftime("%H:%M:%S", time.gmtime(commandvals.run_time))

def orderselection():
    if commandvals.OS0 != False:
        commandvals.V0 = 0
      #print('Order: ', commandvals.OS0) 
    if commandvals.OS1 != False:
        commandvals.V0 = 1
      #print('Order: ', commandvals.OS1) 
    if commandvals.OS2 != False:
        commandvals.V0 = 2
      #print('Order: ', commandvals.OS2)
    if commandvals.OS3 != False:
        commandvals.V0 = 3
      #print('Order: ', commandvals.OS3)
    if commandvals.OS4 != False:
        commandvals.V0 = 4
      #print('Order: ', commandvals.OS4)
    if commandvals.OS5 != False:
        commandvals.V0 = 5
      #print('Order: ', commandvals.OS5)
    if commandvals.OS6 != False:
        commandvals.V0 = 6
      #print('Order: ', commandvals.OS6)
    if commandvals.OS7 != False:
        commandvals.V0 = 7
      #print('Order: ', commandvals.OS7)

def orderentry():
    CommandChoiceMenu.CommandMenu.values['Order#'] = commandvals.V0
    print(commandvals.V0)