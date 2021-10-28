import math
#The Replacments Needed for Each Profession 
def IT_Needed(Total,Saudi):
    return math.ceil(float(Total)*(0.25)-float(Saudi))

def ACC_Needed(Total,Saudi):
    return math.ceil(float(Total)*(0.3)-float(Saudi))
    
def ENG_Needed(Total,Saudi):
    return math.ceil(float(Total)*(0.2)-float(Saudi))

def TENG_Needed(Total,Saudi):
    return math.ceil(float(Total)*(0.25)-float(Saudi))


def LG_1Y(x):
    return (2.47*math.log(x)+19.25)/100
def LG_2Y(x):
    return (2.47*math.log(x)+26.25)/100

def LG_3Y(x):
    return (2.47*math.log(x)+33.25)/100

def MG_1Y(x):
    return (2.47*math.log(x)+22.72)/100
def MG_2Y(x):
    return (2.47*math.log(x)+33.25)/100
def MG_3Y(x):
    return (2.67*math.log(x)+36.72)/100
def HG_1Y(x):
    return (2.67*math.log(x)+26.91)/100
def HG_2Y(x):
    return (2.67*math.log(x)+33.91)/100
def HG_3Y(x):
    return (2.67*math.log(x)+40.91)/100
def P_1Y(x):
    return (2.84*math.log(x)+35.91)/100
def P_2Y(x):
    return (2.84*math.log(x)+42.91)/100
def P_3Y(x):
    return (2.84*math.log(x)+49.91)/100




