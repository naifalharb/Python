import calc
from openpyxl import load_workbook
import pyinputplus as pyip


workbook = load_workbook(filename="NID.xlsx",data_only=True)



def profesions_update(str):
        workbook['Professions']['D2'] = calc.IT_Needed(workbook['CurrentSituation']['J'+ str].value,workbook['CurrentSituation']['H'+str].value)
        workbook['Professions']['D3'] = calc.IT_Needed(workbook['CurrentSituation']['D'+ str].value,workbook['CurrentSituation']['B'+str].value)
        workbook['Professions']['D4'] = calc.IT_Needed(workbook['CurrentSituation']['G'+ str].value,workbook['CurrentSituation']['E'+str].value)
        workbook['Professions']['D5'] = calc.IT_Needed(workbook['CurrentSituation']['M'+ str].value,workbook['CurrentSituation']['K'+str].value)
        workbook['Professions']['D6'] = calc.IT_Needed(workbook['CurrentSituation']['P'+ str].value,workbook['CurrentSituation']['N'+str].value)
        workbook['Professions']['D7'] = calc.IT_Needed(workbook['CurrentSituation']['S'+ str].value,workbook['CurrentSituation']['Q'+str].value)
        workbook['Nitaqat']['E2'] = workbook['CurrentSituation']['AC' + str].value / workbook['CurrentSituation']['AE' + str].value
        workbook['Nitaqat']['E3'] = workbook['CurrentSituation']['AC' + str].value / workbook['CurrentSituation']['AE' + str].value
        workbook['Nitaqat']['E4'] = workbook['CurrentSituation']['AC' + str].value / workbook['CurrentSituation']['AE' + str].value
        workbook['Nitaqat']['E5'] = workbook['CurrentSituation']['AC' + str].value / workbook['CurrentSituation']['AE' + str].value
        workbook.save('NID.xlsx')


def Nitaqat_update(int):
        workbook['Nitaqat']['B2'] = calc.LG_1Y(int)
        workbook['Nitaqat']['C2'] = calc.LG_2Y(int)
        workbook['Nitaqat']['D2'] = calc.LG_3Y(int)
        workbook['Nitaqat']['B3'] = calc.MG_1Y(int)
        workbook['Nitaqat']['C3'] = calc.MG_2Y(int)
        workbook['Nitaqat']['D3'] = calc.MG_3Y(int)
        workbook['Nitaqat']['B4'] = calc.HG_1Y(int)
        workbook['Nitaqat']['C4'] = calc.HG_2Y(int)
        workbook['Nitaqat']['D4'] = calc.HG_3Y(int)
        workbook['Nitaqat']['B5'] = calc.P_1Y(int)
        workbook['Nitaqat']['C5'] = calc.P_2Y(int)
        workbook['Nitaqat']['D5'] = calc.P_3Y(int)
        workbook.save('NID.xlsx')





R = pyip.inputMenu(["Aramco", "alRajhi", "Nadec", "STC", "ACS", "NTG", "LMS", "NID"],numbered=True)
S = ''
if R == 'Aramco':
        S = '2'
elif R == 'alRajhi':
        S = '3'
elif R == 'Nadec':
        S = '4'
elif R == 'STC':
        S = '5'
elif R == 'ACS':
        S = '6'
elif R == 'NTG':
        S = '7'
elif R == 'LMS':
        S = '8'
elif R == 'NID':
        S = '9'
profesions_update(S)
Nitaqat_update(workbook['CurrentSituation']['AE' + S].value)
print('####### ' + R)
