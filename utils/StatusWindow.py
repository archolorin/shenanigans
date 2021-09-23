import PySimpleGUI as sg
from utils.var import opsMetrics as om
import utils
import time


class StatWin:
    sg.theme('darkgrey1')

    def statGui():
        ops = [[
            sg.Frame('Operational Metrics',
                     [[sg.Text('Status:'), sg.T(om.stat)],
                      [sg.T('Current Orders:'),
                       sg.T(om.opsNum)]])
        ], [sg.Submit('Modify'), sg.B('Refresh')]]
        
        ops2 = [[
            sg.Frame('Operational Metrics',
                     [[sg.Text('Status:'), sg.T(om.stat)],
                      [sg.T('Current Orders:'),
                       sg.T(om.opsNum)]])
        ], [sg.Submit('Modify'), sg.B('Refresh')]]

        #statLayout = [sg.Frame('Operating Status', layout = ops)]

        layout = [ops]

        window = sg.Window('AIGCC Operations', layout)
        while True:
            event, values = window.Read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            if event == 'Refresh':
                utils.var.cmdRef()
                #time.sleep(1)
            if event == 'Modify':
                break
        window.close()
