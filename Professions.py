import calc
from openpyxl import load_workbook


workbook = load_workbook(filename="NID.xlsx", data_only=True)
Professio = workbook['Professions']
CurrentSituation = workbook['CurrentSituation']
Nitaqa = workbook['Nitaqat']


def profesions_update(str):
        Professio['D2'] = calc.IT_Needed(CurrentSituation['J'+ str].value,CurrentSituation['H4'].value)
        Professio['D3'] = calc.IT_Needed(CurrentSituation['D'+ str].value,CurrentSituation['B4'].value)
        Professio['D4'] = calc.IT_Needed(CurrentSituation['G'+ str].value,CurrentSituation['E4'].value)
        Professio['D5'] = calc.IT_Needed(CurrentSituation['M'+ str].value,CurrentSituation['K4'].value)
        Professio['D6'] = calc.IT_Needed(CurrentSituation['P'+ str].value,CurrentSituation['N4'].value)
        Professio['D7'] = calc.IT_Needed(CurrentSituation['S'+ str].value,CurrentSituation['Q4'].value)
        workbook.save('NID.xlsx')


ifnt = CurrentSituation['AE4']

def Nitaqat_update(int):
        Nitaqa['B2'] = calc.LG_1Y(int)
        Nitaqa['C2'] = calc.LG_2Y(int)
        Nitaqa['D2'] = calc.LG_3Y(int)
        Nitaqa['B3'] = calc.MG_1Y(int)
        Nitaqa['C3'] = calc.MG_2Y(int)
        Nitaqa['D3'] = calc.MG_3Y(int)
        Nitaqa['B4'] = calc.HG_1Y(int)
        Nitaqa['C4'] = calc.HG_2Y(int)
        Nitaqa['D4'] = calc.HG_3Y(int)
        Nitaqa['B5'] = calc.P_1Y(int)
        Nitaqa['C5'] = calc.P_2Y(int)
        Nitaqa['D5'] = calc.P_3Y(int)
        workbook.save('NID.xlsx')

if __name__ == "__main__":
        R = pyip.inputMenu(["Aramco", "alRajhi", "Nadec", "STC", "ACS", "NTG", "LMS", "NID"],numbered=True)

