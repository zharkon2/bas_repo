'''
Created on Apr 3, 2018

@author: yosi.aprilius
'''
def split(val, sep):
    for x in (3, 2, 1):
        if val.find(sep * x) != -1:
            return val.split(sep * x)
    return [val]
