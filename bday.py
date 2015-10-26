#!/usr/bin/env python3
"""
Simple python3 program matching the Probability_Birthday_surprise notebook.

"""
from datascience import *
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
import numpy as np

def show_bday(n):
    bd = Table()
    bd["day"] = range(365)
    bd['left']= 364-bd['day']
    bd['frac']=bd['left']/365
    bd["different"] = np.cumprod(bd["frac"])
    bd['some same bday'] = 1-bd['different']
    bd.select('some same bday').take(range(n)).plot()
    return bd

if __name__ == '__main__':
    show_bday(50)
    plots.show()
