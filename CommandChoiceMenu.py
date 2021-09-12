import sys
import PySimpleGUI as sg
import var
import time

class CommandMenu:

    sg.theme('darkgrey1')

    def collapse(Layout, key):
        return sg.pin(sg.Column(Layout, key=key))


    def CCGUI():
        sg.SetOptions(text_justification='right')
                  ##__Execution Area__##
        flags = [
                  [sg.Frame('Command Configuration',
                  [[sg.Text('Order:', size=(8, 1)), sg.Spin(values=[i for i in range(0, 6)], initial_value=None, size=(6, 1), key='Order#'),
                    sg.Text('Cat:', size=(8, 1)), sg.Spin(values=[i for i in range(0, 10)], initial_value=0, size=(6, 1), key='Category')],
                  [sg.Text('Edict:', size=(8, 1)), sg.Spin(values=[i for i in range(0, 1000)], initial_value=0, size=(6, 1), key='Edict#'), 
                    sg.Text('P:', size=(8, 1)), sg.Spin(values=[i for i in range(0, 1000)], initial_value=0, size=(6, 1), key='Priority')],
                  [sg.Text('Protocol:', size=(8, 1)), sg.Spin(values=[i for i in range(0, 1000)], initial_value=0, size=(6, 1), key='Protocol#'), 
                    sg.Text('Auth:', size=(8, 1)), sg.Spin(values=[i for i in range(0, 10)], initial_value=0, size=(6, 1), key='Auth')],
                  [sg.Text('Stage:', size=(8, 1)), sg.Spin(values=[i for i in range(0, 10)], initial_value=0, size=(6, 1), key='Stage'), 
                    sg.Text('Alarm:', size=(8, 1)), sg.Drop(values=('Yes', 'No', None), default_value='None', auto_size_text=True, key='Alarm Status')]])],
                  ##__Augmentation Area__##
                  [sg.Frame('Augmentations', [[sg.Radio('Emergency', 'loss', size=(12, 1)), 
                   sg.Radio('Standard', 'loss', default=True, size=(12, 1))],
                  [sg.Radio('Delay', 'loss', size=(12, 1)), 
                   sg.Radio('Reset', 'loss', size=(12, 1))],
                  #[sg.Radio('Nuke', 'loss', size=(12, 1)), sg.Radio('Other', 'loss', size=(12, 1))],
                  [sg.Radio('Nuke', 'loss', size=(12, 1)), 
                   sg.Radio('Other', 'loss', size=(12, 1))]])],
                  ##__Option Area__##
                  [sg.Frame('Options', [
                  [sg.Checkbox('Select All', size=(12, 1), k='-OPTAll-', default=False, enable_events=True), 
                   sg.Checkbox('Select None', size=(20, 1), k='-OPTNone-', enable_events=True)],
                  [sg.Checkbox('Orders', k='-ORDCheckbox-', size=(12, 1), default=False, enable_events=True), 
                   sg.Checkbox('Edicts', k='OE', size=(20, 1))],
                  [sg.Checkbox('Protocols', k='OP', size=(12, 1)), 
                   sg.Checkbox('Authorizations', k='OK', size=(20, 1), default=False)],
                  [sg.Checkbox('Exec', k='OEX', size=(12, 1)), 
                   sg.Checkbox('Repeat', k='OR', size=(20, 1))],
                  [sg.Checkbox('Force', k='OF', size=(12, 1), default=False), 
                   sg.Checkbox('Override', k='OOR', size=(20, 1))],
                  [sg.Checkbox('Contain', k='OC', size=(12, 1)), 
                   sg.Checkbox('Flush', k='OFL', size=(20, 1), default=False)],
                  [sg.Checkbox('Plant Seeds', k='OS', size=(12, 1)), 
                   sg.Checkbox('Debug', size=(20, 1), key='-DBGCheckbox-', enable_events=True, default=False)]])]
                ]
        
        debug_window = [
                        [sg.Text(time.strftime("%H:%M:%S", time.gmtime(var.commandvals.run_time)))], 
                        [sg.Text('Seed: ', key='SEEDS'), 
                         sg.Text(var.commandvals.rseed)],
                        [sg.Text('RValue: '),
                         sg.Text(var.commandvals.rvalue)]
                       ]

        orders_window = [
                        [sg.Radio('0', 'orders', k='O0', size=(12, 1))], 
                        [sg.Radio('1', 'orders', k='O1', size=(20, 1))],
                        [sg.Radio('2', 'orders', k='O2', size=(12, 1))], 
                        [sg.Radio('3', 'orders', k='O3', size=(20, 1))],
                        [sg.Radio('4', 'orders', k='O4', size=(12, 1))], 
                        [sg.Radio('5', 'orders', k='O5', size=(20, 1))],
                        [sg.Radio('6', 'orders', k='O6', size=(12, 1))], 
                        [sg.Radio('7', 'orders', k='O7', size=(20, 1))],
                        [sg.Button('Confirm'), sg.Button('Return')]
                        ]    

        orders =  [[sg.Frame('Order Selection', layout = orders_window)]]
        console = [[sg.Frame('Console', layout = flags)]]
        debug =   [[sg.Frame('Debug', layout = debug_window)]]

        layout = [
                  [sg.Column(console), CommandMenu.collapse(orders, '-ORDWindow-'), CommandMenu.collapse(debug, '-DBGWindow-')],
                  [sg.Submit('Execute'), sg.Button('Clear'), sg.Cancel()],
                 ]

        
        window = sg.Window('Ai Galactic Command Console', layout, finalize=True, font=("Technic", 12))
        
        def selectNone():
          window['']

        def closeWinD():
            #window['SEEDS'](value=())
            window['-DBGCheckbox-'](False)
            window['-DBGWindow-'](visible=False)

        def openWinD():
            #window['SEEDS'](value=())
            window['-DBGCheckbox-'](True)
            window['-DBGWindow-'](visible=True)

        def closeWinO():
            window['-ORDCheckbox-'](False)
            window['-ORDWindow-'](visible=False)

        def openWinO():
            window['-ORDCheckbox-'](True)
            window['-ORDWindow-'](visible=True)

        def resetAll():
            window[values](value=None)


        #window['-DBGWindow-'](visible=False)
        sg.SetOptions(text_justification='left')
        closeWinD()
        closeWinO()
        while True:
            event, values = window.Read()
            #closeWinD()
            #closeWinO()
            running_time = (time.time() - var.commandvals.start_time)
            time.strftime("%H:%M:%S", time.gmtime(running_time))
            var.commandvals.run_time = running_time
            print(time.strftime("%H:%M:%S", time.gmtime(var.commandvals.run_time)))
            
            if values['-DBGCheckbox-']==True:
                 openWinD()

            if values['-DBGCheckbox-']==False:
                closeWinD()

            if values['-ORDCheckbox-']==True:
                openWinO()
                if event == 'Confirm':
                    if values['O0'] == True:
                        var.commandvals.OS0 = True
                    else:
                        var.commandvals.OS0 = False
                    var.commandvals.OS1 = values['O1']
                    var.commandvals.OS2 = values['O2']
                    var.commandvals.OS3 = values['O3']
                    var.commandvals.OS4 = values['O4']
                    var.commandvals.OS5 = values['O5']
                    var.commandvals.OS6 = values['O6']
                    var.commandvals.OS7 = values['O7']
                    var.orderselection()
                    print(var.commandvals.V0)
                    values['Order#']=var.commandvals.V0
                    window['Order#'](value=var.commandvals.V0)
                    print('\n')
                    print(values['Order#'])
                if event =='Return':
                    closeWinO()



            if values['-ORDCheckbox-']==False:
                 closeWinO()

            if event =='Clear':
                closeWinD()

            if event =='Execute':
                var.commandvals.V0 = values['Order#']
                var.commandvals.V1 = values['Category']
                var.commandvals.V2 = values['Edict#']
                var.commandvals.V3 = values['Priority']
                var.commandvals.V4 = values['Protocol#']
                var.commandvals.V5 = values['Auth']
                var.commandvals.V6 = values['Stage']
                var.commandvals.V7 = values['Alarm Status']
                var.valueprinter()
                #Debug Section, Uncomment to print variables
                #print(var.commandvals.V0)
                #print(var.commandvals.order)
                break

            if event =='Cancel':
                window.Close()
          
        
        #debug values
        #print(button, values)
        
        #var.valueprinter()

        #sg.Popup('lol')
        window.CloseNonBlocking()

