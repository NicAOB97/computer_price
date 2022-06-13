# functions to carry out preprocessing of data and test data 

# import dependencies
import pandas as pd 
import re

def ram_name(data):
        
    data['Ram'] = [elem[:-2:] for elem in data['Ram']]
    data['Ram'] = pd.to_numeric(data['Ram'])

    return data

def memory_type(data):

    data['Memory_Type'] = 0

    for i in range(len(data['Memory'])):
        if re.search(r'\bSSD', data['Memory'][i]):
            data['Memory_Type'][i] = 1 

    return data

def screen_res_type(data):
    
    data['ScreenResolutionType'] = 0
    for i in range(len(data['ScreenResolution'])):
        data['ScreenResolutionType'][i] = re.sub('[0-9]+[x][0-9]+', '', data['ScreenResolution'][i])

    data['Touchscreen'] = 0
    x = 'Touchscreen'

    for i in range(len(data['ScreenResolutionType'])):
        if x in data['ScreenResolutionType'][i]:
            data['Touchscreen'][i] = 1

    data['HD'] = 0
    x = 'HD'

    for i in range(len(data['ScreenResolutionType'])):
        if x in data['ScreenResolutionType'][i]:
            data['HD'][i] = 1


    return data

def gpu(data):
    data['Mobile'] = 0
    data['Discrete'] = 0

    x = 'Intel'
    y = 'Nvidia'
    z = 'AMD Radeon'

    for i in range(len(data['Gpu'])):
        if x in data['Gpu'][i]:
            data['Mobile'][i] = 1
        if y in data['Gpu'][i]:
            match =  re.match('\d+[M]' , data['Gpu'][i])
            if match == True :
                data['Mobile'][i] = 1
            else:
                data['Mobile'][i] = 1
        if y in data['Gpu'][i]:
            match =  re.match('[M]\d+' , data['Gpu'][i])
            if match == True:
                data['Mobile'][i] = 1
            else:
                data['Discrete'][i] = 1

    return data

def cpu(data):
    data['cpu_GHz'] = 0

    for i in range(len(data['cpu_GHz'])):
        data['cpu_GHz'][i] = re.findall('(?:\d+\.)?\d+[G][H][z]', data['Cpu'][i])  

    data['cpu_GHz'] = [elem[0][:-3:] for elem in data['cpu_GHz']]
    data['cpu_GHz'] = pd.to_numeric(data['cpu_GHz'])

    return data