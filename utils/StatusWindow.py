import PySimpleGUI as sg
from utils.var import opsMetrics as om
from utils import CommandChoiceMenu as ccm
from utils import functions as fn


class StatWin:
    sg.theme('darkgrey1')

    @staticmethod
    def statGui():
      ops = [
                [sg.Frame('Operational Metrics', 
                  [[sg.Text('Status:'), sg.T(om.stat)],
                  [sg.T('Current Orders:'), sg.T(om.opsNum)]]
                  )
                ],
                [sg.Submit('Modify'), sg.Button('Refresh', k='refresh', enable_events=True)]
              ]

        #statLayout = [sg.Frame('Operating Status', layout = ops)]
        
        #layout = [ops]

      window = sg.Window('AIGCC Operations', ops)

      while True:

				#event, values = window.Read()
        

        #if event == sg.WIN_CLOSED or event == 'Exit':
            #quit()

        #if event == 'refresh':
				    #fn.Commands.cmdRef()
						#continue

				#if event == 'Modify':
						#break
						#window.Close()
						


        window.Close()

            