import PySimpleGUI as sg
from utils.var import opsMetrics as om
import utils
#import time


class StatWin:
    sg.theme('darkgrey1')


    @classmethod
    def statGui(cls):
        ops = [[
            sg.Frame('Operational Metrics',
                     [[sg.Text('Status:'), sg.T(om.stat)],
                      [sg.T('Current Orders:'),
                       sg.T(om.opsNum)]])
        ], [sg.Submit('Modify'), sg.B('Refresh')]]

        layout = [ops]

        window = sg.Window('AIGCC Operations', layout)
        while True:
            event = window.Read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            if event == 'Refresh':
                utils.var.cmdRef()
            if event == 'Modify':
                break
        window.close()
