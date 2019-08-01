# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:26:23 2019

@author: STEM
"""

import pandas as pd
import plotly
import plotly.offline as plot
import plotly.graph_objs as go


wodf = pd.read_excel("GISdata.xlsx",sheet_name = "womenOccupation")
wodf

womenoccupation = go.Bar(x=wodf["occupation"],y=wodf["women"],
                         marker = {"color" : wodf["women"], "colorscale":"Jet"})

plot([womenoccupation])
