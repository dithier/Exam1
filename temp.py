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
    listing = [x for v in d.values() for x in v]
    return d["data"][listing.index(i)]

""" yougetme(d_s, "Never) should return 2
yougetme(d_i,2) should return Never
"""

test = [x for v in d_i.values() for x in v]
two = test.index(2)

print(yougetme(d_s, "Down"))