def execstats():
    layout = [[sg.Text('Commands Issued: ')],
              [[sg.Text('Order:     '), sg.Text(var.commandvals.V0)]],
              [sg.Text('Category:'), sg.Text(var.commandvals.V1)],
              [sg.Text('Edict:       '), sg.Text(var.commandvals.V2)],
              [sg.Text('Priority:   '), sg.Text(var.commandvals.V3)],
              [sg.Text('Protocol: '), sg.Text(var.commandvals.V4)],
              [sg.Text('Auth:       '), sg.Text(var.commandvals.V5)],
              [sg.Text('Stage:     '), sg.Text(var.commandvals.V6)],
              [sg.Submit('Confirm'), sg.Cancel()]
             ]

    window = sg.Window('Execution Confirmation').Layout(layout)

    button, values = window.Read()
    if button == 'Cancel':
        window.Close()
        var.mainLoop()

    window.CloseNonBlocking()

def CustomMeter():
    # layout the form
    layout = [[sg.Text('Loading AIGCC...')],
              [sg.ProgressBar(100, orientation='h', size=(20,20), key='progress')],
              [sg.Cancel()]]

    # create the form`
    window = sg.Window('Launch Status').Layout(layout)
    progress_bar = window['progress']
    # loop that would normally do something useful
    for i in range(100):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.Read(timeout=0, timeout_key='timeout')
        if event == 'Cancel' or event == None:
            break
        # update bar with loop value +1 so that bar eventually reaches the maximum
        progress_bar.UpdateBar(i+20)
    # done with loop... need to destroy the window as it's still open
    window.CloseNonBlocking()

#if __name__ == '__main__':
#    CustomMeter()
#    CommandChoiceMenu()


def CommandProcWindow():
    layout = [[sg.Text('Command Accepted, Executing...')],
              [sg.ProgressBar(2000, orientation='h', size=(20,20), key='progress1')],
              [sg.Cancel()]]

    window = sg.Window('Command Status').Layout(layout)
    progress_bar = window['progress1']
    for i in range(var.commandvals.rvalue):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.Read(timeout=0, timeout_key='timeout')
        if event == 'Cancel' or event == None:
            break
        # update bar with loop value +1 so that bar eventually reaches the maximum
        progress_bar.UpdateBar(i+20)
    # done with loop... need to destroy the window as it's still open
    window.Close()
