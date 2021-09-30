import PySimpleGUI as sg
from utils.var import opsMetrics as om
import utils


class StatWin:


    overrideval = False

    sg.theme('darkgrey1')

    #@classmethod
    def statGui():
        ops = [[sg.Frame('Operational Metrics',
                     [[sg.Text('Status:'), sg.T(om.stat), sg.T('        '), sg.T('   Alarm:'), sg.T(om.alarmstat)],
                      [sg.Text('Operation:'), sg.T(om.opname), sg.T(''), sg.T('Override:'), sg.T(StatWin.overrideval)],
                      [sg.T('Current Orders:'),
                       sg.T(om.opsNum)]])
        ], [sg.Submit('Modify'), sg.B('Refresh'), sg.B('Override', k='ovrd')]]

        layout = [ops]

        window = sg.Window('AIGCC Operations', layout)
        while True:
            event, values = window.Read()
            print('Override Status:', StatWin.overrideval)
            if event == sg.WIN_CLOSED:
                break
            if event == 'Refresh':
                utils.var.cmdRef()
            if event == 'Modify':
                StatWin.overrideval = None
                break
            if event =='ovrd':
                StatWin.override()
        window.close()

    def override():


        ovrdwin = [[sg.InputText('')],
                  [sg.B('Submit'), sg.Cancel()]]

        window = sg.Window('Override', ovrdwin)

        while True:
            event, values = window.Read()
            print(values)
            if event == 'Submit':
                StatWin.overrideval = values[0]
                break
            if event == sg.WIN_CLOSED or 'Cancel':
                break
            print('override input:', values[0])
            print(values)

        window.close()