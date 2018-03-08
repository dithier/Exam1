# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:20:07 2018

@author: Ithier
"""

d_i = {'index':[2,4,6,8,10],
       'data':["Never",'Gonna','Give','You','Up'],
       'name':'Rick'
      }

d_s = {'index':["Never",'Gonna','Let','You','Down'],
       'data':[2,4,6,8,10],
       'name':'Astley'}
 

def yougetme(d,i):
    return d["index"][i]

print(d_i["index"])